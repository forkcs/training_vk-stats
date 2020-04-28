import sys

from utils.console import parse_arguments, create_progressbar
from utils.output import write_to_console, write_to_file, generate_json, generate_text
from utils.vkontakte import fetch_messages_by_user_id, get_messages_count, create_api_connection
from analyze import generate_analyze_results

if __name__ == '__main__':
    # Parse command-line arguments
    args = parse_arguments()

    # Create VkApiMethod instance to call vk.com API
    vk = create_api_connection(login=args.login, password=args.pwd)

    # Initialize progress bar and fetch messages
    msg_count = get_messages_count(conn=vk, user_id=args.user_id)
    if msg_count == 0:
        print('This dialogue is empty, exiting...')
        sys.exit(0)
    pbar = create_progressbar(max_val=msg_count + (msg_count % 200))
    messsages = fetch_messages_by_user_id(conn=vk, user_id=args.user_id, pbar=pbar)

    # Generate stats and format results
    analyze_results = generate_analyze_results(messsages)
    # Add user id to output data
    output_data = dict(user_id=args.user_id, **analyze_results)

    # Get results according to given output options
    if args.json_filename is not None:
        json_ouptut = generate_json(output_data)
        write_to_file(json_ouptut, args.json_filename)
    else:
        console_output = generate_text(output_data)
        write_to_console(console_output)
