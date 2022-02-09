def test_list_types():
    assert type(samplelist) == list
    assert type(samplelist[0]) == tuple
    
def test_list_length_check():
    assert len(rivers_by_station_number(stations, 40)) == 48
    assert len(rivers_by_station_number(stations, 20)) < len(samplelist)
    assert len(rivers_by_station_number(stations, 13)) == len(rivers_by_station_number(stations, 14))