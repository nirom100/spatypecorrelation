from stlib_scripts import alignment, selection, distance, clustering, readdata, correlation
import os
import streamlit as st

def main():
    selection.main()

    alignment.main()

    distance.main()

    clustering.main()

    readdata.main()

    correlation.main()


    os.remove("selectlocdata.txt")
    os.remove("genclusters.txt")



if __name__ == "__main__":
    main()
