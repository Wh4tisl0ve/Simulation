import time


def show_menu() -> None:
    print('Меню')
    items = ['Запустить симуляцию', 'Выход']

    print('=' * (len(max(items, key=len)) + 3))

    for i, item in enumerate(items):
        print(f'{i + 1}. {item}')

    print('=' * (len(max(items, key=len)) + 3))


def show_information():
    print('Для паузы/продолжения симуляции введите любой символ и нажмите Enter')
    time.sleep(3)


def show_incorrect_command_error() -> None:
    print('\n***Нет данной команды***\n')
