import datetime

print("\nStudent Roster Kit\n")

list1 = ["Andrew", "Becky", "Carol", "Dennis"]
print("Student Names:\n", list1)


confirm = input("\nDo you want to add a new student? Y/N: ")

while confirm == 'Y' or confirm =='y':
    list1.append(input("\nAdd a new student name: "))
    print(list1)
    confirm = input("\nDo you want to continue? Y/N: ")
else:
    print("\nOk, let's continue...")

print("There are " + str(len(list1)) + " students in my class.\n")

list2 = []
list3 = []
y = 0
for x in list1:
    list2.append(input("What is the age of " + str(x) + "?: "))
    list3.append([list1[y], list2[y]])
    y+=1

f = open("roster.txt","a")
f.write(str(datetime.datetime.now()))
f.write("\nStudent Roster\n")

print("\nStudent Roster:")
z = 0
for w in list3:
    out = (str(z+1) +": " + str(list3[z]))
    print(out)
    f.write(out+"\n")
    z+=1

# insert the name and age into a dictionary




f.close()
print(input("\n\nPress Enter to End"))