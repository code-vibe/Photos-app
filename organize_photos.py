import os

def extract_place(filename):
    return filename.split("_")[1]

def make_place_directories(places):
	for place in places:
		os.mkdir(place)
	

os.chdir("Photos")
originals = os.listdir()
places = []


for filename in originals:
	place = extract_place(filename)
	places.append(place)

print(places)