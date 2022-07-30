from subprocess import run
import logging
import sys
import os
import requests
from configparser import ConfigParser


def enable_logging():
    logging.basicConfig(level=logging.INFO)


def initializing_root_path():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(root_dir)


def send_report():
    with open('result/report.xml') as file:
        if os.path.exists('config.ini'):
            cfg = ConfigParser()
            cfg.read('config.ini')
            sensitive_data = dict(cfg.items('secrets'))
            requests.post(
                url=f"https://app.calliope.pro/api/v2/profile/"
                    f"{sensitive_data['profile_id']}/import/junit",
                headers={"x-api-key": sensitive_data['api_key']},
                files={
                    'ignore_empty_report': True,
                    'ignore_empty_import': True,
                    'file[]': ('report.xml', file, 'application/xml', {'Expires': '0'})
                }
            )


def run_tests():
    if not os.path.exists('result'):
        os.mkdir('result')
    initializing_root_path()
    enable_logging()
    run(
        [
            "python", "-m", "pytest",
            "--junit-xml=result/report.xml",
        ], capture_output=True
    )


def main():
    run_tests()
    send_report()


if __name__ == "__main__":
    main()
