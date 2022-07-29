from subprocess import run
import logging


def enable_logging():
    logging.basicConfig(level=logging.DEBUG)


def run_tests():
    with open('logs/logs.txt', 'w') as file:
        enable_logging()
        result = run(["python", "-m", "pytest", "-svv"], capture_output=True).stdout
        print(result.decode('utf-8'), file=file)


def main():
    run_tests()


if __name__ == "__main__":
    main()