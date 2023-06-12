import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
import scipy.cluster.hierarchy as shc
import scipy.spatial.distance as dist
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from collections import defaultdict



def main():
    matrix = read_distance('distancematrix.txt')
    get_locdata()
    mlen = len(matrix)

    labels = [get_labels(i) for i in range(0,mlen)]

    #create condensed matrix
    condensedgen = dist.squareform(matrix,'tovector',False)

    #Hierarchical Clustering based on previously created distance matrix
    #linkage matrix
    Z = shc.linkage(condensedgen, 'single')

    #create dendrogram with spatype-labels, set cmap
    plt.figure(figsize=(8,12))
    cmap = cm.turbo(np.linspace(0, 6, mlen))
    shc.set_link_color_palette([mpl.colors.rgb2hex(rgb[:4]) for rgb in cmap])

    dendrogram = shc.dendrogram(Z,
                                color_threshold = 0.25, #cluster threshold, max HED distance = 0.2
                                above_threshold_color = "grey",
                                orientation="right",
                                no_labels = True) #set labels = labels instead for printing of spa-type numbers
                                                 #set no_labels = True for no labels

    #Get number of clusters + its contents in separate file for further work
    cutoff = get_cluster_amount(dendrogram)
    clusters,cldata = get_clusters(Z,cutoff)

    add_cluster_to_map(cldata)
    print_clusters(clusters,"genclusters.txt")

    #Visualization of Dendrogram
    plt.title("genetical clustering dendrogram of spa-types")
    plt.ylabel("spa-type index")
    plt.xlabel("genetic distance")
    plt.savefig('genetic.pdf')
    plt.show()

    return cldata

#read distance matrix
def read_distance(filename):
    matrix = []
    with open(filename) as dm:
        for line in dm:
            line = line.rstrip("\n")
            arr = line.split()
            matrix.append(arr)
    dm.close()
    matrix = np.array(matrix)
    return matrix

#get labels of spatypes
def get_labels(i):
    spatypes = []
    with open("spaselection.txt") as spa:
        for line in spa:
            spatype = line.split(",")[0]
            spatypes.append(spatype)
        spa.close()
    return spatypes[i]

#get the contents of clusters and save them in groups for further evaluation, form flat clusters out of dendrogram
def get_clusters(Z,cutoff):
    clusters = defaultdict(list)
    # flat clusters so that the original observations in each flat cluster have no greater a cophenetic distance than t.
    cldata = fcluster(Z, t=0.25 , criterion='distance')  #cluster threshold, max HED distance = 0.2
    for count,value in enumerate(cldata):
        clusters[value].append(get_labels(count))
    return clusters,cldata


# gets cut-off / amount of clusters based on color / NOT USED IN FINAL VERSION
def get_cluster_amount(dendrogram):
    cutoff = []
    cutoff_counter = 0
    for color in dendrogram['leaves_color_list']:
        if color not in cutoff:
            cutoff.append(color)
            cutoff_counter += 1
    return cutoff_counter

#prints clusters into an extra file
def print_clusters(clusters,filename):
    with open(filename, 'w') as cl:
        for key,values in clusters.items():
            for value in values:

                print(f"{key} - {value}",file = cl)
    cl.close()
    print("clusters have been printed to " + filename)

def add_cluster_to_map(cldata):
    #get locdata for selection only, format into mapinput to create folium map - remove the country names and use alpha-02 spatypecorrelation
    with open("selectlocdata.txt", "r") as tl:
        for index,line in enumerate(tl):
            newline = line.rstrip("\n")
            #due to country entries with different word count such as "United Kingdom" vs "Germany" vs "United Arab Emirates" we have to access different indices for the alpha-02 spatypecorrelation
            if len(newline.split(" ")) == 7:
                input = newline.split(" ")[0]+" "+newline.split(" ")[1]+" "+ newline.split(" ")[2]+" "+newline.split(" ")[6]+" "+str(cldata[index])
            elif len(newline.split(" ")) == 6:
                input = newline.split(" ")[0]+" "+newline.split(" ")[1]+" "+ newline.split(" ")[2]+" "+newline.split(" ")[5]+" "+str(cldata[index])
            else:
                input = newline.split(" ")[0]+" "+newline.split(" ")[1]+" "+ newline.split(" ")[2]+" "+newline.split(" ")[4]+" "+str(cldata[index])
            with open("mapinput.txt", "a") as tln:
                print(input, file=tln)

#get locdata for individual spa-selection
def get_locdata():
    target = []
    target2 = []
    index = []
    spatypes = []

    with open("spaselection.txt") as spa:
        for line in spa:
            spatype = line.split(",")[0]
            spatypes.append(spatype)
        spa.close()

    with open("../resources/locdata.txt", "r") as ld:
        target = ld.readlines()
        for line in target:
            temp = line.split(" ")[0]
            target2.append(temp)
        for type in spatypes:
            index.append(target2.index(type))
    ld.close()

    i = 0
    with open("selectlocdata.txt", "a") as sl:
        for type in spatypes:
            newstring = target[index[i]]
            newnewstring = newstring.rstrip("\n")
            print(newnewstring, file = sl)
            i = i + 1



if __name__ == "__main__":
    main()
