"""import Socket library"""
from socket import *
import os
import json

"""create an identifier"""
IP = "sl-dual-287"
Port = 33333
"""helping variables"""
FORMAT = "utf-8"
SIZE = 1024

"""start main"""


def main():
    print("[STARTING] Server is starting.")
    """create a server socket and bind it to the port"""
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(("", Port))
    print(f"[BINDING] Server Socket has been bind to {Port} .")

    server.listen(1)
    print("[LISTENING] Server socket is listening.")


    """loop forever"""
    while True:
        """create connectionSocket"""
        con, address = server.accept()

        print(f"[NEW CONNECTION] {address} connected.")

        helper = con.recv(SIZE).decode(FORMAT) # decode the users request
        if helper == "U":
            """receive file name from client"""
            filename = con.recv(SIZE).decode(FORMAT)
            print(f"[RECV]:  Receiving the filename.")  # print out the progress of the program and communication


            """direct the file to file storage directory"""
            path = os.path.dirname(os.path.realpath(__file__))
            des_Dir = os.path.join(path, "FileStorage")

            print("file name received")
            """open file and send message back to client"""
            file = open(os.path.join(des_Dir, filename), "w")
            con.send("[SERVER] Filename Received".encode(FORMAT))
            """receive file data from client"""
            data = con.recv(SIZE).decode()
            print(f"[RECV] Receiving the file data.")
            """write to file"""
            file.write(data)

            """send message back to the client"""
            con.send("[SERVER] File data received".encode(FORMAT))
            """close the file and socket"""

            print(f"[DISCONNECTED] {address} disconnected.")
            file.close()
            con.close()
        elif helper == "D":
            """Access file and read data"""
            userFile = con.recv(SIZE).decode()
            
            file = open("FileStorage/"+userFile, "r")
            data = file.read()
            """send file name to the server"""
            #con.send("File.txt".encode(FORMAT))
            #con.recv(1024)
            """send file data to the server"""
            con.send(data.encode(FORMAT))
            print("[Done]: Done sending")
            print(f"[DISCONNECTED] {address} disconnected.")
            file.close()
            con.close()
        elif helper == "L":
            print("[SERVER] is listing")
            entries = os.listdir('FileStorage/')
            arr = []
            for item in entries:
                arr.append(item)
            var = 1
            myData = json.dumps({"a": arr, "b": var})
            con.send(myData.encode())
            con.close()
            print(f"[DISCONNECTED] {address} disconnected.")


if __name__ == "__main__":
    main()
