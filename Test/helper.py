from colorama import init, Fore

init(convert=True)

def display(message, is_warning=False):
    if is_warning:
        print(Fore.RED + message)
    else:
        print(Fore.GREEN + message)