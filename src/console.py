import time

Off = '\033[0m'           # Text Reset
Black = '\033[1;90m'      # Black
Red = '\033[1;91m'        # Red
Green = '\033[1;92m'      # Green
Yellow = '\033[1;93m'     # Yellow
Blue = '\033[1;94m'       # Blue
Purple = '\033[1;95m'     # Purple
Cyan = '\033[1;96m'       # Cyan
White = '\033[1;97m'      # White


def out(*args):
    print(str().join(args))


def log(filename, *args):
    with open(filename, "a") as logfile:
        logfile.write(f"{Blue}{time.asctime()}{Off}")
        [logfile.write(f"\t{statement}\n") for statement in args]
        logfile.write('\n')
