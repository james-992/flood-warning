""""
for task 2E
This sub module contains code for plotting data    
displays a plot of the water level data against time for a station, 
and includes on the plot lines for the typical low and high levels.
"""

from floodsystem.datafetcher import *
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
import matplotlib
import matplotlib.pyplot as plt


def plot_water_levels(station, dates, levels):

    # sets up the dates

    t = matplotlib.dates.date2num(dates)

    #checks to see if the requested station has consistant upper and lower bounds which can be plotted
    stations = build_station_list()
    inconsistent_stations, inconsistent_data = inconsistent_typical_range_stations(stations)
    if station in inconsistent_stations:
        print ("cannot show typical ranges as the data is inconsistant")
        pass
    else:
        lower, upper = station.typical_range
        plt.axhline(y=upper, color='r', linestyle='-')
        plt.axhline(y = lower, color = 'g', linestyle = '-')

    
    #makes the plot
    plt.plot_date(t, levels)


    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)


    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


#def plot_water_level_with_fit(station, dates, levels, p):
