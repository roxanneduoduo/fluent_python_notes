import csv


with inplace(csvfilename, 'r', newline='') as (infh, outfh):
    reader = csv.reader(infh)
    writer = csv.writer(outfh)

    for now in reader:
        row += ['new', 'columns']
        writer.writerow(row)


# reference http://www.zopatista.com/python/2013/11/26/inplace-file-rewrite/
