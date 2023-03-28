import os
from datetime import datetime
from functools import wraps


def logger(old_function):
    full_path = os.getcwd() + '/main.log'

    @wraps(old_function)
    def new_function(*args, **kwargs):
        start = datetime.now().strftime('%Y-%m-%d время: %H:%M:%S:%f(2)')[:-6]
        name_function = old_function.__name__
        arguments = (', '.join(
            [str(arg) for arg in args]) if args else 'Нет аргументов'
        )
        kwarguments = (
            ', '.join([f'{key}={value}' for key, value in kwargs.items()])
            if kwargs else 'Нет аргументов'
        )
        results = old_function(*args, **kwargs)
        with open(full_path, 'a', encoding='utf-8') as f:
            f.write(f'Время запуска: {start}\n'
                    f'Название функции: {name_function}\n'
                    f'Передаваемые аргументы: {arguments, kwarguments}\n'
                    f'Результат выполнения: {results}\n'
                    f'{"*" * 50}\n')
        return results
    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(
            item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()