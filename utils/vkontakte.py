from typing import List, Dict
import vk_api

import config


def create_api_connection(login: str, password: str):
    vk_session = vk_api.VkApi(login=login, password=password,
                              scope='messages', app_id=config.VK_APP_ID)
    vk_session.auth()
    vk = vk_session.get_api()
    return vk


def get_messages_count(conn, user_id: int) -> int:
    msg_count = conn.messages.getHistory(user_id=user_id, count=1, version=config.VK_API_VERSION)['count']
    return msg_count


def format_raw_message(message: Dict):
    m = message
    return {'date': m['date'], 'out': m['out'], 'text': m['text']}


def fetch_messages_by_user_id(conn, user_id: int, pbar=None) -> List[Dict]:
    """

    :param pbar: progressbar instance
    :param conn: VkApiMethod object
    :param user_id: vk user id
    :return: list of dicts

    TODO: multi-processing or asynchronous fetching
    TODO: fetch with bufering and save chunks to temp file
    """

    messages = []
    msg_count = get_messages_count(conn, user_id)
    if pbar:
        pbar.start()
    for i in range(0, msg_count + (msg_count % config.MESSAGES_PER_REQUEST), config.MESSAGES_PER_REQUEST):
        raw_data = conn.messages.getHistory(user_id=user_id, count=config.MESSAGES_PER_REQUEST, offset=i,
                                            version=config.VK_API_VERSION)
        messages_part = [format_raw_message(m) for m in raw_data['items']]
        messages.extend(messages_part)
        if pbar:
            pbar.update(i)
    if pbar:
        pbar.finish()
    return messages
