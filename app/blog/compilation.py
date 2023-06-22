import os, subprocess, zipfile, tarfile, glob
from blog.test.compare import *
from blog.test_gentoo import *
from blog.test_irc import *

def decompress_zip(zip_file, destination):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(destination)
  

def remove_zip_extension(filename):
    if filename.endswith(".zip"):
        return filename[:-4]  # Retourne la chaîne sans les 4 derniers caractères (".zip")
    return filename  # La chaîne ne se termine pas par ".zip", pas de modification nécessaire

def decompress_tar(file_tar, destination_dir):
    with tarfile.open(file_tar, "r:bz2") as tar:
    # Extract all contents of the .tar.bz2 file
        tar.extractall(path=destination_dir)


def eval_tp_system(categorie_name, devoir, student_name):

    print(devoir)
    sans_zip = remove_zip_extension(devoir.name)
    zipfile = "./data/devoirs/"+ devoir.name
       
    path_devoirs = "./data/devoirs/"+ categorie_name + "/" + sans_zip
    decompress_zip(zipfile, path_devoirs)
    
    # dossier pour tester
    devoir_txt = os.getcwd() + "/blog/test/resultat_etudiant.txt"
    correction_txt = os.getcwd() + "/blog/test/resultat.txt"
    destination = "./data/student_files/" + categorie_name + "/" + student_name

    # Vérifier si le dossier de destination existe, sinon le créer
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    # Copier le fichier ZIP vers la destination
    shutil.copy2(zipfile, destination)

    note = compile_exec_text("./data/corrections/" + categorie_name + "/" + sans_zip +"/src/main.c"
                    ,path_devoirs +'/src', devoir_txt, correction_txt)

    # Iterate over the zip files and delete them
    for zip_file in glob.glob(os.path.join("./data/devoirs", '*.zip')):
        os.remove(zip_file)

    print("All zip files have been deleted.")

    return note

def eval_tp_gentoo(categorie_name, devoir, student_name):
    sans_ext = os.path.splitext(devoir.name)[0]
    tarfile = "./data/devoirs/" + devoir.name
    path_devoirs = "./data/devoirs/"+ categorie_name + "/" + sans_ext

    decompress_tar("./data/devoirs/" + devoir.name, path_devoirs)
    note = run_evaluation_gentoo(path_devoirs + "/tmp/evaluation/evaluation.txt")

    destination = "./data/student_files/" + categorie_name + "/" + student_name

    # Vérifier si le dossier de destination existe, sinon le créer
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    # Copier le fichier ZIP vers la destination
    shutil.copy2(tarfile, destination)

    # Iterate over the zip files and delete them
    for bz2_file in glob.glob(os.path.join("./data/devoirs", '*.bz2')):
        os.remove(bz2_file)

    print("All bz2 files have been deleted.")

    return note


def compile_server_irc(student_src_dir):

    student_src_dir = student_src_dir

    # Liste des fichiers C dans le student_src_dir
    fichiers_c =  [fichier for fichier in os.listdir(student_src_dir) if fichier.endswith('.c') and fichier != "ircclient.c"]

    # Commande de compilation
    commande_compilation = ['gcc', '-o', 'ircserver'] + [fichier for fichier in fichiers_c]

    # Compilation des fichiers
    subprocess.run(commande_compilation, cwd=student_src_dir)

def compile_client_irc(student_src_dir):

    student_src_dir = student_src_dir

    # Liste des fichiers C dans le student_src_dir
    fichiers_c =  [fichier for fichier in os.listdir(student_src_dir) if fichier.endswith('.c') and fichier != "ircserver.c"]

    # Commande de compilation
    commande_compilation = ['gcc', '-o', 'ircclient'] + [fichier for fichier in fichiers_c]

    # Compilation des fichiers
    subprocess.run(commande_compilation, cwd=student_src_dir)


def eval_tp_reseau(categorie_name, devoir, student_name):

    sans_zip = remove_zip_extension(devoir.name)
    zipfile = "./data/devoirs/"+ devoir.name
       
    path_devoirs = "./data/devoirs/"+ categorie_name + "/" + sans_zip
    decompress_zip(zipfile, path_devoirs)

    compile_server_irc(path_devoirs + "/src")
    compile_client_irc(path_devoirs + "/src")

    note = start_server(path_devoirs + "/src")


    destination = "./data/student_files/" + categorie_name + "/" + student_name

    # Vérifier si le dossier de destination existe, sinon le créer
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    # Copier le fichier ZIP vers la destination
    shutil.copy2(zipfile, destination)


    # Iterate over the zip files and delete them
    for zip_file in glob.glob(os.path.join("./data/devoirs", '*.zip')):
        os.remove(zip_file)

    print("All zip files have been deleted.")

    return note