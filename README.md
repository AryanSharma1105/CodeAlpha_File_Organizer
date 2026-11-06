# 📁 File Organizer in Python

Hi, I'm Aryan Sharma 👋

This is a small Python script that moves all the `.jpg` images from one folder into another. I made it after realising how messy my folders get when photos and other files are all mixed together. It's a simple script, but it saves a lot of manual dragging and dropping.

## What it does

- Looks inside a **source folder**
- Finds every file that ends with `.jpg` (capital letters like `.JPG` work too)
- Moves those files into a **destination folder**
- Creates the destination folder automatically if it doesn't exist yet
- Prints a message for every file it moves, so you can see what's happening

Files that aren't JPGs are left exactly where they are.

## How to run it

1. Make sure Python 3 is installed. You don't need to install anything extra, because the script only uses built-in modules (`os` and `shutil`).
2. Clone this repo or download the file:
   ```
   git clone <your-repo-link-here>
   ```
3. Create a folder named `source_folder` next to the script and put some `.jpg` files in it.
4. Run the script:
   ```
   python file_organizer.py
   ```
5. Check `destination_folder`, and your images will be there.

Want to use different folders? Just change these two lines at the top of the script:

```python
source_folder = "source_folder"
destination_folder = "destination_folder"
```

## Example output

```
photo1.jpg moved successfully!
holiday.JPG moved successfully!
selfie.jpg moved successfully!
All JPG files have been moved.
```

## What I practiced

- Working with files and folders using the `os` module
- Checking if a folder exists and creating it with `os.makedirs()`
- Listing folder contents with `os.listdir()`
- Looping through files and filtering them with `.endswith()`
- Using `.lower()` so the file extension check isn't case sensitive
- Building file paths properly with `os.path.join()`
- Moving files with `shutil.move()`

## Things to keep in mind

- This **moves** the files, it doesn't copy them. The originals won't stay in the source folder.
- Right now it only handles `.jpg`. Files ending in `.jpeg` or `.png` are ignored.
- The source folder has to exist, otherwise Python will show an error.
- If a file with the same name is already in the destination folder, it may cause an error or get replaced, depending on your system.

## Feedback

I'm still learning Python, so any suggestions are welcome. If you find a bug or have an idea to make this better, feel free to open an issue or send a pull request.

If you found it useful, a ⭐ on the repo would make my day. Thanks for stopping by!

Author:-
**Aryan Sharma**
GitHub: [@AryanSharma1105](https://github.com/AryanSharma1105)# CodeAlpha_File_Organizer
