
data = input("Enter a message: ")
s = 4
letter=""

cipher={}
for i in range (len(data)):
    char = data[i]
    cipher[i] = chr((ord(char) + s- 65) % 26 + 65)

print(cipher)
for i in range (len(cipher)):
    letter += "".join(cipher[i])
print("Here your's Encrypted message: {}".format(letter))
