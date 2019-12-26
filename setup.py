"""Ejecutar comandos.

Usage:
    setup.py documents (--delete | --create | --dump)

Options:
    -h --help                           Muestra esta información.
    --version                           Muestra las versiones de este comando.

"""
from docopt import docopt
import importlib
import time
import sys
import os


def main():
    arguments = docopt(__doc__, version='Loe 2019 1.0')
    print(arguments)
    for key in arguments:
        if key[0] != '-' and arguments[key] == True:
            start_time = time.time()
            module = importlib.import_module("bin."+str(key))
            command_ = getattr(module, str(key).replace(
                "_", " ").title().replace(" ", ""))
            instance = command_(arguments)
            instance.exe_command()
            print("Execution time: %s seconds" % (time.time() - start_time))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nEl comando ha sido cerrado')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
