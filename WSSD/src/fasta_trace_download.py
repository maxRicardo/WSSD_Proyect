#!/usr/bin/python2.7

# script to download from the 
# ftp server of the trace archive 
# database file by file

# # variables

from ftplib import FTP

def initialize(server, path):
    ftp = FTP(server)
    ftp.login()
    ftp.cwd(path)
    return ftp

def make_list(file_type, ftp):
    doc = open("list_of_packages.txt", "w")
    packages = []
    counter = 0
    print("Downloading list of packages...")
    for filename in ftp.nlst(file_type):
        doc.write(filename + "\n")
        counter += 1
        packages.append(filename)
        print(str(counter) + ") " + filename)

    return packages

def download(ftp, pack):
    print("Donwloading archive packages....")
    for each in pack:
        print("getting =>" + each)
        output = open(each, "wb")
        ftp.retrbinary("RETR " + each, output.write)
        output.close()
        print("downloading done!")

def main():
    File = raw_input("Enter Organism name to download: ")
    ftp = initialize("ftp-private.ncbi.nlm.nih.gov", "pub/TraceDB/" + File + "/")
    packtype = raw_input("\nEnter :\n1.Fasta \n2.Qual\n")

    if eval(packtype) == 1:
        pack = make_list("fasta.*", ftp)
        print ("You downloading : \n Files : "+File+"\nType: Fasta")
    if eval(packtype) == 2:
        pack = make_list("qual.*", ftp)
        print ("You downloading : \n Files : "+File+"\nType: Qual")

    if raw_input("\nStart Downloading....\n'y' or n\n") == "y":
        download(ftp, pack)

main()
    
        

    

    
        
    
    
        

