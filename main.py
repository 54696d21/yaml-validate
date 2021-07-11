import yaml
import sys
import os
from pprint import pprint


def main():
    if len(sys.argv) < 1:
        print("No yaml file specified. Exiting...")
        exit(1)
    run(sys.argv[1])

def run(file):
    if os.path.exists(file):
        with open(file, 'r') as f:
            a = yaml.safe_load(f)
        pprint(a)
    else:
        print("yaml file no found. Exiting...")
        exit(1)


if __name__ == '__main__':
    main()
