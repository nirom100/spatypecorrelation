import pandas as pd
import numpy as np
import requests
import random

#init selection of N spatypes and print to spaselection.txt
def main():

    spatype_selection()


def spatype_selection():
    inp = input("Enter a number N for a selection of N random spatypes:")
    with open('../resources/spatypessorted.txt') as st1:
        curr_entries = len(st1.readlines())
    st1.close()

    
    random.seed(20)
    ra = random.sample(range(1,curr_entries),int(inp))
    with open('../resources/spatypessorted.txt') as st2:
        spatypes = st2.readlines()
        for line in ra:
            for index,content in enumerate(spatypes):
                if line == index:
                    print_spatypes(spatypes[index])
    st2.close()


def print_spatypes(line):
    with open('spaselection.txt', 'a') as ss:
        print(line, end="", file = ss)
    ss.close()


if __name__ == "__main__":
    main()
