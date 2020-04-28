import re
from datetime import datetime
from typing import List, Tuple, Dict
from collections import Counter


def get_first_message_date(messages) -> datetime:
    msg_timestamp = messages[-1]['date']
    msg_date = datetime.utcfromtimestamp(msg_timestamp)
    return msg_date


def get_last_message_date(messages) -> datetime:
    msg_timestamp = messages[0]['date']
    msg_date = datetime.utcfromtimestamp(msg_timestamp)
    return msg_date


def get_total_messages_count(messages) -> int:
    return len(messages)


def get_input_messages_count(messages) -> int:
    input_messages = list(filter(lambda m: m['out'] == 0, messages))
    return len(input_messages)


def get_output_messages_count(messages) -> int:
    output_messages = list(filter(lambda m: m['out'] == 1, messages))
    return len(output_messages)


def get_words_from_messages(messages) -> List[str]:
    words = []
    for m in messages:
        msg_words = re.findall(r'\w+', m['text'])
        words.extend(msg_words)
    return words


def get_most_common_words(messages, count) -> List[Tuple[str, int]]:
    """

    :param messages:
    :param count: how much words need to return
    :return: list of tuples ('word', count) like
    """
    words = get_words_from_messages(messages)
    words_counter = Counter(words)
    return words_counter.most_common(count)


def generate_analyze_results(messages) -> Dict:
    results = {
        'total_count': get_total_messages_count(messages),
        'sent_count': get_output_messages_count(messages),
        'received_count': get_input_messages_count(messages),
        'first_message_date': str(get_first_message_date(messages)),
        'last_message_date': str(get_last_message_date(messages)),
        'top_100_most_common_words': get_most_common_words(messages, 100)
    }
    return results

