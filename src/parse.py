import argparse
import src.console as console

parser = argparse.ArgumentParser()

i_help = "Run with an interactive python interpreter that lives along the script"
I_help = "Interactive python interpreter will remain alive even after the script finishes"
s_help = "Supress all error output to stdout and exclusively output to error logs"
v_help = "Output extra information at runtime"
vv_help = "Like verbose, but updates sleep time at real time"

parser.add_argument("-i", "--interactive", action="store_true", help=i_help)
parser.add_argument("-p", "--persistent", action="store_true", help=I_help)
parser.add_argument("-s", "--silent", action="store_true", help=s_help)
parser.add_argument("-v", "--verbose", action="store_true", help=v_help)
parser.add_argument("-vv", dest="very_verbose", action="store_true", help=vv_help)

args = parser.parse_args()

if args.verbose and args.silent:
    console.Out(console.Yellow, "[WARNING]", console.Off, " Contradictory flags passed. Errors will be excluded from"
                " stdout and stored to a log instead while complementary info will be displayed to stdout.")
