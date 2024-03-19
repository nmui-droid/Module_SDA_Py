# MODULE SDA

* A new module to print
* It's so easy to use


````py
from colorama import Fore, Style

class Sda:
    def logprint(*args, **kwargs):
        print(*args, **kwargs)

class Sdaa:
    def logerror(*args, **kwargs):
        print(Fore.RED + "ERR:", *args, **kwargs, end=Style.RESET_ALL + "\n")

    def logwarn(*args, **kwargs):
        print(Fore.YELLOW + "WARN:", *args, **kwargs, end=Style.RESET_ALL + "\n")

    def logdone(*args, **kwargs):
        print(Fore.GREEN + "DONE:", *args, **kwargs, end=Style.RESET_ALL + "\n")

    def logshellerr(*args, **kwargs):
        print(Fore.LIGHTBLUE_EX + "SERR:", *args, **kwargs, end=Style.RESET_ALL + "\n")

#Easy to use this
````
# A module can replace normal print()
* Easy to use. There are all different colors and hues.
* Click here to install.
<button><a href="">Click here</a></button>