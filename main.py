Songs = ["Rockstar", "Do it", "For the Night"]

print(Songs[0])
print(Songs[2])

print(Songs[1:2])

Songs[2] = "Yoru Ni Kakeru"

Songs.append("Tabun")
Songs.append("Halzion")
Songs.append("Lemon")

del Songs[5]

animals = ["Cat", "Dog", "Chicken"]

animals.append("Potato")

print(animals[2])

del animals[0]

for i in range(len(animals)):
     print(animals[i])