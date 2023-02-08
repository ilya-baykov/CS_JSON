import csv

crimes = {}
with open("Crimes.csv", "r") as file, open("answer.txt", "w") as answer:
    info_data = csv.reader(file)
    for row in info_data:
        if "2015" in row[2]:
            crimes[row[5]] = crimes.setdefault(row[5], 0) + 1
    sorted_crimes = sorted(crimes.items(), key=lambda item: item[1], reverse=True)
    answer.write(sorted_crimes[0][0])
    file.close()
    answer.close()
