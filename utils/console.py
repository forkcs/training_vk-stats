"""
args:
--json
--auth-app-id=
--login=
--pwd=
--user-id=
"""
import argparse
import progressbar


def create_progressbar(max_val: int):
    pbar = progressbar.ProgressBar(maxval=max_val, widgets=[
        'Fetching messages...',  # Статический текст
        progressbar.Bar(left='[', marker='=', right=']'),  # Прогресс
        progressbar.SimpleProgress(),  # Надпись "6 из 10"
    ])
    return pbar


def parse_arguments():
    parser = argparse.ArgumentParser(description='Analyze dialogue messages.', add_help=True)
    parser.add_argument('--login', type=str, help='Login or phone number.')
    parser.add_argument('--pwd', type=str, help='Password.')
    parser.add_argument('--user-id', type=int, help='Id of the user, to analyze conversation history to.')
    parser.add_argument('--json-filename', type=str, default=None,
                        help='Filename to write json-formatted data in.')
    args = parser.parse_args()
    return args
