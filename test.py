from os import path
from ftplib import FTP


f = open("log.txt")
x = f.read()
ftp = FTP(x)
ftp.login()
ftp.retrlines('LIST')