import sys

from getphoto import cli, __app_name__


def main():
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    # sys.argv.append('--help')
    # sys.argv.append('get-list')
    try:
        main()
    except:
        print('\n')
        print('Use "getphoto.exe --help" to get commands list')
        print('Use "getphoto.exe get-list" to get available photos list')
        print('Use "getphoto.exe get-photo" to download photo', '\n')
        input('Press any key to close ...')

