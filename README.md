This weekend I fooled around with WASM and libreoffice, trying to make a docx editor for vscode.
If I had my way, I'd want vscode to be a "universal editor", I could edit anything from a docx to a stl to svg to c# with no problems.

A man can dream I guess

Well anyways if you want to run this for now, do:

```
chmod +x serve.py
./serve.py
```

I didn't figure how to get the files in or out, but there is a virtual FS in the system.
Thanks to [allotropia](https://lab.allotropia.de/wasm/) for developing this, I don't take any credit.
