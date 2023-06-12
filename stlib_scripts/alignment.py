import homoeditdistance
from homoeditdistance import homoEditDistance
from time import time
from itertools import islice


def main():
    start  = time()
    print("initialize sequence alignment..")

    repeats,spatypes = read_spatypes()
    print("data has been stored.")

    scoringmatrix = scoring_matrix(repeats)
    print("scoringmatrix initialized.")

    scoringmatrix = fill_matrix(repeats,scoringmatrix)
    print_matrix(scoringmatrix)

    print(f"time taken to run HED algorithm: {time() - start} seconds")



# Read spaselection file, save types into strings
def read_spatypes():
    repeats = []
    spatypes = []
    with open('spaselection.txt') as spa:
        for line in spa:
            spatype = line.split(",")[0]
            spatypes.append(spatype)
            newline = line.split(",",1)[1]
            repeats.append(newline.rstrip("\n"))
    spa.close()

    return repeats,spatypes

#split a string at - and return, remove "-" from repeat sequence, encode sequence for alignment
def split_spatypes(string):
    new_string = list(string.split("-"))
    encoded = ""
    for i,j in enumerate(new_string):
        encoded = encoded + chr(int(new_string[i])+30)
    return encoded

#create score matrix and init with 0
def scoring_matrix(repeats):
    n = len(repeats)
    scoring_matrix = [[0 for x in range(n+1)] for y in range(n+1)]
    return scoring_matrix

#fill the created matrix with the called alignment function
def fill_matrix(repeats,scoringmatrix):
    n = len(repeats)
    for i in range(1,n+1):
        for j in range(1,n+1):
            str1 = repeats[i-1]
            strtest1 = split_spatypes(str1)
            str2 = repeats[j-1]
            strtest2 = split_spatypes(str2)
            length = len(strtest1) + len(strtest2)
            alignment_score ='{}'.format(homoEditDistance(strtest1, strtest2, 0)['hed'])
            scoringmatrix[i][j] = int(alignment_score) / length

    print("score matrix has been printed to distancematrix.txt")
    return scoringmatrix

#print the matrix into a txt file
def print_matrix(scoringmatrix):
    with open('distancematrix.txt', 'w') as dm:
        for line in islice(scoringmatrix,1, None):
            line = line[1:]
            print(*line, file = dm)
    dm.close()

if __name__ == "__main__":
    main()
