import os, subprocess, zipfile, tarfile, glob
from blog.test.compare import *
from blog.test_gentoo import *

def decompress_zip(zip_file, destination):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(destination)

def compile_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.c'):
                source_file = os.path.join(root, file)
                output_file = os.path.splitext(source_file)[0] + '.so'
                command = ['gcc', '-shared', '-o', output_file, '-fPIC', source_file]
                subprocess.run(command)

def process_zip(zip_file_path, destination_directory):
    decompress_zip(zip_file_path, destination_directory)
    compile_files(destination_directory)

    so_files = []

    for root, dirs, files in os.walk(destination_directory):
        for file in files:
            if file.endswith('.so'):
                file_path = os.path.join(root, file)
                so_files.append(file_path)
            """else:
                file_path = os.path.join(root, file)
                os.remove(file_path)"""

    return so_files
  

def remove_zip_extension(filename):
    if filename.endswith(".zip"):
        return filename[:-4]  # Retourne la chaîne sans les 4 derniers caractères (".zip")
    return filename  # La chaîne ne se termine pas par ".zip", pas de modification nécessaire

def decompress_tar(file_tar, destination_dir):
    with tarfile.open(file_tar, "r:bz2") as tar:
    # Extract all contents of the .tar.bz2 file
        tar.extractall(path=destination_dir)


def eval_tp_system(categorie_name, devoir):
    sans_zip = remove_zip_extension(devoir.name)
       
    path_devoirs = "./data/devoirs/"+ categorie_name + "/" + sans_zip
    decompress_zip("./data/devoirs/"+ devoir.name, path_devoirs)
    
    # dossier pour tester
    devoir_txt = os.getcwd() + "/blog/test/resultat_etudiant.txt"
    correction_txt = os.getcwd() + "/blog/test/resultat.txt"

    note = compile_exec_text("./data/corrections/" + categorie_name + "/" + sans_zip +"/src/main.c"
                    ,path_devoirs +'/src', devoir_txt, correction_txt)

    # Iterate over the zip files and delete them
    for zip_file in glob.glob(os.path.join("./data/devoirs", '*.zip')):
        os.remove(zip_file)

    print("All zip files have been deleted.")

    return note

def eval_tp_gentoo(categorie_name, devoir):
    sans_ext = os.path.splitext(devoir.name)[0]
    path_devoirs = "./data/devoirs/"+ categorie_name + "/" + sans_ext
    decompress_tar("./data/devoirs/" + devoir.name, path_devoirs)
    note = run_evaluation_gentoo(path_devoirs + "/tmp/evaluation/evaluation.txt")

    # Iterate over the zip files and delete them
    for bz2_file in glob.glob(os.path.join("./data/devoirs", '*.bz2')):
        os.remove(bz2_file)

    print("All bz2 files have been deleted.")

    return note
