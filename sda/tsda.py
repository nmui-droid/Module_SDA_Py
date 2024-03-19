import colorama

class Sda():
    def logprint(*args, **kwargs):
        print(*args, **kwargs)

class Sdaa():
    def logerror(*args, **kwargs):
        print(colorama.Fore.RED + "ERR:", *args, **kwargs, end=colorama.Fore.RESET + "\n")
        
    def logwarn(*args, **kwargs):
        print(colorama.Fore.YELLOW + "WARN:", *args, **kwargs, end=colorama.Fore.RESET + "\n")
        
    def logdone(*args, **kwargs):
        print(colorama.Fore.GREEN + "DONE:", *args, **kwargs, end=colorama.Fore.RESET + "\n")
        
    def logshellerr(*args, **kwargs):
        print(colorama.Fore.LIGHTBLUE_EX + "SERR:", *args, **kwargs, end=colorama.Fore.RESET + "\n")