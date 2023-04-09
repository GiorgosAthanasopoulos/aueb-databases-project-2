#!/usr/bin/env python3
# to extract data from keywords.csv file
from csv import reader
# string to json
import ast
# to get current working directory
import os
# to use exit function
import sys


# simple wrapper for id, name of every keyword
class Keyword:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    # string representation of keyword class
    def __str__(self):
        return str(self.id) + ", " + self.name


# check if a keyword(id basically) already exists in a list/set of keywords (repo)
def exists_in_keyword_repository(repo, id):
    for keyword in repo:
        if keyword.id == id:
            return True
    return False


# simple wrapper class for movie data structure
class Movie:
    def __init__(self, id):
        self.id = id
        self.keywords_list = []

    def __str__(self):
        return str(self.id) + ", " + str(self.keywords_list)


# check if a keyword already exists in a movie keyword list
def exists_in_movie_keyword_list(movie, id):
    for keyword in movie.keywords_list:
        if keyword == id:
            return True
    return False


#basic check to make sure that the files are in the correct paths
if not os.getcwd().endswith("src"):
    print("Make sure to run the python script from within the src directory to make sure that the program can find the files it depends on...")
    sys.exit(1)

print("Due to the amount of data, the program takes about 20 seconds to finish. Please be patient...")

# produced keyword repository
keyword_repository: set = set()
# produced movie list
movie_repository: set = set()

# open keywords.csv and give it alias f
with open('../data/dataset/keywords.csv', 'r') as f:
    # read f in csv format
    data = reader(f)
    # first line is headers, gives format of the rest of the file
    header = next(data)

    # if the file is not empty
    if header != None:
        # for every non-header line
        for row in data:
            # first element of the string is the movie_id
            movie_id = row[0]
            # register movie to movie repository
            movie = Movie(int(movie_id))
            movie_repository.add(movie)
            # second element is a string of list of json objects (which is also considered valid json)
            movie_keywords_string = row[1]
            # convert json string to json list
            movie_keywords_json = ast.literal_eval(movie_keywords_string)
            # for every keyword in list
            for keyword in movie_keywords_json:
                # create a temporary new keyword
                _keyword = Keyword(keyword['id'], keyword['name'])
                # if the temporary new keyword is not already in the keyword repository
                if not exists_in_keyword_repository(keyword_repository, _keyword.id):
                    # add it to the keyword repo
                    keyword_repository.add(_keyword)
                # if the temporary new keyword is not already in the keyword list of the movie
                if not exists_in_movie_keyword_list(movie, _keyword.id):
                    # add it to the movie keyword list
                    movie.keywords_list.append(_keyword.id)

# now that we have the keyword repository we can already create the first of the 2 sub-files
# which is the one containing the id, name pair of keywords
with open('../data/dataset/keyword.csv', 'w') as f:
    f.write("id, name\n")
    for keyword in keyword_repository:
        f.write(str(keyword.id) + ", " + keyword.name + "\n")

# for the second file we re gonna have to do some more data manipulation...
with open('../data/dataset/haskeyword.csv', 'w') as f:
    f.write('movie_id, keyword_id\n')
    for movie in movie_repository:
        for id in movie.keywords_list:
            f.write(str(movie.id) + ", " + str(id) + "\n")
