import random, string

dfile1 = open("searchf.txt", "a")

infor = []
infor.append(input("First Name: ") + "\n")
infor.append(input("Last Name: ") + "\n")
infor.append(input("Your Age: ") + "\n")
infor.append(input("City: ") + "\n")
infor.append(input("State: ") + "\n")

dfile1.write("\nSearch Result:\n")
dfile1.writelines(infor)
plates = (str(random.randint(1,9)) + random.choice(string.ascii_uppercase) + "/" + str(random.randint(0,9999)))
dfile1.write(plates)

print("\nSearch Complete! \nYour License Plate # " + plates)

print(input("\nPress Enter to Close\n"))

dfile1.close()