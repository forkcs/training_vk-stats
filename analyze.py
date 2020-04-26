from datetime import datetime


def get_first_message_date(messages):
    msg_timestamp = messages[-1]['date']
    msg_date = datetime.utcfromtimestamp(msg_timestamp)
    return msg_date


def get_last_message_date(messages):
    msg_timestamp = messages[0]['date']
    msg_date = datetime.utcfromtimestamp(msg_timestamp)
    return msg_date


def get_input_messages_count(messages):
    input_messages = list(filter(lambda m: m['out'] == 0, messages))
    return len(input_messages)


def get_output_messages_count(messages):
    output_messages = list(filter(lambda m: m['out'] == 1, messages))
    return len(output_messages)
