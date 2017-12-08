# edinbustrack V0.02 - get all of the upcoming services at a particular stop
# (c) Mark Pentler 2017
#
# This uses screen scraping as you appear to have to be a proper developer to
# get access to the Edinburgh City Council's BusTracker API
#
# Important: This doesn't work right now and is loaded with test data. In a
# future release I'll try and fix the scraping or I guess I'll have to find 
# out how we get access to the API

from bs4 import BeautifulSoup
import requests

def get_bus_times(stop_id): # returns a list of expected buses at the chosen stop
	url = "http://www.mybustracker.co.uk/?module=mobile&mode=1&busStopCode=" + stop_id + "&subBusStop=Display+Departures"
	r  = requests.get(url) # make our request
	data = r.text
	soup = BeautifulSoup(data, "html.parser") # bs4 doing its work
	stop_data = soup.find_all("tr", attrs={'style': None, 'class': None}) # grab every single bus entry in the table - this ID changes!
	print stop_data
	services = [] # service list goes in here
#	services = [(0,"1","5"),(1,"1","14"),(2,"3","4"),(3,"3","9"),(4,"33","12"),(5,"33","24"),(6,"x","xx"),(7,"x","xx"),(8,"x","x"),(9,"xx","xx"),(10,"N25","00:24"),(11,"N25","00:54")] # some test data

        for row_num, row in enumerate(stop_data):
                cols = row.find_all("td") # this will grab every column per bus
                services.append ([row_num, cols[0].get_text(strip=True).encode("ascii"), cols[2].get_text(strip=True).encode("ascii")]) # extract service and time remaining
        return services
