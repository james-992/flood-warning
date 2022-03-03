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
import numpy as np


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

  #  plt.xlim([dates[0], dates[-1]])


    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()



def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree 4
    p_coeff = np.polyfit(x - x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
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

    # Plot original data points
    plt.plot(x-x[0], y, '.')

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    matplotlib.pyplot.xlabel("time from present / days")
    matplotlib.pyplot.ylabel("water height / m")
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1-x[0], poly(x1 - x[0]))
    plt.title(station.name)

    # Display plot
    plt.show()

