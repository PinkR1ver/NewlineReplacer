import win32clipboard
import time
from sys import platform
if platform == "linux" or platform == "linux2":
    my_os = 'linux'
elif platform == "darwin":
    my_os = 'mac'
elif platform == "win32":
    my_os = 'windows'


if my_os == 'windows':
    # first get str from CLipboard
    try:
        win32clipboard.OpenClipboard()
        current_clipboard = win32clipboard.GetClipboardData()
        out = current_clipboard.replace('\r\n', ' ')
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(out)
        win32clipboard.CloseClipboard()
    except:
        win32clipboard.CloseClipboard()

    while True:
        try:
            while True:
                    # mointor clipboard
                    time.sleep(2) # important step, or will error, idk right now
                    win32clipboard.OpenClipboard()
                    text_essay = win32clipboard.GetClipboardData()
                    win32clipboard.CloseClipboard()

                    if '\r\n' in text_essay or '\n' in text_essay:
                        out = text_essay.replace('\r\n', ' ').replace('\n', ' ')

                        # Set str to Clipboard
                        win32clipboard.OpenClipboard()
                        win32clipboard.EmptyClipboard()
                        win32clipboard.SetClipboardText(out)
                        win32clipboard.CloseClipboard()
        except:
            win32clipboard.CloseClipboard()
            print("Not text in cilpboard")
