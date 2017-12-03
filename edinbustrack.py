# Edinburgh bus tracker - get all of the upcoming services at a particular stop
# (c) Mark Pentler 2017
#
# This uses screen scraping as you appear to have to be a proper developer to
# get access to the Edinburgh City Council's BusTracker API

from bs4 import BeautifulSoup
import os
import requests
import time

# setup our variables first. stop id and url are definable in case they change them
stop_id = "36232626" # grabbed from the mybustracker website
url = "http://www.mybustracker.co.uk/?module=mobile&mode=1&busStopCode=" + stop_id + "&subBusStop=Display+Departures"

def get_times(): # returns a list of expected buses at the chosen stop
	r  = requests.get(url) # make our request
	data = r.text
	soup = BeautifulSoup(data, "html.parser") # bs4 doing its work
	stop_data = soup.find_all("tr", {"class": " srUtmLxK"}) # grab every single bus entry in the table
	services = [] # store our services in this list

	for row_num, row in enumerate(stop_data):
		cols = row.find_all("td") # this will grab every column per bus
		services.append ([row_num, cols[0].get_text(strip=True).encode("ascii"), cols[2].get_text(strip=True).encode("ascii")]) # extract service and time remaining
	return services 

while True:
	services = get_times() # update our service list
	os.system("clear")

	print "Service\t\tMins"
	print "---------------------"

	for id, service, mins in services: # iterate through the list
		print service + "\t\t" + mins

	time.sleep(30) # wait before updating again
