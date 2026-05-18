# import pyperclip
import win32clipboard
import markdown
import sys
import os
import re
from Extensions import  CaptionExtension, ExtTableExtension


def html_clipboard_payload(fragment: str) -> bytes:
    html = f"<html><body><!--StartFragment-->{fragment}<!--EndFragment--></body></html>"
    html_bytes = html.encode("utf-8")

    header_template = (
        "Version:0.9\r\n"
        "StartHTML:{start_html:010d}\r\n"
        "EndHTML:{end_html:010d}\r\n"
        "StartFragment:{start_fragment:010d}\r\n"
        "EndFragment:{end_fragment:010d}\r\n"
    )

    header = header_template.format(
        start_html=0,
        end_html=0,
        start_fragment=0,
        end_fragment=0,
    ).encode("ascii")

    start_html = len(header)
    start_fragment = start_html + html_bytes.index(b"<!--StartFragment-->") + len(b"<!--StartFragment-->")
    end_fragment = start_html + html_bytes.index(b"<!--EndFragment-->")
    end_html = start_html + len(html_bytes)

    header = header_template.format(
        start_html=start_html,
        end_html=end_html,
        start_fragment=start_fragment,
        end_fragment=end_fragment,
    ).encode("ascii")

    return header + html_bytes

def copy_html_to_clipboard(fragment: str):
    payload = html_clipboard_payload(fragment)
    html_format = win32clipboard.RegisterClipboardFormat("HTML Format")

    print(payload)
    win32clipboard.OpenClipboard()
    try:
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(html_format, payload)
    finally:
        win32clipboard.CloseClipboard()

if __name__ == "__main__": 
    if(len(sys.argv) <= 1): 
        print("No path specified, exiting...")

    fPath:str = sys.argv[1]
    if(not re.search(".md$", fPath)): 
        print("Path '%s' is not valid .md file..." % (fPath))
    if(not os.path.isfile(fPath)): 
        print("Path '%s' is not valid path..." % (fPath))

    with open(fPath, "r+") as fp:
        textContent:str = fp.read()
        html = markdown.markdown(textContent, extensions=[CaptionExtension(), 'sane_lists', ExtTableExtension()])
        # print(html)
        copy_html_to_clipboard(html)
        