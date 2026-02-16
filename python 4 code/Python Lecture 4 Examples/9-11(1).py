Import jieba library with open("J. K. Rowling - Harry Potter 1 - Sorcerer's Stone.txt", "r")as file:
txt = file.read()  # open the file and read its contents
words = jieba.lcut(txt)  # segment the text, and store the results in the words list
counts = {}  # define a dictionary to store words and counters for word in words:
If len(word) == 1:  #Exclude single-character segmentation results continue
else:
counts[word] = counts.get(word, 0) + 1    #increment counter
items = list(counts.items())                    #convert dictionary entries to list
items.sort(key=lambda x: x[1], reverse=True)    #sort by value in descending order
for i in range(15):                            #output top 15 items word, count = items[i]
print ("{0:<10}{1:>5}".format(word, count))
