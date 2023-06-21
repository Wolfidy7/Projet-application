import subprocess, os
from time import *
import shutil

def compile_and_execute_correction(correction_dir, text):

    # Liste des fichiers C dans le student_src_dir
    fichiers_c = [fichier for fichier in os.listdir(correction_dir) if fichier.endswith('.c')]

    # Commande de compilation
    commande_compilation = ['gcc', '-o', 'program'] + [fichier for fichier in fichiers_c]

    # Compilation des fichiers
    subprocess.run(commande_compilation, cwd=correction_dir)

    # Exécution du programme et sauvegarde de la sortie dans un fichier
    with open(text, 'w') as output_file:
        subprocess.run('./program', stdout=output_file, cwd=correction_dir, shell=True)

def compile_and_execute(student_src_dir, resultat_etudiant):
    
    # Chemin du code d'eleve
    # contenant les fichiers C
    student_src_dir = student_src_dir

    # Liste des fichiers C dans le student_src_dir
    fichiers_c =  [fichier for fichier in os.listdir(student_src_dir) if fichier.endswith('.c')]

    # Commande de compilation
    commande_compilation = ['gcc', '-o', 'program'] + [fichier for fichier in fichiers_c]

    # Compilation des fichiers
    subprocess.run(commande_compilation, cwd=student_src_dir)

    # Exécution du programme et sauvegarde de la sortie dans un fichier
    with open(resultat_etudiant, 'w') as output_file:
        subprocess.run('./program', stdout=output_file, cwd=student_src_dir, shell=True)

def compare(student_text, correction_text):

    with open(student_text, 'r') as file1, open(correction_text, 'r') as file2:
        lignes1 = file1.readlines()
        lignes2 = file2.readlines()

    nb_lignes_identiques = 0
    nb_lignes_total = len(lignes2)

    # Vérification des lignes identiques
    for ligne1, ligne2 in zip(lignes1, lignes2):
        if ligne1 == ligne2:
            nb_lignes_identiques += 1

    print(f"Nombre total de lignes : {nb_lignes_total}")
    print(f"Nombre de lignes identiques : {nb_lignes_identiques}")

    return (nb_lignes_identiques/nb_lignes_total) * 20

def compile_exec_text(path_main_prof, path_src_student, resultat_etudiant, resultat_prof): #compilation et exécution pour l'étudiant
# def compile_exec_text():

    # copy main file
    shutil.copy(path_main_prof, path_src_student)
        

    # chaque fois aue l'eleve transmis son travail
    compile_and_execute(path_src_student, resultat_etudiant)

    result = compare(resultat_etudiant, resultat_prof)
    print("Note obtenue:", result)
    return result

