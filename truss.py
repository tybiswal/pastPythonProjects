# keep inputting words into a list until a blank is detected
# then once a blank is detected (press enter), break the input loop
# and print the complete list
i = 1
wlist=[]

while i < 6:
    word = input("Type a word: ")

    if word != '':
        wlist.append(word)
    elif word == '':
        print("\n")
        print(' '.join(wlist))
        break
