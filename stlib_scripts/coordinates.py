import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from geopandas.tools import geocode
from itertools import islice
import numpy as np
import pycountry

#get coordinates for all entries and save to txt file
def main():
    countrylist = []
    spatypes = read_spatypes()
    spatypescountry = read_countries(spatypes)

    n = len(spatypes)
    for i in spatypescountry:
        i = i.rstrip("\n")
        countrylist.append(i.split(",")[1])

    d = {'type' : spatypes, 'country': countrylist}
    df = pd.DataFrame(data = d)

    geo = geocode(df['country'])
    df1 = geo.join(df)

    #some names could not be matched to alpha_02 codes, because the old ISO country name was saved
    #exceptions for those cases were written

    for index, element in df1.iterrows():
        type = element['type']
        a = element['geometry'].x
        b = element['geometry'].y
        c = element['country']
        #print(countrylist[index])
        if countrylist[index] == "Iran":
            d = "IR"
        elif countrylist[index] == "Czech Republic":
            d = "CZ"
        elif countrylist[index] == "South Korea":
            d = "KR"
        elif countrylist[index] == "Taiwan":
            d = "TW"
        elif countrylist[index] == "Kosovo":
            d = "XK"
        elif countrylist[index] == "Ivory Coast":
            d = "CI"
        elif countrylist[index] == "Tanzania":
            d = "TZ"
        elif countrylist[index] == "Cape Verde":
            d = "CV"
        elif countrylist[index] == "Bolivia":
            d = "BO"
        else:
            d = pycountry.countries.get(name=countrylist[index]).alpha_2


        print_location(type,a,b,c,d)


def print_location(line,a,b,c,d):
    with open("../resources/locdata.txt", 'a') as tl:
        print(line, a, b, c, d, file=tl)

#open second file used, spatypecorrelation works only up to 999 entries, so we had to do multiple iterations
def read_spatypes():
    spatypes = []
    with open('spatypessorted2.txt') as spa:
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

if __name__ == "__main__":
    main()
