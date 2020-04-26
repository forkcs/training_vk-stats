import sys
import vk_api

import config
from utils.console import parse_arguments, create_progressbar
from utils.output import write_to_console, write_to_json_file
from utils.vkontakte import fetch_messages_by_user_id, get_messages_count
from analyze import get_first_message_date, get_last_message_date, \
    get_input_messages_count, get_output_messages_count

if __name__ == '__main__':
    args = parse_arguments()
    vk_session = vk_api.VkApi(login=args.login, password=args.pwd,
                              scope='messages', app_id=config.VK_APP_ID)
    vk_session.auth()
    vk = vk_session.get_api()
    msg_count = get_messages_count(conn=vk, user_id=args.user_id)
    if msg_count == 0:
        print('This dialogue is empty, exiting...')
        sys.exit(0)

    pbar = create_progressbar(max_val=msg_count + (msg_count % 200))
    messsages = fetch_messages_by_user_id(conn=vk, user_id=args.user_id, pbar=pbar)

    first = get_first_message_date(messsages)
    last = get_last_message_date(messsages)
    in_count = get_input_messages_count(messsages)
    out_count = get_output_messages_count(messsages)
    if args.json_filename is not None:
        write_to_json_file(user_id=args.user_id, filename=args.json_filename,
                           start_date=first, last_date=last, in_count=in_count,
                           out_count=out_count, msg_count=msg_count)
    else:
        write_to_console(start_date=first, last_date=last, in_count=in_count,
                         out_count=out_count, msg_count=msg_count)
