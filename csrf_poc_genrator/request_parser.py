import argparse
import sys
import os
import shlex

def raw_request_parser():
    print("Paste your HTTP request line by line. Type 'END' on a new line to finish:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    return "\n".join(lines)


def curl_request_parser(curl_command):
    command = shlex.split(curl_command)
    method_index = command.index('-X')
    body_index = command.index('-d')
    method = command[method_index+1]
    body = command[body_index+1]
    url = next((line for line in command if line.startswith("http")), None)
    print(method, body, url)
    return body, method, url


def parse_request_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"[Error] File not found: {file_path}")
        return None

    if not file_path.lower().endswith(".txt"):
        print("[Error] Invalid file type. Only '.txt' files are supported.")
        return None

    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"[Error] Unexpected error while reading the file: {str(e)}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Parse raw HTTP request, cURL command, or file input"
    )
    parser.add_argument('--arg', default=None, help='Optional argument')
    parser.add_argument('-c', '--curl_request', help='cURL command string (quoted)')
    parser.add_argument('-t', '--text_file', help='Path to a .txt file containing request')

    args = parser.parse_args()

    if args.text_file:
        request_data = parse_request_from_file(args.text_file)
        return request_data
    elif args.curl_request:
        request_data = curl_request_parser(args.curl_request)
        return request_data
    elif args.arg is None:
        request_data = raw_request_parser()
        return request_data
    else:
        print("[!] No valid input source provided.")
        return


if __name__ == "__main__":
    main()
