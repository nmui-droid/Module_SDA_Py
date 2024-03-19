class Sda():
    def logprint(*args, **kwargs):
        print(*args, **kwargs)

class Sdaa():
    def logerror(*args, **kwargs):
        print("ERR:", *args, **kwargs)
    def logwarn(*args, **kwargs):
        print("WARN:", *args, **kwargs)
    def logdone(*args, **kwargs):
        print("DONE:", *args, **kwargs)
    def logshellerr(*args, **kwargs):
        print("SERR:", *args, **kwargs)