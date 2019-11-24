## Installation Instruction

HIPHOP is built with Python3, along with multiple modules. To install these, perform the following steps:

1. Install Python3 via https://www.python.org/downloads/
2. After Python3 has been installed
	1. Install OpenCV with ```pip3 install opencv-python```
	2. Install Termcolor with ```pip3 install termcolor```
	3. Install Colorama with ```pip3 install colorama```
3. Ensure that git is installed, following instructions on https://www.atlassian.com/git/tutorials/install-git
4. Download the v0.1 release of hiphop-lang on https://github.com/kristenkwong/hiphop-lang/releases/tag/v0.1-alpha

## Running Instruction

HIPHOP can be used in two ways: command line mode and running a HIPHOP script
(may have to use python3 instead of python depending on which platform you are on)

Command line mode that reads in line by line:
1. In terminal, cd to the directory containing main.py
2. Enter command line mode by ```python main.py```

Running script written in HIPHOP:
1. In terminal, cd to the directory containing main.py
2. Run the script by ```python main.py <location of script>```

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

## Functions Provided By HIPHOP

* open ***filename*** as ***id***
	* this would open file specified at ***filename*** as ***id***
	* ***filename*** has to be in double quote
	* ex. to open a file in the testing/images folder and save as test-img
	  ```open "testing/images/test-color.jpg" as test-img``` 
* apply ***arguments*** to ***id***
* save ***id*** as ***filename***
