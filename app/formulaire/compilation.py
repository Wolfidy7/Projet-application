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

    for root, dirs, files in os.walk(destination_directory):
        for file in files:
            if not file.endswith('.so'):
                file_path = os.path.join(root, file)
                os.remove(file_path)