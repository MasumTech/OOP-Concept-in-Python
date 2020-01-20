from Player import Player

player1 = Player("Tom", 20)

player2 = Player("Jerry",20)



#Access via class name.

print("Player.minAge = ", Player.minAge)


#Access via object.

print("player1.minAge = ", player1.minAge)

print("player2.minAge = ", player2.minAge)

print("--------------")



print("Assign new value to minAge via class name, and print..")

#Assigin new value to minAge via class name

Player.minAge = 20


print("Player.minAge = ", Player.minAge)
print("player1.minAge = ", player1.minAge)
print("player2.minAge = ", player2.minAge)


 







'''

print("player1.name = ", player1.name)

print("player1.age = ", player1.age)


print("player2.name = ", player2.name)

print("player2.age = ", player2.age)


print("----------------")

print("Assign new value to Player1.age = 21")

#Assign new value to age attribute of player1.

player1.age = 21



print("player1.name = ", player1.name)

print("player1.age = ", player1.age)


print("player2.name = ", player2.name)

print("player2.age = ", player2.age)

'''





