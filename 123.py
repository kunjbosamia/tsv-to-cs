import csv
file1 = open("title_basics.tsv", encoding="utf8")
file2 = open("title_ratings.tsv", encoding="utf8")
    # Passing the TSV file to 
    # reader() function
    # with tab delimiter
    # This function will
    # read data from file
tsv_file1 = csv.reader(file1, delimiter="\t")
tsv_file2 = csv.reader(file2, delimiter="\t")
for l1 in tsv_file1:
  print(len(l1))