# File-Sorting
This repository is a simple program that helps to organize a user's files.

Given a path provided by the user, the program will sort all files of the same type under their corresponding folder types.
For example, if that path provided contains the following files:
```
/path/to/organize/files/
    app.py
    instructions.pdf
    list.txt
    important.pdf
```

The program will reorganize the structure as follows:
```
/path/to/organize/files/
    py/
        app.py

    pdf/
        instructions.pdf
        important.pdf

    txt/
        list.txt
```

# Running
Once the repository is cloned, give the file executable permissions by running `chmod +x file_sorting.py`.

To execute, run the program as follows:
* `./file_sorting.py -p /path/to/organize/files`

Once complete, the files should be organized into the proper folders.
