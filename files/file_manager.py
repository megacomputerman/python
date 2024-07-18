import os
import shutil
import hashlib

class FileManager:
    def __init__(self):
        pass

    def copy_file(self, source, destination):
        shutil.copyfile(source, destination)

    def copy_directory(self, source, destination):
        shutil.copytree(source, destination)

    def delete_file(self, file_path):
        os.remove(file_path)

    def compare_hash(self, file1, file2):
        hash1 = self._calculate_hash(file1)
        hash2 = self._calculate_hash(file2)
        return hash1 == hash2

    def _calculate_hash(self, file_path):
        with open(file_path, 'rb') as f:
            content = f.read()
            return hashlib.md5(content).hexdigest()

    def list_local_files(self, directory):
        return os.listdir(directory)
    
def list_files(self, directory):
    try:
        files = []
        for element in os.listdir(directory):
            full_path = os.path.join(directory, element)
            if os.path.isfile(full_path):
                files.append(full_path)
            elif os.path.isdir(full_path):
                files.extend(self.list_files(full_path))
        return files
    except OSError as e:
        print(f"Error listing files: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

    def copy_file_to_multiple_directories(file_path, directories):
        for directory in directories:
            shutil.copyfile(file_path, os.path.join(directory, os.path.basename(file_path)))
    
    def copy_file_if_different(self, source, destination):
        if not os.path.exists(destination) or not self.compare_hash(source, destination):
            shutil.copyfile(source, destination)
            return True
        return False

    def ler_arquivo(self, file_path):
        with open(file_path, 'r') as f:
            return [line.strip() for line in f.readlines()]

file_manager = FileManager()
current_directory = os.getcwd()
files = file_manager.list_files(current_directory)
print(files)