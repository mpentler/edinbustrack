# edinbustrack V0.05
A small python library to display live Edinburgh bus times for an individual stop

Code is (C) Mark Pentler 2017

## Install

Obviously you need python for this, but you also need Beautiful Soup 4 for the screen scraping. You can grab that from here:
https://www.crummy.com/software/BeautifulSoup/

Then just use 'import from edinbustrack *' to load it into your project.

## Usage

There are three examples included:
* A simple shell outputted table with appalling formatting that I never finished tidying up
* A curses-based example, again with awful formatting
* A more polished PyGame-based example that could be adapted for many applications or displays

There is are currently two functions implemented: 
### get_bus_times(stop_id)

Retrieves a new timetable update for a busstop. The function requires a single string parameter to be passed. This is the ID of the bus stop you require. You can retrieve this from bus stop signs on the street. Alternatively you can get it from from the Edinburgh bus tracker website:
http://www.mybustracker.co.uk

This function will return a list of lists with each list containing: id (integer), service (string), mins (string)
* id is just a row entry ID in case you need to make formatting decisions based on specific rows of data
* service is a service ID (the number on the front of the bus)
* mins is either the time remaining in minutes, the word DUE if the time remaining is less than a minute, or a future moment in time in 24-hour format (usually for night buses that haven't started running yet)

### get_stop_name(stop_id)

Retrieves the stop name for a bus stop. Again, the parameter is the string containing the required stop ID.

This function returns a single string containing the stop name.

## Disclaimer

It goes without saying that this could:

* Break at any time - I'll try and keep on top of any changes to the MyBusTracker website that stop it working. The devs are randomising the table cell ID names to stop scraping, so the library needs a chunk of code adding to check this first and change its queries accordingly. One day the whole cell layout changed completely.
* Disappear at any time - This is a project unassociated with the City of Edinburgh Council or any of the bus services that operate on its routes. Hopefully they're cool with it. It's a hobby project that doesn't detract from their other services. Maybe we can use the API someday...

## Changelog (from memory up to v0.0.5)

### Early December 2017:
v0.0.1 initial release as a standalone app
v0.0.2 converted to a library, shell and curses examples added
v0.0.3 added pygame example, but scraping is broken
v0.0.4 scraping fixed, fixed pygame display errors, and completed refactorisation of the code

### v0.0.5 - 9th Dec 2017
- added get_stop_name function and updated all included examples to demonstrate its use
- also tried to tidy up the curses example output but curses is a shitty library that doesn't even let you do tabbed data. it stays as is for now.
