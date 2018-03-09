#Andrew Hilton 3/6/18 Count Longest Word
def passage_list():
    passage = open("alice.txt", "r")
    list_of_passage = passage.read().split() #This function lists the entire textfile and passes the newly made list to the next function
    passage.close
    letter_count(list_of_passage)

def letter_count(passage): 
    biggest_len=0 #Saves biggest length of each word as it runs down the for loop
    for item in passage:
        if len(item) >= biggest_len:
            biggest_len=len(item) #Once it's finished, the string of the biggest word is saved as biggest_str
            biggest_str=item
    print(biggest_str)
passage_list()
