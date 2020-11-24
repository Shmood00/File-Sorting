#!/usr/bin/python3.6

import argparse
import os

def get_files(path):
    return os.listdir(path)

def get_extensions(path, file):
    file_name, file_ex = os.path.splitext(path+file)

    return file_name,file_ex

def make_directories(path, extension):
    try:
        os.mkdir(path+extension[1:])
    except:
        pass

def move_files(path, file, extension):
    os.rename(path+file, path+extension[1:]+f"/{file}")

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--path", dest="path", help="Path of directory to clean up.")

    args = parser.parse_args()

    if args.path:
        path = args.path

        if path[-1] != "/":
            path = path+"/"

        files = get_files(path)
        
        for f in files:
            file_name, file_ex = get_extensions(path, f)

            if len(file_ex) >= 1:
                make_directories(path, file_ex)

                if file_ex in f:
                    move_files(path, f, file_ex)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()