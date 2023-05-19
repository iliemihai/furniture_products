import sys

f = open("../data/raw_data.txt", "r")
g = open("../data/dedup_data.csv", "w")

data_pages = f.read().split("<TEXT_SEPARATOR>")
g.write("LINES\n")
aux_dict = {}

for page in data_pages:
    # aux_dict = {}
    for line in page.split("\n"):
        if hash(line) not in aux_dict.keys():
            aux_dict[hash(line)] = line

    # for dedup_line in aux_dict.values():
    #    g.write(dedup_line+"\n")
    # g.write("<TEXT_SEPARATOR>")

for dedup_line in aux_dict.values():
    g.write(dedup_line + "\n")
