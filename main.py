import inspect, sys
from array import array
from random import randint
from rich.table import Table
from rich.syntax import Syntax
from rich.console import Console

console = Console()

def print_code():
    """
    Вывод кода программы
    """
    syntax = Syntax(inspect.getsource(sys.modules[__name__]), "python", theme="monokai", line_numbers=True)
    console.print(syntax)

HELLO_MESSAGE = '''
[green]
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█─▄▄▄─█─▄▄─█▄─▄▄─█─▄─▄─█▄─▄▄─█─▄▄─█▄─▄─▀█▄─█─▄██▀▄─██
█─███▀█─██─██─▄▄▄███─████─▄▄▄█─██─██─▄─▀██─▄▀███─▀─██
█▄▄▄▄▄█▄▄▄▄█▄▄▄████▄▄▄██▄▄▄███▄▄▄▄█▄▄▄▄██▄▄█▄▄█▄▄█▄▄█
[/green]
[red]Список команд: [/red]
[dark_orange][bold]c[/bold] - Вывести код программы[/dark_orange]
[gray]---------------------------------------------[/gray]
[salmon1]1 - Произвести сортировку и генерацию массива[/salmon1]
[pale_violet_red1]2 - Произвести сортировку и генерацию списка[/pale_violet_red1]
    '''

def generate_array(size=10) -> array:
    """
    Генерация массива
    size - размер массива
    """
    a = array('I')
    for i in range(size):
        a.append(randint(0,size*10))
    return a

def generate_list(size=10) -> list:
    """
    Генерация списка
    size - размер списка
    """
    l = list()
    for i in range(size):
        l.append(randint(0,size*10))
    return l

if __name__ == '__main__':
    console.print(HELLO_MESSAGE)
    variant = str(input()).lower()
    if variant == 'c' or variant == 'с' or variant == 'код':
        print_code()
    elif variant == '1' or variant == '2':
        console.print('Введите длинну списка/массива:')
        size : int
        try:
            size = int(input())
        except:
            size = 10
        
        #Генерация массива/списка
        data = None
        if variant == '1':
            data = generate_array(size=size)
        elif variant == '2':
            data = generate_list(size=size)
        
        #Запись массива до сортировки
        _data = None
        
        if variant == '1':
            _data = array('I')
        elif variant == '2':
            _data = list()
        
        for i in range(len(data)):
            _data.append(data[i])

        #Создание таблицы
        data_table = Table(title = 'Сортировка ' + str(type(data)), style='blue')
        data_table.add_column('До', justify='center', style='cyan')
        data_table.add_column('После', justify='center', style='green')

        #Сортировка
        for i in range(len(data) - 1):
            _min = i
            j = i + 1
            while j < len(data):
                if data[j] < data[_min]:
                    _min = j
                j+=1
            data[i], data[_min] = data[_min], data[i]
        
        #Вывод результата
        for i in range(len(data)):
            data_table.add_row(str(_data[i]), str(data[i]))
        console.print(data_table)
        console.print('[green]Сортировка окончена![/green]')

    else:
        console.print('[dark_red]ОШИБКА![/dark_red][red]\t\tТакой команды в списке нет[/red]')