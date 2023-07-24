"""import socket libraty"""
import socket
import os
from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog
import json


"""create an identifier"""
IP = socket.gethostbyname(socket.gethostname())
Port = 12379
"""helping variables"""
FORMAT = "utf-8"
size = 1024
count = "n"

"""start of main function"""
def main():
    
    """create TCP socket connect it to remote host"""
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    client.connect((IP,Port))
    """prompt the user"""
    
    query = input("Press U[for upload], press D[for download] and press L[for listing]:")
    if query == "U":
        """gui start"""
        root = Tk()
        root.title("File sharing App")
        root.filename = filedialog.askopenfilename(initialdir="/Assignment/downloaded", title="File sharing App", filetypes=(("all files","*.*"), ("pdf files","*.pdf")))
        root.mainloop()
        """this part will get the name of the selected file from the gui"""
        tempArr = root.filena