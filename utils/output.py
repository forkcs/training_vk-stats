import json
from string import Template


plain_text_output = '''Conversation with $user_id user.

The conversation starts: $first_message_date
Last message: $last_message_date
Total messages count: $total_count

Top 100 most common words: $top_100_most_common_words'''


def generate_text(results: dict):
    output = Template(plain_text_output).substitute(results)
    return output


def generate_json(results: dict):
    return json.dumps(results, indent=4, ensure_ascii=False)


def generate_html(results: dict):
    raise NotImplementedError


def generate_md(results: dict):
    raise NotImplementedError


def write_to_console(results: dict):
    print(results)


def write_to_file(results: str, filename: str):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(results)
