# Edinburgh bus tracker - ncurses display example
# (curses is awful though, so the formatting sucks)
# (c) Mark Pentler 2017

from edinbustrack import *
from curses import wrapper
import time

stop_id = "36232626"
stop_name = get_stop_name(stop_id)

def main(stdscr):
	services = get_bus_times(stop_id)
	stdscr.clear()

	stdscr.addstr(0, 0, "Next departures from " + stop_name + " - CTRL-C to exit")
	stdscr.addstr(1, 0, "---------------------")
	stdscr.addstr(2, 0, "| Service |   Mins  |")
	stdscr.addstr(3, 0, "---------------------")

        for id, service, mins in services: # iterate through the list
		stdscr.addstr(id+4, 0, "|" + service + "         " + mins)

	stdscr.refresh()
	time.sleep(30)

while True:
	wrapper(main)
