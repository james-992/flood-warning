from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import *
from floodsystem.datafetcher import *

def test_run():

    #input the number of days of data you want to show
    dt = 50
    # Station name to find
    station_name = "Abingdon Lock"

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
