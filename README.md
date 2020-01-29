## Installation Instruction

HIPHOP is built with Python3, along with multiple modules. To install these, perform the following steps:

1. Install Python3 via https://www.python.org/downloads/
2. After Python3 has been installed
	1. Install OpenCV with ```pip3 install opencv-python```
	2. Install Termcolor with ```pip3 install termcolor```
	3. Install Colorama with ```pip3 install colorama```
	4. Install numpy with ```pip3 install numpy```
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
<HHE> ::= open <filename> as <id>
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
* reload ***id***
	* this command would re-open a file at the path related to ***id***
	* ***id*** does not have to be in quotes
	* ex. to undo changes applied to an image
	  ```
	  reload test-img
	  ```
* save ***id*** as ***filename***
	* this command would save ***id*** from the program at ***filename***
	* ***filename*** has to be in double quote
	* folder specified in ***filename*** will be created if it doesn't already exist
	* ex. to save test-img at a new folder output in testing as result.jpg
	  ```
	  save test-img as "testing/output/result.jpg"
	  ```
* save ***id*** as "genfilename" ***type***
	* where ***type*** is an acceptable image file type (jpg/jpeg, png, bmp, tiff)
	* this command would save ***id*** from the program with a name generated from the current timestamp
	* file is saved to the current working directory saved in environment variable `wd`
	* command must include double quotes arround ***genfilename***
	  ```
	  save test-img as "genfilename" jpg
	  ```
* apply ***func*** to ***id***
	* this command would apply specified ***func*** to given ***id***
	* see the next section for available functions
	* ex. to blur the test-img opened earlier
	  ```
	  apply blur 10 to test-img
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
* set ***variable*** ***value***
	* this command allows setting of environment variables
	* ***value*** must be in double quotes
	* reserved environment variables: `wd` as working directory, `all` as all variables
	  ```
	  set wd "testing/images/"
	  open "test-img.jpg" as test
	  ```
* get ***variable***
	* this command retrieves environment variables associated with ***variable***
	* ***variable*** does ***NOT*** need to be in double quotes
	  ```
	  get wd
	  get all
	  ```

## Functions In HIPHOP

Function Name  | Number of Arguments | Argument Names | What The Function Does | Example Usage
------------- | ------------- | ------------- | ------------- | -------------
blur | 1 | scale | Blurs the image by averaging the image with a kernel of scale*scale size | ```blur 10``` 
grayscale | 0 | n/a | Turns the image into black and white | ```grayscale```
erode | 1 | scale | Erodes the image with a kernel of scale*scale size with full of ones | ```erode 3```
dilate | 1 | scale | Dilates the image with a kernel of scale*scale size with full of ones | ```dilate 3```
outline | 1 | scale | Removes the noise in image by eroding and dilating the image with a kernel of scale*scale size with full of ones | ```outline 5```
filtercolor | 6 | lowR, lowG, lowB, highR, highG, highB | Filters the image so only color between [lowB, lowG, lowR] and [highB, highG, highR] returns and turns rest of image black | ```filtercolor 50 50 110 255 255 130```
scale | 2 | x, y | Scales the image to x\*original width and y\*original height | ```scale 0.5 0.3```
impose | 3 | overlayImage, px, py | Overlays an opened image over another opened image at the specified pixel value of the background image. The overlay images top left corner will end up at that coordinate.| ```impose imageId 15 25```
crop | 4 | widthlow, widthhigh, heightlow, heighthigh | Crops the image with specified range, where the range of image is [-1, 1] for width and height with 0 at center<br>Applying example on the right on an image with width 200 and height 100 would return a new image with pixels width ranged [50, 150] and height ranged [25, 75] of original image | ```crop -0.5 0.5 -0.5 0.5```
wave | 2 | direction, amplitude | Applies a sine wave to the image vertically (v), horizontallity (h), or multidirectionally (m). | ```wave h 35```
