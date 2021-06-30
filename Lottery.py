import random
Participants =[]
n=int(input("Number of participants :"))
for i in range(0,n):
    print("Name of Participants:".format(i+1))
    elem=input()
    Participants.append(elem)
    print("Participants are:", Participants)
    random_num=random.choice(Participants)
    print("Winner is : ",random_num)