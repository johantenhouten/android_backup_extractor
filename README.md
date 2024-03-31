# android_backup_extractor
A python script to convert a Android backup to to a TAR file.

I tried som of the JAR files out there and they did not work. But the AndroidBackup (abd backup output) file seems straightforward.


The first 24 bytes contain a header, the rest if the file is compressed with ZLIB. I did not find a commandline tool to decompress ZLIB.

So I wrote a small Python script that reads the file, cheks the header, runs the ZLIB extraction and writes the data to a tar file with the same name.

I like GUI's so I used PySimpleGUI

Requirements:
  ZLIB
  PySimpleGUI


Use:
  python3 extract.py

  The application will open a dialog, choose our AB file and press Convert File

  ![alt text](http://url/to/img.png)
  
  
