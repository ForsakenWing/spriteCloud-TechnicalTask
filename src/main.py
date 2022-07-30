from subprocess import run
import logging
import sys
import os


def enable_logging():
    logging.basicConfig(level=logging.DEBUG)


def initializing_root_path():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(root_dir)


def run_tests():
    with open('logs/logs.txt', 'w') as file:
        initializing_root_path()
        enable_logging()
        result = run(["python", "-m", "pytest", "-svv"], capture_output=True).stdout
        print(result.decode('utf-8'), file=file)


def main():
    run_tests()


if __name__ == "__main__":
    main()