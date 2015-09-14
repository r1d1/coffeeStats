#!/usr/bin/python

# Client/server python
# and mostly from http://www.binarytides.com/code-chat-application-server-client-sockets-python/
# and http://www.binarytides.com/python-socket-programming-tutorial/

import socket               # Import socket module
import sys
from thread import *
import numpy as np
# ====================================================================================
#Function for handling connections. This will be used to create threads
def clientThread(conn, prodData):
	#Sending message to connected client
	conn.send('\033[36mWelcome to the Coffee server.\033[39m\n\nType /help to get a list of available commands\n\n>')
	#infinite loop so that function do not terminate and thread do not end.
	while True:
		#Receiving from client
		data = conn.recv(1024)
		if not data: 
			break
		
		command=data.split()
		print command
		#reply = "OK... "
		reply = "OK... "

		if command[0] == "/quit":
			reply = "Disconnecting"
			reply = reply + "\n"
			conn.sendall(reply)
			break
		elif command[0] == "/help":
			print "/help"
			reply= "/help : display this help message\n/quit : disconnect and exit program"
		elif command[0] == "/add":
			print len(command)
			reply="Adding recipe !"
		elif command[0] == "/add":
			print "adding recipe :", command[1], command[2]
	#		# If changed till there
	#		if (command[1] in prod):
	#			try:
	#				productNumber=int(command[2])
	#			except IndexError, ValueError:
	#				print "Quantity is Not a number, try again !"
	#			productIndex=prod.index(command[1])
	#			totalPrice = productNumber * price[productIndex]
	#			print productIndex, totalPrice
	#			if totalPrice <= myMoney:
	#				myMoney = myMoney - totalPrice 
	#				myProducts[productIndex] = myProducts[productIndex] + productNumber
	#				stocks[productIndex] = stocks[productIndex] - productNumber
	#				reply = "Transaction done !"
	#			else:
	#				reply= "Not enough money !"
	#		else:
	#			reply = "Unknown product !"
	#			print reply 
	#	elif command[0] == "/sell":
	#		print "sell", data[6:]
	#	elif command[0] == "/product":
	#		# /product <name> <>
	#		print "product", command[1]
	#		try:
	#			productIndex=prod.index(command[1])
	#		except IndexError, ValueError:
	#			print "unknown product, try again !"
	#		reply = str(command[1]) + " remaining : " + str(stocks[productIndex]) + " at " + str(price[productIndex]) + " unit per element."
	#	elif command[0] == "/status":
	#		products=[str(yourp[0])+" "+str(yourp[1]) for yourp in zip(*[prod, myProducts])]
	#		status=str("Your account currently has " + str(myMoney) + " unit, you owe " + str(products))
	#		reply = reply + status
	#		print status
	#	else:
	#		pass
		reply = reply + "\n>"
		conn.sendall(reply)
	#came out of loop
	conn.close()
