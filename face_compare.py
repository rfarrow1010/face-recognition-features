import os

SOURCE_PATH = "/Volumes/Extreme Pro/FRGC-2.0-dist/FRGC-2.0-dist/nd1/Fall2003" # points to fall 2003
DEST_PATH = "/Volumes/Extreme Pro/FacialRetouch/"

# here, the keys are the names of directories in FacialRetouch and the values
# are the corresponding suffixes that were appended to each filename when the 
# processed files were made
DEST_DIRNAMES = {
    "eyes_50": "_eyes50",
    "eyes_100": "_eyes100",
    "faceshape_50": "_faceShape50",
    "faceshape_100": "_faceShape100",
    "lips_50": "_lips50",
    "lips_100": "_lips100",
    "nose_50": "_nose50",
    "nose_100": "_nose100"
}

# the structure of the original filenames is:
# (person's ID #)d(this picture's #)
# this is because one person will have anywhere from 30 to 60 pictures of them from different angles
# we will need to get the ID # and use it to generate random pairs of pictures for each person
filenames = []

def main():
    # add all filenames in Fall 2003 to filenames list
    for root, dirs, files in os.walk(SOURCE_PATH):
        for file in files:  
            filenames.append(file)

if __name__ == "__main__":
    main()