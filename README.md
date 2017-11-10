# Better Call Saul.py 👍📞👨⚖️⚫🐍

- Are you frustrated with writing log calls or other statement over and over?
- Are you frustrated with time consuming code refactor that a 5-year can do?
- Do you know you have rights as a software develper? 

Well, you **better call saul.py**

This project aim to create scripts with Antlr4 and predefined Antlr4 grammars
to tokenize source code and refactor them

## Prerequisites

1. Python3 (investigating a python2 antlr runtime bug)

## Installation

0. (Optional) [Install Antlr4](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md).
You only need this if you want to generate new lex/parser file for a language

1. **Install Antlr4 Python3 runtime**
```bash
pip3 install antlr4-python3-runtime
```

2. **Download this repo to your source code repository**
```bash
git clone https://github.com/yoland68/saul
```

## Usage

- Better call ⤵ to log every statement in a Javafile
```
python3 saul/src/saul.py -a android-add-log -f [path-to-file]
```
- Better call ⤵ to log every statement in a method
```
python3 saul/src/saul.py -a android-add-log -f [path-to-file] --method-declaration [method-name]
```
- Better call ⤵ to log method call with specific name
```
python3 saul/src/saul.py -a android-add-log -f [path-to-file] --method-invocation [method-name]
```
- Better call ⤵ to trace every statement in a Javafile
```
python3 saul/src/saul.py -a android-add-trace -f [path-to-file]
```
- Better call ⤵ to learn how to use saul.py
```
python3 saul/src/saul.py -h
```
- Better call ⤵ to find out all the available Saul agents
```
python3 saul/src/saul.py -l
```

## Links

- [Install Antlr4](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md)
