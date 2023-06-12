from collections import defaultdict

#read data from countrylist and clustering,  save into separate file for clustering results

def main():
    countries = []
    genclusters = get_clusters("genclusters.txt")
    sequences = []
    with open("../resources/countrylist.txt", "r") as rl:
        for line in rl:
            line = line.rstrip()
            countries.append((line.split(",")[0],line.split(",")[1]))
    rl.close()

    with open("spaselection.txt", "r") as spa:
        for line in spa:
            line = line.rstrip()
            sequences.append((line.split(",")[0],line.split(",")[1]))
    spa.close()

    for k, types in genclusters.items():
        clusterstring = "cluster number:" + k + " "
        #print_results2(clusterstring)
        print_results(clusterstring, " ", 'genclusterresult.txt')
        #catch error of lines having " " in front of type:
        for type in types:
            if type[0] == " ":
                newtype = type[1:]
                get_countries(countries,newtype,'genclusterresult.txt',sequences)
            else:
                get_countries(countries,type,'genclusterresult.txt',sequences)

def get_countries(countries, type, filename,sequences):
    sequence = get_sequence(sequences,type)
    #print_results2([item[1] for item in countries if item[0] == type])
    print_results([item for item in countries if item[0] == type], sequence, filename)

def get_sequence(sequences, type):
    return [item[1] for item in sequences if item[0] == type]

def print_results(string,string2, filename):
    with open(filename, 'a') as rs:
        print(string, string2, file = rs)
    rs.close()

def print_results2(string):
    with open("untitled.txt", 'a') as rs:
        print(string, file = rs)
    rs.close()


def get_clusters(filename):
    clusters = defaultdict(list)
    with open(filename, 'r') as cl:
        for line in cl:
            cluster = line.split("-")[0]
            clusters[cluster].append(line[4:].rstrip("\n"))
    cl.close()
    return clusters


if __name__ == "__main__":
    main()
