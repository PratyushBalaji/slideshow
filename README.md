# Slideshow Program Using OpenCV
This is a basic slideshow to cycle through and preview all image files in a certain directory

## **To Use**
1. Place the program in a folder containing PNG files.
2. Run the program.

**To Exit**:  
Quit the program from the terminal or editor. Pressing the 'X' button on the window **does not work**.

---

## **Functionality**
This is a slideshow program using OpenCV with the following features:

1. **Reads Files**:  
   Reads the names of all the files in the directory
2. **Filters PNG Files**:  
   Filters by png files
   Splits each file name into name and extension. If the extension is `'png'`, the program adds that file name to an array.  
   **(Note: Support for other image file types will be added.)**

3. **Displays Images**:  
   Displays the first image in the array using OpenCV's `imshow()`.

4. **Navigation**:  
   - Press **`d`** to go to the next image.
   - Press **`a`** to go to the previous image.  

   If at the first/last image and the user presses **`a`**/**`d`**, the program cycles to the end/start of the array.

5. **Feedback**:  
   Prints the letter pressed and the current image being displayed in the terminal (e.g., `"Image number 1, 2, 3, etc."`).

6. **Exit Program**:  
   Press **`Escape`** to kill the program by ending the loop.

---

## **Known Issues / Planned Changes**
1. **Key Registration Issue**:  
   Sometimes, keys need to be double-pressed to register. This might be due to a keyboard issue or `waitKey()` behavior.

2. **Performance**:  
   Images may appear laggy.

3. **Proper Exit Handling**:  
   Plan to use `sys.exit()` to ensure that pressing the 'X' button on the image window exits the program instead of creating a new instance of the slideshow.
