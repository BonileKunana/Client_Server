"""
Auther: Bonile Kunana
Date: 2/03/2023
"""

"""import socket libraty"""
import socket
import os
from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog
import json


"""create an identifier"""
IP = socket.gethostbyname(socket.gethostname())
Port = 33333
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
        tempArr = root.filename.split("/")
        selectedFile =  tempArr[len(tempArr)-1]
        """gui end"""
        client.send(query.encode(FORMAT))
        """Access file and read data"""
        
        file = open(selectedFile, "r")
        
        data = file.read()
        """send file name to the server"""
        client.send(selectedFile.encode())
        """recieve message from the server and print it"""
        msg = client.recv(size).decode(FORMAT)
        print(f"[SERVER]: {msg}")
        """send file data to the server"""
        client.send(data.encode(FORMAT))
        """recieve message from the server"""
        msg = client.recv(size).decode(FORMAT)
        print(f"[SERVER]: {msg}")
    elif query =="D":
        client.send(query.encode(FORMAT))
        
        userFile = input("Enter file name:")
        client.send(userFile.encode())
        #path = "/FileStorage"
        
        """recieve the file name"""
        print("[Client] Preparing to download. Please wait...")
        #newFileName = client.recv(size).decode(FORMAT)
        client.send(b"OK")
    
        """open file """
        file = open("downloaded/"+userFile, "w")
        """recieve file data from server"""
        newData = client.recv(size).decode(FORMAT)
        """write data into a file"""
        file.write(newData)
        print("[Client] File downloaded.")
        print("[Client] Please find the file in 'downloaded' folder")
    elif query == "L":
        """This the option of listing files that are in a folder"""

        """Send the helping variable to the server so that it knows what to do"""
        client.send(query.encode())
        """Recieve list of file names from the server"""
        arr = client.recv(size)
        """Decode the data in the list"""
        arr = json.loads(arr.decode())
        myArr = arr.get("a")
        var = arr.get("b")
        """Print the number of files and list them"""
        print("There are ",len(myArr)," files in the folder:")
        for i in myArr:
            print(i)
        
    else:
        "”” terminated the connection."""
        print ("Invalid request, connection closed")

if __name__ == "__main__":
    main()
