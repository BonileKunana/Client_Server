#Tsatsawani Mnisi
#23-02-2023
#Assignment 1

import socket
""" This program is a sserver code program that communicates with a server to allow a user to either upload,
   download, or view a list of available files on a directory. The client communicates with the server buy
   sending back messages"""

#data field
IP = socket.gethostbyname(socket.gethostname())
Port = 12382


#main method
def main():
   

    #Create clientside socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
    #Connect client to server
    client.connect((IP, Port))
    
    
    #Prompt user for request
    request = input("[U] Upload\n[R] Download \n[D] List files\nSelect request:\n")

    """ The if statements are created to allow the different execution of statements based on what the users request is. """
    if request == "U":
        client.send(request.encode("utf-8"))
        """ The program prompts user for filename , and then reads the file."""
        filename= input("Enter filename: ")
        file = o