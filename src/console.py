from src.parse import args as arguments
from threading import Thread
import pathlib as pl
import code
import time
import sys

Off = '\033[0m'           # Text Reset
Black = '\033[1;90m'      # Black
Red = '\033[1;91m'        # Red
Green = '\033[1;92m'      # Green
Yellow = '\033[1;93m'     # Yellow
Blue = '\033[1;94m'       # Blue
Purple = '\033[1;95m'     # Purple
Cyan = '\033[1;96m'       # Cyan
White = '\033[1;97m'      # White


def Interact(globals_var):
    if arguments.interactive or arguments.persistent:
        t = Thread(target=code.InteractiveConsole(locals=globals_var).interact)
        t.start()
        return t
    return Thread()


def Join(thread: Thread):
    if arguments.persistent:
        if thread.is_alive():
            thread.join(timeout=30)


def Out(*args):
    print(str().join(args) if not arguments.silent else '')


def Log(filename, *args):
    try:
        with open(filename, "a") as logfile:
            logfile.write(f"{Blue}{time.asctime()}{Off}")
            [logfile.write(f"\t{statement}\n") for statement in args]
            logfile.write('\n')

    except FileNotFoundError:
        pl.Path(''.join([f"/{i}" for i in filename.split('/')[0:-1] if i != ''])).mkdir(parents=True, exist_ok=True)
        Log(filename, args)


def Verbose(*args):
    Log(f"{sys.path[0]}/assets/logs/runtime.log")
    if arguments.verbose or arguments.very_verbose:
        Out(*args)
        Log(f"{sys.path[0]}/assets/logs/verbose.log")
