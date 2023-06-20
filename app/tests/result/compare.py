import subprocess, os
from time import *

def compile_and_execute_correction(correction_dir):

    # Liste des fichiers C dans le student_src_dir
    fichiers_c = [fichier for fichier in os.listdir(correction_dir) if fichier.endswith('.c')]

    # Commande de compilation
    commande_compilation = ['gcc', '-o', 'program'] + [os.path.join(correction_dir, fichier) for fichier in fichiers_c]

    # Compilation des fichiers
    subprocess.run(commande_compilation, cwd=correction_dir)

    # Exécution du programme et sauvegarde de la sortie dans un fichier
    with open('/home/dini/Projet-application/app/tests/result/resultats.txt', 'w') as output_file:
        subprocess.run('./program', stdout=output_file, cwd=correction_dir, shell=True)

def compile_and_execute(student_src_dir):
    
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
    with open('/home/dini/Projet-application/app/tests/result/resultats_etudiant.txt', 'w') as output_file:
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

    return nb_lignes_identiques/nb_lignes_total * 20

def compile_exec_text(path_src_student):
# def compile_exec_text():

    # genere correction_dir une seul fois des que le TP est transmis
    compile_and_execute_correction('/home/dini/Projet-application/app/tests/sample_correction/src')

    # chaque fois aue l'eleve transmis son travail
    compile_and_execute(path_src_student)

    result = compare('/home/dini/Projet-application/app/tests/result/resultats_etudiant.txt', '/home/dini/Projet-application/app/tests/result/resultats.txt')

    print("Pourcentage: ", result)


