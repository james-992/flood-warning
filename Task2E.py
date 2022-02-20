"""
displays a plot of the water level data against time for a station, 
and includes on the plot lines for the typical low and high levels.
"""

from floodsystem.datafetcher import *
from datetime import datetime, timedelta
import matplotlib.dates
import matplotlib.pyplot as plt
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list


#this is code to build the dates levles data for the function to use

#input the number of days of data you want to show
dt = 2

# Station name to find
station_name = "Cam"


# Build list of stations
stations = build_station_list()

# Find station
station_of_interest = None
dates, levels = (fetch_measure_levels(station_of_interest.measure_id,
                                     dt=datetime.timedelta(days=dt)))


for station in stations:
if station.name == station_name:
    station_of_interest = station
    break

if not station_of_interest:
    raise ValueError("Station {} could not be found".format(station_name))

    
#everything below here is the actual function


def plot_water_levels(station, dates, levels):

    # sets up the plot
    
    t = matplotlib.dates.date2num(dates)
    plt.plot_date(t, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
    
    

plot_water_levels(station_of_interest, dates, levels)


                                    