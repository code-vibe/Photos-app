import os
def extract_place(filename):
    return filename.split("_")[1]

print(extract_place("2016-11-04_Berlin_09/42/22.jpg"))

#os.chdir("Photos")

#originals = os.listdir()

#print(originals)