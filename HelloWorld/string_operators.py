string1 = "Lord Khorne, "
string2 = "grant me your power, "
string3 = "that I might sweep "
string4 = "this army "
string5 = "aside!"

print(string1 + string2 + string3 + string4 + string5)

print("Lord Khorne, " "grant me your power, " "that I might sweep " "this army " "aside!")
print("Hello " * 5) #Multiplying a string
# print("Hello " * 5 + 4) Cannot concatenate string with integer
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

supreme_god = "Khorne"
print("ne" in supreme_god)          #True
print("Khor" in supreme_god)        #True
print("Tzeentch" in supreme_god)    #False
print("forward" in "aside")         #False