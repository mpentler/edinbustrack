# edinbustrack V0.01
A python library to display live Edinburgh bus times for an individual stop

Code is (C) Mark Pentler 2017

## Install

Obviously you need python for this, but you also need Beautiful Soup 4 for the screen scraping. You can grab that from here:
https://www.crummy.com/software/BeautifulSoup/

## Usage

There are two examples included - a simple shell output and one using ncurses. There is a single function called get_bus_times() that will retrieve the data.

The function requires a single integer parameter to be passed. This is the ID of the bus stop you require. You can retrieve this from the Edinburgh bus tracker website:
http://www.mybustracker.co.uk

You can also get them from the bus stop signs on the street.

## Further adaptation

I'll try and work on a PyGame example soon as I want to eventually get this running on my TV on a Raspberry Pi. Could also send it to one of those LCD matrix displays. I wondered about a Kodi screensaver too?

## Disclaimer

It goes without saying that this could:

* Break at any time - I'll try and keep on top of any changes to the MyBusTracker website that stop it working.
* Disappear at any time - This is a project unassociated with the City of Edinburgh Council or any of the bus services that operate on its routes. Hopefully they're cool with it. It's a hobby project that doesn't detract from their other services. Maybe we can use the API someday...
