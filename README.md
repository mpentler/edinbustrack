# edinbustrack V0.0.2
A python library to display live Edinburgh bus times for an individual stop

Code is (C) Mark Pentler 2017

## Install

Obviously you need python for this, but you also need Beautiful Soup 4 for the screen scraping. You can grab that from here:
https://www.crummy.com/software/BeautifulSoup/

Then just `import from edinbustrack *` to load it into your project.

## Usage

There are three examples included:
* A simple shell-outputted table with appalling formatting that I never finished tidying up
* A curses-based example, again with awful formatting
* A more polished PyGame-based example that could be adapted for many applications or displays - this is broken right now (see the issues list for details)

There is a single function called get_bus_times() that will retrieve the data. The function requires a single integer parameter to be passed. This is the ID of the bus stop you require. You can retrieve this from the Edinburgh bus tracker website:
http://www.mybustracker.co.uk

You can also get them from the bus stop signs on the street.

This function will return a list of lists with each list containing: id (int), service (string), mins (string)
* id is just a row entry ID in case you need to make formatting decisions based on specific rows of data
* service is a service number (the one on the front of the bus...)
* mins is either the time remaining in minutes, the word DUE if he time remaining is less than a minute, or a future moment in time in 24-hour format (usually for night buses that haven't started running yet)

## Disclaimer

It goes without saying that this could:

* Break at any time - I'll try and keep on top of any changes to the MyBusTracker website that stop it working. The devs are randomising the table cell ID names to stop scraping, so the library needs a chunk of code adding to check this first and change its queries accordingly
* Disappear at any time - This is a project unassociated with the City of Edinburgh Council or any of the bus services that operate on its routes. Hopefully they're cool with it. It's a hobby project that doesn't detract from their other services. Maybe we can use the API someday...
