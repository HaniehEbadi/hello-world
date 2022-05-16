import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    with open(input_file_name) as input_file:
        reader = csv.reader(input_file)
        hashdict = dict()
        key = list()
        for row in reader:
            hashdict[row[0]] = row[1] #name = row[0] ,hexaformat = row[1]
        for i in range(1000,10000):
            encoded = str(i).encode()
            result = hashlib.sha256(encoded)
            hexaformat = result.hexdigest()
            for name,password in hashdict.items():
                if password == hexaformat:
                    key.append([name,i])                 
    with open(output_file_name, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(key)
        output_file.close()