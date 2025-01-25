### New stuff Added👉 Speach to text , Code execution(Python Only) , clock widget , calculator , drawing pad , terminal and more ! 

## GTextEditor :
is a basic text editor with tabbed interface, customizable fonts, text styling options, and file handling capabilities. It provides a rich set of features such as font and color customization, find and replace, undo/redo, and more. This text editor is built using Python's Tkinter module for graphical user interface and is designed for simple and efficient text editing.

## Features
- Tabbed Interface: Create, close, and switch between multiple tabs for easy management of documents.

- Font Customization: Change font family, size, and color of text.

- Text Styling: Apply text styles such as bold, italic, underline, strike-through, Bullet Points and Number list, framing

- Text Alignment: Align text to the left, center, or right.

- Find & Replace: Perform find and replace operations on the content of the current tab.

- File Operations: Save text to a file, load text from a file, and clear the text area.

- Undo/Redo: Support for undo and redo actions to manage text changes.

- Background Color: Customize the background color of the editor area.

- Spell Check: You can check all the texts for mis spelled words and if it finds one , just right click and it will bring up options to choose from 

## Speach to text : Use prebuilt in commands :
Bold - Applies bold formatting to the selected text.

Italic - Toggles italic formatting for the selected text (assumes _toggle_italic method implementation).

Load File - Opens a file dialog to load a text file into the text area.

Underline - Toggles underline formatting for the selected text (assumes _toggle_underline method implementation).

Strike - Toggles strikethrough formatting for the selected text (assumes _toggle_strike method implementation).

Highlight <keyword> - Highlights all occurrences of the specified keyword in the text area.

Clear Highlight - Removes all existing highlights from the text area.

Align Left - Aligns text to the left (assumes _align_left method implementation).

Align Center - Aligns text to the center (assumes _align_center method implementation).

Align Right - Aligns text to the right (assumes _align_right method implementation).

Insert Text - If no specific command is recognized, the spoken text is inserted as plain text into the text area.

## Code Execution 
just type out your code and click run (only works with Python) and nott terminal base games 

## Terminal Widget 
you should be able to use all basic windwo command like 
- dir
- time /t
- date /t
and so on

if u want to customize backgroun and texk of termnial juts use these commands 
- set bgcolor blue
- set fgcolor red

list of colors for terminal:
- red
- blue
- green
- cyan
- yellow
- white
- lime
  and more 


### Keybindings

| Key Combination     | Action                             |
|---------------------|------------------------------------|
| **Ctrl + N**        | Open a new tab                   |
| **Ctrl + S**        | Save as text                     |
| **Ctrl + O**        | Load text                        |
| **Ctrl + Q**        | Quit application                 |
| **Ctrl + Z**        | Undo last action                 |
| **Ctrl + Y**        | Redo last undone action          |
| **Ctrl + F**        | Find and replace text            |
| **Ctrl + B**        | Toggle bold formatting           |
| **Ctrl + I**        | Toggle italic formatting         |
| **Ctrl + U**        | Toggle underline formatting      |
| **Ctrl + L**        | Align text to the left           |
| **Ctrl + E**        | Center-align text                |
| **Ctrl + R**        | Align text to the right          |


## Menu \ ToolBar Options:
File: New Tab, Close Tab, Save, Load, Clear, Exit.

Edit: Undo, Redo, Find and Replace, Bold, Italic, Underline, Strike, Align (Left, Center, Right).

Help: About the application.

Text Customization: You can change the text font, size, and color using the toolbar buttons. Additionally, you can update the background color.

Save and Load: You can save the current text to a file and load text from a file into the active tab.

Spell Check: You can check all the texts for mis spleed words and if it finds and just right click and it will bring up options to choose from 

inset Date & time: This will add the current date and time to your tab in text fromat 

Bullet Points \ Number List: Highlght and click One of them add the list format 

Font Size: You can ajust and choose the size of the font 

Font Picker: choose a font style you like 

## Requirements
- Python 3.x
- tkinter (included with Python standard library)
- tkinter.ttk for advanced widgets
- tkinter.colorchooser for color picking
- pip install pyspellchecker (for the spell checking)

## Tested And Made With: 

- Python
- Windows
 
i have not tested on mac or linux.
If it dosent work , thats my bad but i have no plans to test it on them right now,
feel free to test and edit what every you ned to make it work on your OS.


## Usage

Creating the Editor: The GTextEditor class can be initialized with the following optional parameters:

- x, y: Coordinates for the editor window (default: 0, 0). this realy dosnt matter because u cant change cords 

- wd, ht: Width and height of the window (default: 600, 400). same with this they kinda just there and dont do anything 

- default_font: Default font tuple, e.g., ("Arial", 12) (default: "Arial", 12).

- bg, fg: Background and foreground color for the text editor (default: white for background, black for foreground). 


## import 
![Screenshot 2025-01-20 194505](https://github.com/user-attachments/assets/3c13cd0c-828a-4dae-af24-914420244a84)

You can Apply my Custom style, all u need to do is add the root like this ![Screenshot 2025-01-21 191602](https://github.com/user-attachments/assets/8f963b1c-6550-487f-8335-a173bf266a9d)

## Full Example code of Adding widget to tkinter window: 
![Screenshot 2025-01-23 002032](https://github.com/user-attachments/assets/9a89834a-ec1e-4528-b051-4fc848b8cd76)


## Example.py is the file you can use to run the code or make your own file to run the widget 

# License 
This is open-source and can be used and modified freely







