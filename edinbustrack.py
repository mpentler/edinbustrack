# edinbustrack V0.05 - get all of the upcoming services at a particular stop
# (c) Mark Pentler 2017
#
# This uses screen scraping as you appear to have to be a proper developer to
# get access to the Edinburgh City Council's BusTracker API

from bs4 import BeautifulSoup
import requests

def get_bus_times(stop_id): # returns a list of expected buses at the chosen stop
	url = "http://www.mybustracker.co.uk/?module=mobile&mode=1&busStopCode=" + stop_id + "&subBusStop=Display+Departures"
	r  = requests.get(url) # make our request
	data = r.text
	soup = BeautifulSoup(data, "html.parser") # bs4 doing its work
	stop_data = soup.find_all("tr", attrs={"style": None, "class": None}) # grab every single bus entry in the table - this ID changes!
	services = [] # service list goes in here

        for row_num, row in enumerate(stop_data):
                cols = row.find_all("td") # this will grab every column per bus
                services.append ([row_num, cols[0].get_text(strip=True).encode("ascii"), cols[2].get_text(strip=True).encode("ascii")]) # extract service and time remaining
        return services

def get_stop_name(stop_id):
	url = "http://www.mybustracker.co.uk/?module=mobile&mode=1&busStopCode=" + stop_id + "&subBusStop=Display+Departures"
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data, "html.parser")
	stop_name = soup.find("span", attrs={"id": "resultTitleText"}).get_text(strip=True).encode("ascii").split("Next departures from ") # specifically grab the stop name here from the top of the timetable
	return stop_name[1]
