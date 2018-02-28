# pycode-analyzer

## Requirements

Install `flake8`

```bash
sudo pip3 install flake8
```

## Run

```bash
python3 test_flake.py
```

## Sample Outpus

```
Analyze resource/plugin.audio.detektorfm/addon.py
3 E265 block comment should start with '# '
4 E501 line too long (125 > 79 characters)
20 W191 indentation contains tabs
3 F401 'os' imported but unused


Analyze resource/bad.py
1 E999 SyntaxError: invalid syntax
1 W292 no newline at end of file
```