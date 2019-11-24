## Installation Instruction


HIPHOP is built with Python3, along with multiple modules. To install these, perform the following steps:

1. Install Python3 via https://www.python.org/downloads/
2. After Python3 has been installed
	1. Install opencv with 
		```
		pip3 install opencv-python
		```

## EBNF

```
<HHE> ::= <id>
        | open <filename> as <id>
        | save <id> as <filename>
        | apply <func> to <id>
        | apply-all [<funcs>] to <id>
        | save-macro [<funcs>] as <id>

<filename> ::= "<literal>"

<funcs> ::= <func>
        | <func>, <funcs>

<func> ::= <id> <nums>

<literal> ::= STRING

<nums> ::= 
         | <num> <nums>
```