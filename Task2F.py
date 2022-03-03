
import matplotlib.pyplot as plt

from floodsystem.datafetcher import *
from floodsystem.analysis import *
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import *
from floodsystem.datafetcher import *


def run():
    p = 4
    #   build and update the lsit of stations
    stations = build_station_list()
    update_water_levels(stations)

    #   set variable N
    N = 5
    dt=2

    #   Print out stations as the questions requests
    for station in stations_highest_rel_level(stations, (N+1)):
        station_name = station[0]
        #specific_station = None
        if station[0] == "Letcombe Bassett":
            print("Letcombe Bassett is not shown, it's data is bad")
            pass 
        else: 
            for station_obj in stations:
                if station_obj.name == station_name:
                    specific_station = station_obj

                else:
                    pass


                
            dates, levels = (fetch_measure_levels(specific_station.measure_id,
                                                dt=datetime.timedelta(days=dt)))
            plot_water_level_with_fit(specific_station, dates, levels, p)
            poly, d0 = polyfit(dates, levels, p)
            print("poly is ", poly)
            print("offset is", d0)



       

if __name__ == "__main__":
    print("Task 2F Running...")
    run()


