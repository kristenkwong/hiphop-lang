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

## Commands Provided By HIPHOP

* open ***filename*** as ***id***
	* this command would open file specified at ***filename*** as ***id***
	* ***filename*** has to be in double quote
	* ex. to open a file in the testing/images folder and save as test-img to use in program
	  ```
	  open "testing/images/test-color.jpg" as test-img
	  ```
* save ***id*** as ***filename***
	* this command would save ***id*** from the program at ***filename***
	* ***filename*** has to be in double quote
	* folder specified in ***filename*** will be created if it doesn't already exist
	* ex. to save test-img at a new folder output in testing as result.jpg
	  ```
	  save test-img as "testing/output/result.jpg"
	  ```
* apply ***func*** to ***id***
	* this command would apply specified ***func*** to given ***id***
	* see the next section for available functions
	* ex. to apply grayscale to test-img opened earlier
	  ```
	  apply grayscale to test-img
	  ```
* apply-all ***funcs*** to ***id***
	* this command would apply all ***funcs*** specified to given ***id***
	* ***funcs*** have to be a comma separated list of functions
	* ex. to apply grayscale and then blur test-img opened earlier
	  ```
	  apply-all [grayscale, blur 10] to test-img
	  ``` 
* save-macro ***funcs*** as ***id***
	* this command allows saving all ***funcs*** as a new ***id***
	* ***funcs*** have to be a comma separated list of functions
	* ex. to repeat apply blur and then grayscale on multiple images
	  ```
	  save-macro [blur 10, grayscale] to blurscale
	  apply blurscale to img1
	  apply blurscale to img2
	  ```

## Functions In HIPHOP

Function Name  | Number of Arguments | Argument Names | What The Function Does
------------- | ------------- | ------------- | -------------
blur | 0 | n/a | Blurs the image
grayscale | 0 | n/a | Turns the image into black and white
erode | 1 | TODO | TODO
dilate | 1 | TODO | TODO
outline | 1 | TODO | TODO
filtercolor | 6 | lowR, lowG, lowB, highR, highG, highB | Filters the image so only color between [lowB, lowG, lowR] and [highB, highG, highR] returns and turns rest of image black
scale | 2 | TODO | TODO
crop | 4 | widthlow, widthhigh, heightlow, heighthigh | Crop id with specified range, where the range of image is [-1, 1] for width and height with 0 at center<br>For example, a image with width 200 and height 100<br>widthlow = -0.5 widthhigh = 0.5 heightlow = -0.5 heighthigh = 0.5<br>would return a new image with pixels ranged [50, 150] for width and [25, 75] for height