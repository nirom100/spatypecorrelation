import numpy as np
import math

def main():
    spatypes = read_spatypes()
    spatypescountry = read_countries(spatypes)
    coordinates = get_coordinates(spatypes)
    geodistance = np.zeros(shape = (len(spatypescountry),len(spatypescountry)))

    for index, element in enumerate(coordinates):
        for index2, element2 in enumerate(coordinates):
            a = float(element.split(" ")[1])
            b = float(element.split(" ")[2])
            point1 = (a,b)

            c = float(element2.split(" ")[1])
            d = float(element2.split(" ")[2])
            point2 = (c,d)

            distance = haversine(point1,point2)
            geodistance[index][index2] = distance
    print_geodistancematrix(geodistance)


#print location to spa-type
#read spatypes to create distancematrix with same order
def read_spatypes():
    spatypes = []
    with open('../src/spaselection.txt') as spa:
        for line in spa:
            spatype = line.split(",")[0]
            spatypes.append(spatype)
    spa.close()
    return spatypes

#read the countries for the spatype and deliver a sorted result bc the previous results are not sorted the same way as init file
def read_countries(spatypes):
    spatypescountry = []
    target = []
    target2 = []
    index = []
    with open('../resources/countrylist.txt', 'r') as res:
        target = res.readlines()
        for line in target:
            temp = line.split(",")[0]
            target2.append(temp)
        for type in spatypes:
            index.append(target2.index(type))
    res.close()

    i = 0
    for type in spatypes:
        newstring = type + "," + target[index[i]].split(",")[1]
        spatypescountry.append(newstring)
        i = i+1

    return spatypescountry

#get saved coordinates for spatype selection
def get_coordinates(spatypes):
    coordinates = []
    temp = []
    temp2 = []
    index = []

    with open("../resources/locdata.txt", "r") as ld:
        temp = ld.readlines()
        for line in temp:
            templine = line.split(" ")[0]
            temp2.append(templine)
        for type in spatypes:
            index.append(temp2.index(type))
    ld.close()

    i = 0
    for type in spatypes:
        newstring = type + " " + temp[index[i]].split(" ")[1] + " " + temp[index[i]].split(" ")[2]
        coordinates.append(newstring)
        i = i + 1
    return coordinates

#print geodistancematrix to txt file
def print_geodistancematrix(distancematrix):
    with open('geodistancematrix.txt', 'w') as dm:
        for line in distancematrix:
            print(*line, file = dm)
    dm.close()

#haversine formula for distance, source: https://www.educative.io/answers/how-to-calculate-distance-using-the-haversine-formula
def haversine(coord1, coord2):
    lon1, lat1 = coord1
    lon2, lat2 = coord2
    R = 6371000  # radius of Earth in meters
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    meters = R * c  # output distance in meters
    km = meters / 1000.0  # output distance in kilometers

    meters = round(meters)
    km = round(km, 3)
    return km


if __name__ == "__main__":
    main()
