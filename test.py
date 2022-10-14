# import re
# import csv
# data = []
# count  = 0
# with open("title_principle.tsv") as title_principle:
#     with open("title_principle.tsv") as title_basic :
#         tsv_title_principle = csv.reader(title_principle, delimiter="\t")
#         tsv_title_basic = csv.reader(title_basic, delimiter="\t")
#         for L1 in tsv_title_basic:
#             print(L1[0])
#             print(L1)
fields = ['tconst',	'titleType',	'primaryTitle',	'originalTitle',	'isAdult'	,'startYear'	,'endYear'	,'runtimeMinutes',	'genres' ,'averageRating' , 'numVotes']
# with open('GFG.csv', 'w') as f:
      
#     # using csv.writer method from CSV package
#     write = csv.writer(f)
      
#     write.writerow(fields)
#     write.writerows(data)
import csv
 
# open .tsv file
file1 = open("title_basics.tsv", encoding="utf8")
file2 = open("title_ratings.tsv", encoding="utf8")
    # Passing the TSV file to 
    # reader() function
    # with tab delimiter
    # This function will
    # read data from file
tsv_file1 = csv.reader(file1, delimiter="\t")
tsv_file2 = csv.reader(file2, delimiter="\t")
    # printing data line by line
title_basics_data = []
title_ratings_data = []
for l1 in tsv_file1:
    # print(l1[0])
    # print(l1[1])
    # print(l1[2])
    # print(l1[3])
    # print(l1[4])
    # print(l1[5])
    # print(l1[6])
    # print(l1[7])
    # print(l1[8])
    if len(l1) == 9:
        row = [l1[0],l1[1],l1[2],l1[3],l1[4],l1[5],l1[6],l1[7],l1[8]]
        title_basics_data.append(row)
for l1 in tsv_file2:
    if len(l1) == 3:
        row = [l1[0],l1[1],l1[2]]
        title_ratings_data.append(row)


data = []
for l1 in title_basics_data[1:]:
    for l2 in title_ratings_data[1:]:
        if l1[0] == l2[0]:
            row = l1 + l2[1:]
            data.append(row)
            break
with open('final.csv', 'w') as f:
      
    #using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(fields)  
    write.writerows(data)
    