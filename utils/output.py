import json
from datetime import datetime


def write_to_console(start_date=None, last_date=None, msg_count=None, in_count=None, out_count=None):
    if start_date is not None:
        print(f'First message written at {start_date}')
    if last_date is not None:
        print(f'Last messages written at {last_date}')
    if msg_count is not None:
        print(f'Total messages count: {msg_count}')
    if in_count is not None:
        print(f'Input messages count: {in_count}')
    if out_count is not None:
        print(f'Output messages count: {out_count}')


def write_to_json_file(user_id: int, filename,
                       start_date=None, last_date=None, msg_count=None, in_count=None, out_count=None):
    json_data = {'user_id': user_id}
    if start_date is not None:
        json_data['first_message_date'] = str(start_date)
    if last_date is not None:
        json_data['last_message_date'] = str(last_date)
    if msg_count is not None:
        json_data['total_msg_count'] = msg_count
    if in_count is not None:
        json_data['input_msg_count'] = in_count
    if out_count is not None:
        json_data['output_msg_count'] = out_count
    with open(filename, 'w') as f:
        json.dump(json_data, f, indent=4)
