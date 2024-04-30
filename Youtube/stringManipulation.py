a = "India is 'very' beautiful place"
b = 'Bangladesh is "very" beautiful place'

print(a)
print(b)
# India is 'very' beautiful place
# Bangladesh is "very" beautiful place

c = 'Bangladesh is \'very\' beautiful place'
print(c)  # Bangladesh is 'very' beautiful place


number = 465.212340932
print("%.2f" % number)

firstName = input("enter Your First Name : ")
secondName = input("enter Your Second Name : ")

print("Good Morning", firstName + " " + secondName)
print("Hello {} {} ".format(firstName, secondName))
