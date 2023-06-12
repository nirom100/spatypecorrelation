
import matplotlib.pyplot as plt
import scipy.spatial.distance as dist
import numpy as np
from collections import Counter
from collections import defaultdict
from operator import itemgetter


def main():
    
    spatypes = read_spatypes()
    spatypescountry = read_countries(spatypes)
    countrylistfrequency,individualf = read_frequency()

    #for piechart: Country:, 0:type, 1:individualamount, 2:amountsumforcountry
    res = defaultdict(list)

    for i,j in enumerate(spatypescountry):
        type = j.split(",")[0]
        country = j.rstrip("\n")
        country = country.split(",")[1]
        amount = [item for key,item in countrylistfrequency.items() if key == country]
        amountint = [int(x) for x in amount[0]]

        res[country].append((type,individualf[i],sum(amountint)))

    labels = list(res.keys())
    amount = []
    for key,values in res.items():
        temp = res[key][0]
        amount.append(temp[2])

    zipped = zip(labels,amount)
    newdict = dict(zipped)

    sort = dict(sorted(newdict.items(), key = itemgetter(1), reverse = True)[:8])
    set1 = set(newdict.items())
    set2 = set(sort.items())
    diff = set1 - set2
    other = 0

    for key,values in diff:
        other = other + values

    sort['Other'] = other

    cmap = plt.get_cmap('summer')
    colors = cmap(np.linspace(0., 1., len(sort.keys())))

    plt.pie(sort.values(), labels = list(sort.keys()), autopct='%1.2f%%', colors=colors)
    plt.title("distribution of spa-types sequenced")

    plt.show()

#read spatypes to create distancematrix with same order
def read_spatypes():
    spatypes = []
    with open('../resources/spatypessorted.txt') as spa:
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

def read_frequency():
    frequencies = defaultdict(list)
    individualf = []
    with open('../resources/countrylistfrequency.txt', 'r') as clf:
        for line in clf:
            country= line.split(",")[1]
            country = country.replace("'","")
            country = country.replace("(","")
            frequency = line.split(",")[2]
            frequency = frequency.replace(")","")

            frequencies[country].append(int(frequency))
            individualf.append(int(frequency))
    clf.close()
    return frequencies,individualf


if __name__ == "__main__":
    main()
