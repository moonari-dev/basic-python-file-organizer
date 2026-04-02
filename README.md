# Basic file organizer made with python
## This tool organizes folders containing files of different extensions into organized folders.
e.g. "Images" folder containing .jpeg, .png, .gif files; "Documents" folder containing .pdf, .doc, .xlsx files; and so on...

STRUCTURE
"main.py" - a PYTHON file
"file_types.json" - a JSON file
"README" - README file(an instruction text file)

USAGE
Run the script(python file), then a window will appear asking for the directory/path of the messy folder, select it. After that, your folder will be organized in four* folders inside of it:
"Images", "Documents", "Music" and "Others"

*However, the folders can be customized, you can make as much folders for extensions as you want. Check the json file in order to customize it. Also, if theres files that dont match any folder extensions, the "Others" folder will be created, collecting these files.

CUSTOMIZING 
You can customize the file organization by editing `file_types.json`.
e.g.
```json
{
  "Images": [".jpg", ".jpeg", ".png", ".gif"],
  "Documents": [".pdf", ".docx", ".txt"],
  "Music": [".mp3", ".wav"]
}

You can add new categories or modify extensions as needed.

SAFETY
This script moves a file from one place to another, however it is not expected to delete anything.
I recommend testing this script in a safer folder before using it in your desired folder.

If you encouter any issues, please report them.
