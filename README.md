# NewlineReplacer is a useful tool to replace your newline with space. It is very useful when you want to copy some essays.😏
## Awkward Situation:
Do you have this moment:
* Want to translate your essay to Chinese, but when you put them into Google Translator, it was so many new lines you heed to remove.
* DDL is in tonight, you want to copy essay qucikly, but you are be bothered by the newline when you copy from pdf.

![Demo](img/Google%20Translator%20Problem.gif)

**Here**, the NewlineReplacer Coming!🔥

## You need:
```
python
py32win
```

## What you need to do is just Run the NewlineReplacer.exe😏💖 and you can just copy from your ewssay pdf without newlines!!!!🔥
![Solved](img/Problem%20Solved.gif)
If you want to see the details of the code, you can check main.py. It's very simple.
But it's still a question is that if you do not add:
```
time.sleep(...)
```
You will get errors for some reasons. It seems that if you are using `win32clipboard.OpenClipboard()`, you can not do paste operation before `win32clipboard.CloseClipboard()`. I am not sure about this. If you know something, **pls email me**.

## Final Notice:🚧
You may be not able to open the NewlineReplacer.exe or run the main.py, that's because **`Specified clipboard format is not available`**. You may copy some imgs or something, that will cause the exe stopping.