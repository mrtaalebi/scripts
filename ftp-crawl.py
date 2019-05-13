#!/bin/python3

import ftplib
import sys

link = sys.argv[1]

ftp = ftplib.FTP(link)
ftp.login()

methods = [method for method in dir(ftp) if callable(getattr(ftp, method))]
print(methods)

def recur(ftp):
    print(ftp.pwd())
    ftp.nlst()
    curr_dir = ftp.pwd()
    for x in ftp.nlst():
        ftp.cwd(x)
        recur(ftp)
        ftp.cwd(curr_dir)
        print(ftp.pwd())
recur(ftp)


