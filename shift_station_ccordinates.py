import json
from sys import argv

def shift(x: int, y: int):
	"""Takes all stations and shifts their x and y-coordinates by the specified amount."""
	with open("Station.json", encoding="utf-8") as stations_file:
		data = json.load(stations_file)
		stations_list = data["data"]
		for station in stations_list:
			station['x'] += x
			station['y'] += y
	with open("Station_shifted.json", "w", encoding="utf-8") as output:
		# Preserve Unicode and formatting
		json.dump(data, output, ensure_ascii=False,indent="\t")

if __name__ == '__main__':
	x = int(argv[1])
	y = int(argv[2])
	shift(x, y)
