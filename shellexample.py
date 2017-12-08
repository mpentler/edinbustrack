# Edinburgh bus tracker - simple example output to a shell
# (c) Mark Pentler 2017

from edinbustrack import *
import os
from time import sleep

# setup our variables first. stop id and url are definable in case they change them
stop_id = "36232626" # grabbed from the mybustracker website

while True:
	services = get_bus_times(stop_id) # update our service list
	os.system("clear")

	print "Edinburgh Bus Tracker for bus stop " + stop_id + " - CTRL-C to exit"
        print "---------------------"
	print "Service\t\tMins"
	print "---------------------"

	for id, service, mins in services: # iterate through the list
		print service + "\t\t" + mins

	sleep(30) # wait before updating again
