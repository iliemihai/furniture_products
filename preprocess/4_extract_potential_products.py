f = open("../data/adnotated_data.csv", "r")
g = open("../data/potential_products.txt", "w")

for line in f.readlines():
    if ",Yes" in line.strip():
        g.write(line.strip().replace(",Yes", "") + "\n")
