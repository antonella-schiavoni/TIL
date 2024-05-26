# Today I Learned

## Issue: UnicodeDecodeError with pipreqs

While using `pipreqs` to generate a `requirements.txt` file for my Python project, I encountered the following error:

```
(.venv) ~/Maestria/voice git:[main]
pipreqs
INFO: Not scanning for jupyter notebooks.
Traceback (most recent call last):
  File "/Users/antonellaschiavoni/Maestria/voice/.venv/bin/pipreqs", line 8, in <module>
    sys.exit(main())
  File "/Users/antonellaschiavoni/Maestria/voice/.venv/lib/python3.10/site-packages/pipreqs/pipreqs.py", line 609, in main
    init(args)
  File "/Users/antonellaschiavoni/Maestria/voice/.venv/lib/python3.10/site-packages/pipreqs/pipreqs.py", line 533, in init
    candidates = get_all_imports(
  File "/Users/antonellaschiavoni/Maestria/voice/.venv/lib/python3.10/site-packages/pipreqs/pipreqs.py", line 136, in get_all_imports
    contents = read_file_content(file_name, encoding)
  File "/Users/antonellaschiavoni/Maestria/voice/.venv/lib/python3.10/site-packages/pipreqs/pipreqs.py", line 181, in read_file_content
    contents = f.read()
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb1 in position 81: invalid start byte
```

This error is a `UnicodeDecodeError` and it occurs when `pipreqs` tries to read a file that contains non-UTF-8 characters.

## Solution: Ignoring Certain Directories

The solution I found was to ignore certain directories when running `pipreqs`. This can be done by using the `--ignore` option followed by the directories to ignore, separated by commas. In my case, I ignored the `bin`, `etc`, `include`, `lib`, and `lib64` directories:

```
pipreqs --ignore bin,etc,include,lib,lib64
```

This command successfully generated the `requirements.txt` file without any `UnicodeDecodeError`.