## android_backup_extractor
A python script to convert a Android backup to to a TAR file. At this moment the tool does not support password encrypted backups.

I tried some of the JAR files out there and they did not work. But the AndroidBackup (abd backup output) file seems straightforward.


The first 24 bytes contain a header, the rest if the file is compressed with ZLIB. I did not find a commandline tool to decompress ZLIB.

So I wrote a small Python script that reads the file, cheks the header, runs the ZLIB extraction and writes the data to a tar file with the same name.

I like GUI's so I used PySimpleGUI

# Requirements:
  - ZLIB (not evensure if it is part of standard Python3)
  - PySimpleGUI


# Use:
  python3 extract.py

  The application will open a dialog, choose our AB file and press Convert File

  ![image of dialog](https://github.com/johantenhouten/android_backup_extractor/blob/main/picture.jpg)
  
# Tested
I tested it on Windows 11, with Python 3.11 and a AB file I created with "adb backup -all"
