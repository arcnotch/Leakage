import socket
import sys
import argparse
import hashlib
import binascii

def CheckSign(sign):
    hasher = hashlib.sha224()
    with open(args["output"], 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
        if (sign == hasher.hexdigest()):
            print('Signatures are match! The file has been leaked!') 
            return True
        print('File signature is not match to the original signature')
        print('Original is: ',sign)
        print('Recieved is :',hasher.hexdigest())
        return False

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
parser = argparse.ArgumentParser(description='Decode the leakage file')
parser.add_argument("-I","--input",help="Leaked file path", required=True)
parser.add_argument("-O","--output",help="Output file path after decode", required=True)
args = vars(parser.parse_args())

FixedWindow = 63
with open(args["input"], 'r') as my_file:
    hexed = my_file.read().splitlines()
    verify = 0
    length = hexed[0].split('.')[0]
    sign = hexed[1].split('.')[0]
    #print(sign)
    licked = ''
    for line in hexed[2:]:
        dataPeice = line.split('.')[0]
        licked += dataPeice
        verify += len(dataPeice)
    print(licked)
if (verify == int(length)):
    File = binascii.unhexlify(licked)
    f = open(args["output"],"wb")
    f.write(File)
else:
    print('File is corrupted: file size is not match to the original')
f.close()
CheckSign(sign)

