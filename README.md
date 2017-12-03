# edinbustrack
A python script to display live Edinburgh bus times for an individual stop
(C) Mark Pentler 2017

## Install

Obviously you need python for this, but you also need Beautiful Soup 4 for the screen scraping. You can grab that from here:
https://www.crummy.com/software/BeautifulSoup/

## Usage

Edit the "edinbustrack.py" file in a text editor to change the stop_id variable to the ID of the bus stop you require. You can retrieve this from the Edinburgh bus tracker website:
http://www.mybustracker.co.uk

You can also get them from the bus stop signs on the street.

Running the script with "python edinbustrack.py" will output a constantly updating table display to the screen, clearing with an OS call to the "clear" command.

Obviously this is a rather limited output and you'll most probably be wanting to adapt the display for other usages...

## Adapting

You can see by the code that a single call to get_times returns a 2D list containing each service and the time remaining. A simple iteration of this list further down displays the data.

This means that you can pop this block of code into your own where required to populate variables, send output to an ncurses display, etc.

I plan to turn this project into a library and include the current code as an example, along with said ncurses example, and a more fancy pygame display. Clearly this could be very useful for Raspberry Pi or similarly-based systems.

## Disclaimer

It goes without saying that this could:

* Break at any time - I'll try and keep on top of any changes
* Disappear at any time - This is a project unassociated with the City of Edinburgh Council or any of the bus services that operate on its routes. Hopefully they're cool with it. It's a hobby project that doesn't detract from their other services. Unless we can use the API...
