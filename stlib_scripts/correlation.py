import pandas as pd
import matplotlib.pyplot as plt
import scipy.spatial.distance as dist
import numpy as np
import seaborn as sns

def main():
    correlation()

def correlation():

    gendistance = pd.read_csv('distancematrix.txt', sep=" ", header=None)
    gendistancenp = gendistance.to_numpy()

    geodistance = pd.read_csv('geodistancematrix.txt', sep=" ", header=None)
    geodistancenp = geodistance.to_numpy()

    geocomp = dist.squareform(geodistancenp,'tovector',False)
    gencomp = dist.squareform(gendistancenp,'tovector',False)

    

    sns.relplot(x=geocomp,y=gencomp, height=10, aspect=10/8)

    plt.suptitle("correlation of genetic and geographic distance")
    plt.xlabel("geographic distance in km")
    plt.ylabel("genetic distance")
    plt.savefig('correlation.pdf')

    plt.show()

    #pearsons r - correlation coefficient
    r = np.corrcoef(geocomp,gencomp)
    print("pearson's r : ")
    print(r[0][1])


if __name__ == "__main__":
    main()
