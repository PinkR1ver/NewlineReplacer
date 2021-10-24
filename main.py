import win32clipboard

# get str from CLipboard
win32clipboard.OpenClipboard()
text_essay = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

out = text_essay.replace('\r\n',' ')

# Set ste to Clipboard
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(out)
win32clipboard.CloseClipboard()
