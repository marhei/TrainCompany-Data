import csv
import json
import sys
import os

def convert(trasse: str):
	with open(trasse, encoding="cp1252") as trasse_f:
		trassen_reader = csv.reader(trasse_f, delimiter=';')
		trassen_reader.__next__()
		# Format: (distance from start, full name, RIL100, is stop)
		waypoints = [(float(waypoint[0].replace(',', '.')), waypoint[1], waypoint[2], 'Kundenhalt' in waypoint[17]) for waypoint in trassen_reader]
	# Split the data into the part relevant for Station.json and Path.json
	waypoints_station = [(waypoint[1], waypoint[2]) for waypoint in waypoints if waypoint[3]]
	waypoints_paths = [(waypoint[0], waypoint[2], waypoint[3]) for waypoint in waypoints]
	extend_station(waypoints_station)
	extend_path(waypoints_paths)

def extend_station(waypoints: list[tuple[str, str]]):
	platform_data = import_platform_data()
	stations = [{
		"group": 2,
		"name": name,
		"ril100": ril100,
		"x": 0,
		"y": 0,
		"platformLength": (platform_data[ril100][1] if ril100 in platform_data else 0),
		"platforms": (platform_data[ril100][0] if ril100 in platform_data else 0)
	} for (name, ril100) in waypoints]
	
	with open("Station.json", encoding="utf-8") as station_f:
		data = json.load(station_f)
		stations_list: list = data["data"]
		ril100_list = [station["ril100"] for station in stations_list]
		new_stations = [station for station in stations if station["ril100"] not in ril100_list]
		stations_list.extend(new_stations)
	with open("Station.json", "w", encoding="utf-8", newline="\n") as output:
		json.dump(data, output, ensure_ascii=False, indent="\t")

def extend_path(waypoints: list[tuple[float, str, bool]]):
	route = []
	# The distance to the next stop (accumulated for all segments without one)
	distance_to_stop = 0
	total_distance = 0
	for (km, ril100, is_stop) in waypoints:
		# Get the distance of the segment
		segment = km - total_distance
		total_distance = km
		# Regardless of whether it is a stop, we will add it
		distance_to_stop += segment
		if is_stop:
			route.append((ril100, int(distance_to_stop)))
			distance_to_stop = 0
	route_segments = [{
		"start": ril_start,
		"end": ril_end,
		"length": segment_length,
		"twistingFactor": 0
	} for ((ril_start, _), (ril_end, segment_length)) in zip(route, route[1:])]
	route_entry = {
		"group": 0,
		"maxSpeed": 0,
		"objects": route_segments
	}
	
	with open("Path.json", encoding="utf-8") as paths_f:
		data = json.load(paths_f)
		paths_list: list = data["data"]
		paths_list.append(route_entry)
	with open("Path.json", "w", encoding="utf-8", newline="\n") as output:
		json.dump(data, output, ensure_ascii=False, indent="\t")

def import_platform_data() -> dict[str, tuple[int, int]]:
	with open("bahnsteige.csv", encoding="utf-8") as platform_f:
		platform_reader = csv.reader(platform_f, delimiter=';')
		platform_reader.__next__()
		platforms = [(int(platform[0]), int(float(platform[4].replace(',', '.')))) for platform in platform_reader]
		platform_data = dict()
		for (bf_nr, platform_length) in platforms:
			if bf_nr not in platform_data:
				platform_data[bf_nr] = [0, 0]
			platform_data[bf_nr][0] += 1
			platform_data[bf_nr][1] = max(platform_data[bf_nr][1], platform_length)
		platform_data = ((bf_nr, tuple(data)) for (bf_nr, data) in platform_data.items())

	# Now we need to convert from Bf-Nr to RIL100
	with open("bahnhoefe.csv", encoding="utf-8") as stations_f:
		stations_reader = csv.reader(stations_f, delimiter=';')
		stations_reader.__next__()
		stations = dict(((int(station[3]), station[5]) for station in stations_reader))
	platform_data_ril100 = dict(((stations[bf_nr], platform_info) for (bf_nr, platform_info) in platform_data))
	return platform_data_ril100

if __name__ == '__main__':
	if not os.path.exists("Path.json") and os.path.exists("../Path.json"):
		os.chdir('..')
	try:
		convert(sys.argv[1])
	except KeyError:
		print("Usage: python convert_trasse.py trassenfinder.csv")