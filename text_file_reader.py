import csv 

def read_from_file(filepath):
    """Reads the string data from a text/csv file into a dictionary. The expected format is as follows: <key>|<string data>"""
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='|')
        file_dictionary = {}
        for row in csv_reader:
            file_dictionary[row[0]] = row[1]
        csv_file.close()
        return file_dictionary


#print(read_from_file("test.txt"))