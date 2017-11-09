### Warning

The code under this directory is either imported from [Antlr-Grammar-V4](https://github.com/antlr/grammars-v4) or generated from [Antlr4](https://github.com/antlr/antlr4)

### Usage

Fetch new version of grammar files(.g4) from [Antlr-Grammar-V4](https://github.com/antlr/grammars-v4)

to regenerate python runtime files, first follow the antlr tutorial
[here](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md) to
set up your antlr

Then call the following to generate parser,lexer,and ast walk listener
```
$ antlr4 -Dlanguage=Python3 Chat.g4
```

### License

Beware of the licenses on the individual grammars file. 
