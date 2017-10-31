# Lex Refactor
This project aim to create scripts with Antlr4 and predefined Antlr4 grammars to tokenize code and refactor them

## Usage

[Install Antlr4](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md)

0. Install Java (version 1.6 or higher)
1. Download
```
$ cd /usr/local/lib
$ curl -O http://www.antlr.org/download/antlr-4.7-complete.jar
```
Or just download in browser from website:
    [http://www.antlr.org/download.html](http://www.antlr.org/download.html)
and put it somewhere rational like `/usr/local/lib`.

2. Add `antlr-4.7-complete.jar` to your `CLASSPATH`:
```
$ export CLASSPATH=".:/usr/local/lib/antlr-4.7-complete.jar:$CLASSPATH"
```
It's also a good idea to put this in your `.bash_profile` or whatever your startup script is.

3. Create aliases for the ANTLR Tool, and `TestRig`.
```
$ alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.7-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
$ alias grun='java org.antlr.v4.gui.TestRig'

4. run script by calling `python src/lex_refactor.py`

lease email +yolandyan about any of the bug you've encounted or create issue in this repo
