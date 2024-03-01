import pytest
from my_cod import get_dir_info, FileSis

def test_get_dir_info():
    path = 'C:\\Users\Рабочий\Desktop\my_dz' # взял мою директорию, прописал все мои файлы.

    expected_result = [
        FileSis(name='file', extension='.log', is_dir=False, p_dir='my_dz'),
        FileSis(name='my_cod', extension='.py', is_dir=False, p_dir='my_dz'),
        FileSis(name='test', extension='.py', is_dir=False, p_dir='my_dz'),
        FileSis(name='.idea', extension='', is_dir=True, p_dir='my_dz'),
        FileSis(name='.pytest_cache', extension='', is_dir=True, p_dir='my_dz'),
        FileSis(name='__pycache__', extension='', is_dir=True, p_dir='my_dz'),
        FileSis(name='.gitignore', extension='', is_dir=False, p_dir='.idea'),
        FileSis(name='misc', extension='.xml', is_dir=False, p_dir='.idea'),
        FileSis(name='modules', extension='.xml', is_dir=False, p_dir='.idea'),
        FileSis(name='my_dz', extension='.iml', is_dir=False, p_dir='.idea'),
        FileSis(name='workspace', extension='.xml', is_dir=False, p_dir='.idea'),
        FileSis(name='inspectionProfiles', extension='', is_dir=True, p_dir='.idea'),
        FileSis(name='profiles_settings', extension='.xml', is_dir=False, p_dir='inspectionProfiles'),
        FileSis(name='Project_Default', extension='.xml', is_dir=False, p_dir='inspectionProfiles'),
        FileSis(name='.gitignore', extension='', is_dir=False, p_dir='.pytest_cache'),
        FileSis(name='CACHEDIR', extension='.TAG', is_dir=False, p_dir='.pytest_cache'),
        FileSis(name='README', extension='.md', is_dir=False, p_dir='.pytest_cache'),
        FileSis(name='v', extension='', is_dir=True, p_dir='.pytest_cache'),
        FileSis(name='cache', extension='', is_dir=True, p_dir='v'),
        FileSis(name='lastfailed', extension='', is_dir=False, p_dir='cache'),
        FileSis(name='nodeids', extension='', is_dir=False, p_dir='cache'),
        FileSis(name='stepwise', extension='', is_dir=False, p_dir='cache'),
        FileSis(name='my_cod.cpython-311', extension='.pyc', is_dir=False, p_dir='__pycache__'),
        FileSis(name='test.cpython-311-pytest-8.0.1', extension='.pyc', is_dir=False, p_dir='__pycache__')
    ]
    result = get_dir_info(path)

    assert result == expected_result #Сравниваем ожидаемый результат с полученным.

def test_get_dir_info_empty():
    path = './empty_dir'  # создаем пустую тестовую директорию
    expected_result = []
    result = get_dir_info(path)
    assert result == expected_result