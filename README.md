# GTextEditor

## GTextEditor :
is a basic text editor with tabbed interface, customizable fonts, text styling options, and file handling capabilities. It provides a rich set of features such as font and color customization, find and replace, undo/redo, and more. This text editor is built using Python's Tkinter module for graphical user interface and is designed for simple and efficient text editing.

## Features
- Tabbed Interface: Create, close, and switch between multiple tabs for easy management of documents.

- Font Customization: Change font family, size, and color of text.

- Text Styling: Apply text styles such as bold, italic, underline, and strike-through.

- Text Alignment: Align text to the left, center, or right.

- Find & Replace: Perform find and replace operations on the content of the current tab.

- File Operations: Save text to a file, load text from a file, and clear the text area.

- Undo/Redo: Support for undo and redo actions to manage text changes.

- Background Color: Customize the background color of the editor area.

And if you want you can highlight specifc Text or sentence and only change the hilghted text 


## Menu Options:
File: New Tab, Close Tab, Save, Load, Clear, Exit.

Edit: Undo, Redo, Find and Replace, Bold, Italic, Underline, Strike, Align (Left, Center, Right).

Help: About the application.

Text Customization: You can change the text font, size, and color using the toolbar buttons. Additionally, you can update the background color.

Save and Load: You can save the current text to a file and load text from a file into the active tab.


## Requirements
- Python 3.x
- tkinter (included with Python standard library)
- tkinter.ttk for advanced widgets
- tkinter.colorchooser for color picking

## Tested And Made With: 
- Python
- Windows 
i have not tested on mac or linux.
if it dosent work ,  thats my bad but i have no plans to test it on them right now.
feel free to test and edit what every you ned to make it work on your OS.

## Usage

Creating the Editor: The GTextEditor class can be initialized with the following optional parameters:

- x, y: Coordinates for the editor window (default: 0, 0). this realy dosnt matter because u cant change cords 

- wd, ht: Width and height of the window (default: 600, 400). same with this they kinda just there and dont do anything 

-default_font: Default font tuple, e.g., ("Arial", 12) (default: "Arial", 12).

-bg, fg: Background and foreground color for the text editor (default: white for background, black for foreground). 

 
## Adding to a tkinter window Example :
![textedit_init](https://github.com/user-attachments/assets/3feac7c9-9434-4e37-b3b7-2d36bd6cd942) 

## import 
![Screenshot 2025-01-20 194505](https://github.com/user-attachments/assets/3c13cd0c-828a-4dae-af24-914420244a84)

You can Apply my Custom style, all u need to do is add the root like this ![Screenshot 2025-01-21 191602](https://github.com/user-attachments/assets/8f963b1c-6550-487f-8335-a173bf266a9d)

full code make, sure to add the Custom Style import at the top : 
![Screenshot 2025-01-21 191756](https://github.com/user-attachments/assets/4dac34dc-3ea2-4414-be73-f14effc66cc6)

![Screenshot 2025-01-21 191819](https://github.com/user-attachments/assets/c3c475c1-2cd8-48f4-ae59-58fd68103e6a)


# main.py is the file you can use to run the code or make your own main file to run the widget 

# License 
This is open-source and can be used and modified freely







