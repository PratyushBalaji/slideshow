import cv2 as cv
import os

"""
TO USE : 
PLACE PROGRAM INTO A FOLDER CONTAINING PNG FILES
RUN PROGRAM

TO EXIT :
QUIT PROGRAM FROM TERMINAL / EDITOR, PRESSING THE 'x' ON THE WINDOWS DOES NOT WORK

Slideshow program using opencv

1) Reads the names of all the files in the directory using 'dir /b /a-d'
2) Splits each name into name and extension. If extension = 'png' it adds that name to a new array. 
WILL ADD SUPPORT FOR OTHER IMAGE FILE TYPES, VERY SIMPLE CHECK
3) Displays the first image in the array using 'imshow()'
4) If the user presses 'd', it goes to the next img. If the user presses 'a', it goes to the prev img.
5) If at the first / last img and the user wants to go back / forth, program cycles to the end / start
6) Prints the letter pressed and the current image being displayed ("Image number 1, 2, 3, 4, etc")
7) If the user presses 'Escape', it kills the program by ending the loop


KNOWN ISSUES / CHANGES TO BE MADE : 
1) Sometimes have to double press to get a key to register. Could be keyboard being weird again or 'waitkey()' issue
2) Laggy images
3) Use 'sys.exit()' so that when user presses cross on the image it kills program instead of creating a new instance of pic.
"""

directory = os.popen("dir /b /a-d").read()
directory = directory.split("\n")
images = []

for i in directory:
    print(i)
    try:
        if i.split('.')[1] == 'png':
            images.append(i)
    except:
        continue
print(images)
print(directory)
x = 0
c = 0
y = True
while y == True:
    try:
        cv.imshow(images[x].split('.')[0],cv.imread(images[x]))
    except IndexError:
        print("Reached the end of the array")
        x = c
    if cv.waitKey(100) == ord('d'):
        print("d")
        c = x
        if x < len(images)-1:
            x+=1
        else:
            x = 0
        print(f"This is photo number {x+1}")
        cv.destroyAllWindows()
    if cv.waitKey(100) == ord('a'):
        print("a")
        c = x
        if x > 0:
            x-=1
        else:
            x = len(images)-1
        print(f"This is photo number {x+1}")
        cv.destroyAllWindows()
    if cv.waitKey(100) == 27:
        print("Escape")
        y = False
cv.destroyAllWindows()
