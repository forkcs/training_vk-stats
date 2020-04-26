from typing import List, Dict

import config


def get_messages_count(conn, user_id: int) -> int:
    msg_count = conn.messages.getHistory(user_id=user_id, count=1, version=config.VK_API_VERSION)['count']
    return msg_count


def get_messages_from_user_id(conn, user_id: int, pbar=None) -> List[Dict]:
    """

    :param pbar: progressbar instance
    :param conn: VkApiMethod object
    :param user_id: vk user id
    :return: list of dicts
    """

    messages = []
    msg_count = get_messages_count(conn, user_id)
    for i in range(0, msg_count + (msg_count % 200), 200):
        raw_data = conn.messages.getHistory(user_id=user_id, count=200, offset=i, version=config.VK_API_VERSION)
        messages_part = [{'date': m['date'], 'out': m['out'], 'text': m['text']} for m in raw_data['items']]
        messages.extend(messages_part)
        if pbar:
            pbar.update(i + 200)

    return messages


if __name__ == '__main__':
    import vk_api
    login = input('Enter your login: ')
    pwd = input('Enter your password: ')
    vk_session = vk_api.VkApi(login=login, password=pwd,
                              scope='messages', app_id=config.VK_APP_ID)
    vk_session.auth()
    vk = vk_session.get_api()
    uid = int(input('Enter user id: '))
    msg_list = get_messages_from_user_id(conn=vk, user_id=uid)
    for msg in msg_list:
        prefix = 'Вы: ' if msg['out'] else 'Собеседник: '
        print(f'{prefix}{msg["text"]}')
