
from floodsystem.datafetcher import *
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
from datetime import datetime, timedelta
import matplotlib
import matplotlib.pyplot as plt
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels


#input the number of days of data you want to show
dt = 10
# Station name to find
station_name = "Hayes Basin"

# Build list of stations
stations = build_station_list()
station_of_interest = None
for station in stations:
    if station.name == station_name:
        station_of_interest = station
        break

if not station_of_interest:
    raise ValueError("Station {} could not be found".format(station_name))

# find the dates and the levels associated 

dates, levels = (fetch_measure_levels(station_of_interest.measure_id,
                                     dt=datetime.timedelta(days=dt)))
 

plot_water_levels(station_of_interest, dates, levels)


                                    