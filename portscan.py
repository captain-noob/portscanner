#!/bin/python3

import socket  #importing sockets for scan
from datetime import datetime # date
import sys	#for Arguments
import os #for executing system cmds
import platform

ip=""
portlist=[]
time=datetime.now()
sy_stem=platform.system().lower()
pings=""


def banner():		#program banner
	print("-"*50)
	print("\t\tPort Scanner")
	print("\t Scans Through All TCP \"65,535\" Ports")
	print("\t  Time : "+str(datetime.now()))
	time=datetime.now()
	print("-"*50 +"\n")

def scanner():
	try:
		print ("[+] Open Ports")
		for port in range(1,65535):  		#looping port ranges

			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #connection socket
			socket.setdefaulttimeout(1) 	#timeout
			res=s.connect_ex((ip,port))  	#try connecting
			if res==0:		#connection True
				print("            Open     -->    {} /tcp".format(port))
				portlist.append(port)
			print("\rScanning Port :" + str(port) + "/tcp - Not Open", end="\r")
		print("\n")	
		print("-"*50)
		print("[*] Scan Completed....")
		print("[+] Total Number Of Open Ports Are : {}".format(len(portlist)))
		elapsedtime=datetime.now() - time
		print("[*] Elapsed Time : {}".format(elapsedtime))
		#sys.exit()
	except KeyboardInterrupt :  #when ctrl+C
		print ("[*] The Process Is Stoping.....")
		print ("[*] Exiting....")
		#sys.exit()
	except socket.error: 	#socket connection error
		print ("[*] Couldn't Connect to the Server .....")
		print ("[*] Exiting....")
		#sys.exit()




#main

if len(sys.argv)==2:	#checking for Arguments
	banner()
	ip=sys.argv[1]
	val=ip.split(".")
	if len(val)==4:		#validating ipv4

		if (int(val[0]) in range(1,255)) & (int(val[1]) in range(0,255)) & (int(val[2]) in range(0,255)) & (int(val[3]) in range(0,255)): #validating ipv4 range
			
			

			# getting system
			if (sy_stem=="windows"):
				pingz=" ping -n 1 "
				
			elif(sy_stem=="linux"):
				pingz=" ping -c 1 "
				
			pingz=pingz+ip	
			res=os.popen(pingz)	#executing ping
			resp=res.readlines()	#reading output
			resp=resp[1].split()	#split output [1]
			resp=resp[0]		#getting 1st string
			if resp == "64":
				print("[*] IPv4 :{}" .format(sys.argv[1]))
				print("[*] Scanning For Open Ports.....\n")
				print("-"*50)
				scanner()
			else:
				print("[*] Server Is Down.. \n")
				elapsedtime=datetime.now() - time
				print("[*] Elapsed Time : {}".format(elapsedtime))

		else:
			print("[*] Invalid Format of <ip>\n")
			print("[*] Try again With a valid Ip \n")
			#sys.exit()
	else:
		print(" Invalid Ip address \n")
		#sys.exit()
	
else:
	banner()
	print("[*] Usage : python3 portscan.py <ip> \n")
	#sys.exit()

	
	
