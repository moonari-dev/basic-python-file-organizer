# Basic file organizer made with python
## This tool organizes folders containing files of different extensions into organized folders.
e.g. "Images" folder containing .jpeg, .png, .gif files; "Documents" folder containing .pdf, .doc, .xlsx files; and so on...

WHAT IS INCLUDED?
There is:
"main.py" - a PYTHON file
"file_types.json" - a JSON file
"README" - README file(an instruction text file)

HOW TO USE IT?
In order to use this tool, run the script(python file), then a window will appear asking for the directory/path of the messy folder, select it and confirm. After this, your folder will be organized in four* folders inside of it:
"Images", "Documents", "Music" and "Others"

*However, the folders can be customized, you can make as much folders for extensions as you want. Check the json file in order to customize it. Also, if theres files that dont match any folder extensions, the "Others" folder will be created, collecting these files.

CUSTOMIZING 
To customize, you can edit the json file and change the NAME, EXTENSIONS and AMOUNT of folders.
This is the STANDARD CONFIGURATION of this tool:
```json
{
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"]
}
You can add new folders by repeating this structure
e.g.
```json
{
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Code": [".py", ".json", ".html"]
}
As you can see, the "Code" folder has been added into the json, so when organizing the folder will be created gathering files with these extensions.
It is also possible to edit the extensions of each folder
e.g.
```json
{
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Code": [".py", ".json", ".html", ".css", ".js", ".c"]
}
As you can see, three new extensions were added into "Code" folder(".css", ".js", ".c"), therefore when organizing the folder will also gather these new extension.

SAFETY
This script moves a file from one place to another, however it is not expected to delete anything.
I recommend testing this script in a safer folder before using it in your desired folder.

If something goes wrong, please let me know!
