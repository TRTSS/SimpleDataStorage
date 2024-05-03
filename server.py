import main
import sys


def base_storge_dir():
    print(main.BASE_STORAGE_DIR)


if __name__ == '__main__':
    cmd = sys.argv[1]

    if cmd == 'storage_dir':
        base_storge_dir()