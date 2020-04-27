import json


def generate_json(results: dict):
    return json.dumps(results, indent=4, ensure_ascii=False)


def generate_html(results: dict):
    raise NotImplementedError


def generate_md(results: dict):
    raise NotImplementedError


def write_to_console(results: dict):
    print(results)


def write_to_json_file(json_results: str, filename: str):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json_results)
