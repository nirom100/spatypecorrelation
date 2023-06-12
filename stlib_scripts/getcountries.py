from IPython.display import display
from collections import Counter
import pandas as pd
import numpy as np
import requests
import geonamescache
from collections import defaultdict
import os


def main():
    with open("../resources/spatypessorted.txt", "r") as st:
        for line in st:
            newline = line.split(",")[0]
            country_process(newline)


def print_results(string,filename):
    with open(filename, 'a') as rs:
        print(string, file = rs)
    rs.close()

def country_process(spatype):
    url = get_url(spatype)
    get_countries(url,spatype)

#create file with countries
def print_countries(countries):
    with open('countries.txt', 'w') as c:
        for line in countries:
            print(line, file = c)
    c.close()

#get the url of the spatype
def get_url(spatype):
    url = "https://spa.ridom.de/spa-" + spatype + ".shtml"
    return url

#get the country database from url
def get_countries(url,spatype):
    request = requests.get(url, verify = False)
    dataframe = pd.read_html(request.text)

    dataframe_isolated = dataframe[4]

    countries = dataframe_isolated["Country"]

    print_countries(countries)
    clearedcountries = clear_countries()

    result, resultcleared = max_country(clearedcountries)
    result = spatype + "," + result
    resultcleared = spatype + "," + resultcleared
    print_results(result, '../resources/countrylistfrequency.txt')



#open country file and sort
#checks if country is in country or city, only stores what checks one of those boxes so far
def clear_countries():
    gc = geonamescache.GeonamesCache()
    countries = gc.get_countries_by_names()
    clearedcountries = []
    with open('countries.txt', 'r') as c, open('clearedcountries.txt','w') as cc:
        for line in c:
            line2 = line.rstrip('\n').casefold().capitalize().title()
            if line2 in countries or line2 in gc.get_cities_by_name(line2):
                print(line2, file = cc)
                clearedcountries.append(line2)
            if line2 == "Detmold" or line2 == "Minden":
                line2 = "Germany"
                print(line2, file = cc)
                clearedcountries.append(line2)

    c.close()
    cc.close()
    return clearedcountries


#most common country
def max_country(clearedcountries):
    maxcountry = Counter(clearedcountries)
    result = ' '.join([str(elem) for elem in maxcountry.most_common(1)])
    resultcleared = result[2:].split("',")[0]
    return result, resultcleared

if __name__ == "__main__":
    main()
