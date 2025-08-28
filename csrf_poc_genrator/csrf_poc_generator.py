from request_parser import main  # This should be renamed to something meaningful like request_parser.py
from urllib.parse import unquote_plus
import html
import webbrowser
import os

ASCII_BANNER = r"""  
   ______   ______   _______    ________   _______    ___      ______  
 .' ___  |.' ____ \ |_   __ \  |_   __  | |_   __ \ .'   `.  .' ___  | 
/ .'   \_|| (___ \_|  | |__) |   | |_ \_|   | |__) /  .-.  \/ .'   \_| 
| |        _.____`.   |  __ /    |  _|      |  ___/| |   | || |        
\ `.___.'\| \____) | _| |  \ \_ _| |_      _| |_   \  `-'  /\ `.___.'\ 
 `.____ .' \______.'|____| |___|_____|    |_____|   `.___.'  `.____ .' 

                                By Pawan Kadwadi
"""
print(ASCII_BANNER)


def parse_request_details(raw_request):
    #raw_request = main()
    #print(raw_request)
    if not raw_request:
        raise ValueError("No request data received.")

    try:
        if "\n\n" in raw_request:
            headers, body = raw_request.split("\n\n", 1)
        else:
            headers, body = raw_request, None

        lines = headers.split("\n")
        method_line = lines[0]
        host_line = next((line for line in lines if line.lower().startswith("host:")), None)

        if not host_line:
            raise ValueError("Missing 'Host' header.")

        method, path, _ = method_line.split(" ", 2)
        host = host_line.split(":", 1)[1].strip()

        url = f"https://{host}{path}"
        return body, method.upper(), url

    except Exception as e:
        print(f"[Error] Invalid request parsed: {e}")
        raise


def data():
    request_data = main()
    if type(request_data) != tuple:
        req_data = parse_request_details(request_data.strip())
        return req_data
    else:
        req_data = request_data
        return req_data


def generate_csrf_html():
    body, method, url = data()
    html_lines = [
        '<!DOCTYPE html>',
        '<html lang="en">',
        '  <head><meta charset="UTF-8"><title>CSRF PoC</title></head>',
        '  <body>',
        '    <h1>CSRF PoC Form</h1>',
        f'    <form method="{method}" action="{url}">'
    ]

    if body:
        try:
            if body.startswith("{"):
                # Handle JSON-like input
                encoded_body = html.escape(body.replace('"', '%22'))
                print(encoded_body)
                html_lines.append(
                    f'      <input type="hidden" name="{encoded_body}" value="">'
                )
            elif "&" in body:
                body_params = dict(item.split("=", 1) for item in body.split("&"))
                for key, value in body_params.items():
                    clean_key = html.escape(unquote_plus(key.strip()))
                    clean_value = html.escape(unquote_plus(value.strip()))
                    html_lines.append(
                        f'      <input type="hidden" name="{clean_key}" value="{clean_value}">'
                    )
            else:
                key, value = body.split("=", 1)
                clean_key = html.escape(unquote_plus(key.strip()))
                clean_value = html.escape(unquote_plus(value.strip()))
                html_lines.append(
                    f'      <input type="hidden" name="{clean_key}" value="{clean_value}">'
                )
        except Exception as e:
            print(f"[Error] Failed to parse body: {e}")

    html_lines += [
        '      <input type="submit" value="Submit Request">',
        '    </form>',
        '  </body>',
        '</html>'
    ]

    return "\n".join(html_lines)


def save_csrf_html(html_content, filename="CSRF_POCcsrf_poc.html"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"[~] CSRF PoC saved to: {os.path.abspath(filename)}")
        return filename
    except Exception as e:
        print(f"[Error] Failed to save HTML: {e}")


def launching_browser():
    html_content = generate_csrf_html()
    filename = save_csrf_html(html_content)
    return webbrowser.open("file://"+os.path.abspath(filename))



if __name__ == "__main__":
    #html_output = generate_csrf_html()
    #save_csrf_html(html_output)
    launching_browser()
