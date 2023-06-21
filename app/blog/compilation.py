import os
import subprocess
import zipfile

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