import os
import subprocess
import zipfile

def decompress_zip(zip_file, destination):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(destination)

import os
import subprocess

def compile_files(directory):
    for root, dirs, files in os.walk(directory):
        source_files = []
        
        for file in files:
            if file.endswith('.c'):
                source_file = os.path.join(root, file)
                source_files.append(source_file)
        
        if source_files:
            source_directory = os.path.dirname(source_files[0])
            object_files = []
            
            for source_file in source_files:
                object_file = os.path.splitext(source_file)[0] + '.o'
                command = ['gcc', '-c', '-o', object_file, source_file]
                subprocess.run(command)
                object_files.append(object_file)
            
            output_file = os.path.join(directory, 'output.so')
            command = ['gcc', '-shared', '-o', output_file] + object_files
            subprocess.run(command)

            for object_file in object_files:
                os.remove(object_file)


def process_zip(zip_file_path, destination_directory):
    decompress_zip(zip_file_path, destination_directory)
    compile_files(destination_directory)

    so_files = []

    for root, dirs, files in os.walk(destination_directory):
        for file in files:
            if file.endswith('.so'):
                file_path = os.path.join(root, file)
                so_files.append(file_path)
            else:
                file_path = os.path.join(root, file)
                os.remove(file_path)

    return so_files
  
zip_file_path = '/home/ibtissam/Téléchargements/TP_ibtissam_JENNATE.zip'
destination_directory = '/home/ibtissam/Téléchargements/'

so_files = process_zip(zip_file_path, destination_directory)
print("Fichiers .so trouvés :", so_files)
# for file_path in so_files:
#     print(file_path)
