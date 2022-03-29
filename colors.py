from colorama import Fore


def getForeColor(type='success'):
    color = Fore.BLUE
    if type == 'error':
        color = Fore.RED
    if type == 'warning':
        color = Fore.YELLOW
    return color


def cprint(item="", type='success'):
    print(f"{getForeColor(type)}{item}")
