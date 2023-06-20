import subprocess, os

def compile_and_execute_correction():
    # Chemin du correction
    # contenant les fichiers C
    correction = '/home/dini/Projet-application/app/formulaire/tests/sample_correction/src'

    # Liste des fichiers C dans le dossier
    fichiers_c = [fichier for fichier in os.listdir(correction) if fichier.endswith('.c')]

    # Commande de compilation
    commande_compilation = ['gcc', '-o', 'program'] + [os.path.join(correction, fichier) for fichier in fichiers_c]

    # Compilation des fichiers
    subprocess.run(commande_compilation, cwd=correction)

    # Commande d'exécution
    commande_execution = ['./program']

    # # Exécution du programme
    subprocess.run(commande_execution, cwd=correction)

def compile_and_execute(student_dir):
    
    # Chemin du code d'eleve
    # contenant les fichiers C
    dossier = student_dir + '/src'

    # Liste des fichiers C dans le dossier
    fichiers_c = [fichier for fichier in os.listdir(dossier) if fichier.endswith('.c')]

    # Commande de compilation
    commande_compilation = ['gcc', '-o', 'program'] + [os.path.join(dossier, fichier) for fichier in fichiers_c]

    # Compilation des fichiers
    subprocess.run(commande_compilation, cwd=dossier)

    # Commande d'exécution
    commande_execution = ['./program']

    # Exécution du programme
    subprocess.run(commande_execution, cwd=dossier)

def verifier_lignes_identiques(student_file, correction_text):
    with open(student_file, 'r') as file1, open(correction_text, 'r') as file2:
        lignes1 = file1.readlines()
        lignes2 = file2.readlines()

    nb_lignes_identiques = 0
    nb_lignes_total = len(lignes1)

    # Vérification des lignes identiques
    for ligne1, ligne2 in zip(lignes1, lignes2):
        if ligne1 == ligne2:
            nb_lignes_identiques += 1

    print(f"Nombre total de lignes : {nb_lignes_total}")
    print(f"Nombre de lignes identiques : {nb_lignes_identiques}")

    return nb_lignes_identiques/nb_lignes_total

# genere correction une seul fois des que le TP est transmis
compile_and_execute_correction()

# chaque fois aue l'eleve transmis son travail
compile_and_execute('/home/dini/Projet-application/app/formulaire/tests/sample_etudiant')

# comparer les resultats
result = verifier_lignes_identiques('resultats_etudiant.txt', 'resultats.txt')
print(f"Pourcentage : {result}")