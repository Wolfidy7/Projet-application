def extract_section(file_path, section_name):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    section = []
    is_section = False

    for index, line in enumerate(lines):
        if line.startswith(section_name) and lines[index + 1].startswith("="):
            is_section = True
            section.append(line)
            continue
        elif is_section:
            section.append(line)
            if line.startswith("=") and lines[index - 1].strip() != section_name:
                break

    if section:
        return section

    return None


def verify_cron(section):
    if section is None:
        return False

    expected_cron_job = "37 13 * * * root /bin/tar czf /mnt/backup/data.tar.gz /home/toto/data"

    # Parcourir chaque ligne de la section
    for line in section:
        if line.strip().startswith(expected_cron_job.strip()):
            return True

    return False


def verify_syslog(section):
    if section is None:
        return False

    expected_line = "destination loginLog { file(\"/var/log/login.log\"); };"

    for line in section:
        if line.strip() == expected_line:
            return True

    return False


def verify_apache(section):
    if section is None:
        return False

    apache_started = False
    proftpd_started = False
    in_default_runlevel = False

    for line in section:
        if "Runlevel: default" in line:
            in_default_runlevel = True
        if "apache2" in line and in_default_runlevel:
            apache_started = True
        if "proftpd" in line  and in_default_runlevel:
            proftpd_started = True

    if apache_started and proftpd_started:
        return True

    return False


def verify_hostname_configuration(section):
    if section is None:
        return False

    for line in section[2:-1]:
        if line.strip() != "":
            return True

    return False
def verify_disk_configuration(section):
    required_partitions = {
        '/boot': 'ext2',  # Partition /boot avec système de fichiers ext2 requis
        '/': 'ext3',  # Partition / avec système de fichiers ext3 requis
        'none': 'swap',  # Partition swap requise
        '/backup': 'ext3',  # Partition /backup avec système de fichiers ext3 requis
        '/data': 'ext3'  # Partition /data avec système de fichiers ext3 requis
    }

    for line in section:
        if line.lower().startswith(('/dev/sd', '/dev/vg')):
            fields = line.split()
            partition = fields[1]
            filesystem = fields[2]

            if partition in required_partitions:
                if filesystem.lower() != required_partitions[partition].lower():
                    print(f"Le système de fichiers de la partition {partition} n'est pas correct.")
                    return False
                del required_partitions[partition]

    missing_partitions = [partition for partition in required_partitions if required_partitions[partition] is not None]
    if missing_partitions:
        for partition in missing_partitions:
            print(f"La partition {partition} est manquante.")
        return False

    return True




def check_lvm(lvm_section):
    vg_present = False
    backup_present = False
    backup_mounted = False
    data_present = False
    data_mounted = False

    for line in lvm_section:
        if line.strip() == '--- Volume group ---':
            vg_present = True
            break

    for line in lvm_section:
        if line.strip() == '--- Logical volume ---':
            backup_present = True
            break

    for line in lvm_section:
        if line.strip().startswith('LV Path'):
            lv_path = line.split()[2].strip().lower()  # Convertir en minuscules
            if lv_path == ('/dev/vg1/backup').strip().lower():  # Convertir en minuscules
                backup_mounted = True
                break
 
    for line in lvm_section:
        if line.strip() == '--- Logical volume ---':
            data_present = True
            break
    for line in lvm_section:
        if line.strip().startswith('LV Path'):
            lv_path = line.split()[2].strip().lower()
            if lv_path == '/dev/vg1/data':
                data_mounted = True
                break


    return vg_present and backup_present and backup_mounted and data_present and data_mounted


def run_evaluation_gentoo(file_path):

    sections = {
        "CRON": {
            "verification_function": verify_cron,
            "points": 3,
            "message_missing": "La section 'Cron Configuration' est manquante dans le fichier."
        },
        "SYSLOG": {
            "verification_function": verify_syslog,
            "points": 3,
            "message_missing": "La section 'Syslog Configuration' est manquante dans le fichier."
        },
        "APACHE": {
            "verification_function": verify_apache,
            "points": 3,
            "message_missing": "La section 'Apache Configuration' est manquante dans le fichier."
        },
        "HOSTNAME": {
            "verification_function": verify_hostname_configuration,
            "points": 2,
            "message_missing": "La section 'Hostname Configuration' est manquante dans le fichier."
        },
        "DISK": {
            "verification_function": verify_disk_configuration,
            "points": 5,
            "message_missing": "La section 'Disk Configuration' est manquante dans le fichier."
        },
        "LVM": {
            "verification_function": check_lvm,
            "points": 4,
            "message_missing": "La section 'LVM Configuration' est manquante dans le fichier."
        }
    }

    note = 0

    for section_name, section_info in sections.items():
        section = extract_section(file_path, section_name)
        if section:
            if section_info["verification_function"](section):
                note += section_info["points"]
                print(section_name, " good")
            else:
                print(section_name, "not good")
        else:
            print(section_info["message_missing"])

    print("La note finale est", note)

    return note
