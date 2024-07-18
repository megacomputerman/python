import inspect
import os
import tempfile
from file_manager import FileManager
import shutil

def _print_success_message():
    """Imprime a mensagem de sucesso com o nome da função atual"""
    frame = inspect.currentframe().f_back
    function_name = frame.f_code.co_name
    print(f"\033[92mTeste da função '{function_name}' passou OK\033[0m")

def test_copy_file():
    file_manager = FileManager()
    source_file = 'test_source.txt'
    destination_file = 'test_destination.txt'
    with open(source_file, 'w') as f:
        f.write('Este é um arquivo de teste')
    file_manager.copy_file(source_file, destination_file)
    assert os.path.exists(destination_file)
    assert file_manager.compare_hash(source_file, destination_file)
    os.remove(source_file)
    os.remove(destination_file)
    _print_success_message()

def test_copy_directory():
    file_manager = FileManager()
    source_dir = 'test_source_dir'
    destination_dir = 'test_destination_dir'
    os.makedirs(source_dir)
    with open(os.path.join(source_dir, 'file1.txt'), 'w') as f:
        f.write('Este é um arquivo de teste 1')
    with open(os.path.join(source_dir, 'file2.txt'), 'w') as f:
        f.write('Este é um arquivo de teste 2')
    file_manager.copy_directory(source_dir, destination_dir)
    assert os.path.exists(destination_dir)
    assert os.path.exists(os.path.join(destination_dir, 'file1.txt'))
    assert os.path.exists(os.path.join(destination_dir, 'file2.txt'))
    shutil.rmtree(source_dir)
    shutil.rmtree(destination_dir)
    _print_success_message()

def test_delete_file():
    file_manager = FileManager()
    file_path = 'test_file.txt'
    with open(file_path, 'w') as f:
        f.write('Este é um arquivo de teste')
    assert os.path.exists(file_path)
    file_manager.delete_file(file_path)
    assert not os.path.exists(file_path)
    _print_success_message()

def test_list_files():
    file_manager = FileManager()
    directory = 'test_dir'
    os.makedirs(directory)
    with open(os.path.join(directory, 'file1.txt'), 'w') as f:
        f.write('Este é um arquivo de teste 1')
    with open(os.path.join(directory, 'file2.txt'), 'w') as f:
        f.write('Este é um arquivo de teste 2')
    files = file_manager.list_files(directory)
    assert 'file1.txt' in files
    assert 'file2.txt' in files
    shutil.rmtree(directory)
    _print_success_message()

def test_copy_file_if_different():
    file_manager = FileManager()
    source_file = 'test_source.txt'
    destination_file = 'test_destination.txt'
    with open(source_file, 'w') as f:
        f.write('Este é um arquivo de teste')
    assert file_manager.copy_file_if_different(source_file, destination_file)
    assert os.path.exists(destination_file)
    assert file_manager.compare_hash(source_file, destination_file)
    with open(source_file, 'w') as f:
        f.write('Este é um arquivo de teste modificado')
    assert file_manager.copy_file_if_different(source_file, destination_file)
    assert not file_manager.copy_file_if_different(source_file, destination_file)
    os.remove(source_file)
    os.remove(destination_file)
    _print_success_message()

def test_ler_arquivo():
    file_manager = FileManager()
    file_path = 'test_file.txt'
    with open(file_path, 'w') as f:
        f.write('Linha 1\nLinha 2\nLinha 3')
    lines = file_manager.ler_arquivo(file_path)
    assert lines == ['Linha 1', 'Linha 2', 'Linha 3']
    os.remove(file_path)
    _print_success_message()

def test_copy_file_to_multiple_directories():
    file_manager = FileManager()
    file_path = 'test_file.txt'
    directories = ['dir1', 'dir2', 'dir3']
    for directory in directories:
        os.makedirs(directory)
    with open(file_path, 'w') as f:
        f.write('Este é um arquivo de teste')
    file_manager.copy_file_to_multiple_directories(file_path, directories)
    for directory in directories:
        assert os.path.exists(os.path.join(directory, os.path.basename(file_path)))
    os.remove(file_path)
    for directory in directories:
        shutil.rmtree(directory)
    _print_success_message()    

if __name__ == '__main__':
    #test_copy_file()
    #test_copy_directory()
    #test_delete_file()
    #test_list_files()
    #test_copy_file_if_different()
    #test_ler_arquivo()
    #test_copy_file_to_multiple_directories()
    #print('Todos os testes passaram!')
    file_manager = FileManager()

    directory_current = os.getcwd()
    files = file_manager.list_all_files(directory_current)
    print(files)