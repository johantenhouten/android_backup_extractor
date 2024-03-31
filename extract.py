# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 22:46:41 2024

@author: Johan
"""


import zlib
import sys
import pathlib
import PySimpleGUI as sg
import os


inputfile = 'C:/Users/Johan/OneDrive - Hogeschool Leiden/Documenten/scripts/backup-extractor/pixel7.ab'




def ab_to_tar(full_filename):
    
    stem = pathlib.Path(selected_filename).stem
    parent =  pathlib.Path(selected_filename).parent
    tarfile = pathlib.Path(parent , stem + '.tar')
    
    
    if not pathlib.Path(full_filename).is_file():
        print("File not found")
        print("Extraction aborted.")
        return
    else:
        try:
            file = open(full_filename, "rb")
            header = file.read(24)
            if header != b'ANDROID BACKUP\n5\n1\nnone\n':
                file.close()
                print("Header is not ANDROID BACKUP 5.1.")
                print("Extraction aborted.")
                return
            rest = file.read()
            file.close()

            print(len(rest))
            tar = zlib.decompress(rest)
            
        except:
            print("Problem with reading the file")
            print("Extraction aborted.")
            if file: file.close()
            return
    # tar should exist and is a tar file
    # just write it
    
    try:
        file = open(tarfile , "wb")
        file.write(tar)
        file.close()
    except:
        print("Problem with writing the tar file")
        print("Extraction aborted.")
        if file: file.close()
        return
    print("Tar file created")
    

            


def get_filename():
    sg.theme("DarkTeal2")
    layout = [
		[sg.T("Read AB file and create a TAR file")], 
		[sg.Text("Choose a Android Backuop file: "), sg.Input(), sg.FileBrowse(key="-IN-", file_types=(("*.ab", "*.ab"),))],
		[sg.Button("Convert file"), sg.Button("Cancel")], 
		]


    window = sg.Window('Android Backup Extractor', layout, size=(600,150))
    
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event=="Exit" or event == "Cancel":
            window.close()
            return None

        elif event == "Convert file":
            window.close()
            return values['-IN-']
        


selected_filename= get_filename()
ab_to_tar(selected_filename)
