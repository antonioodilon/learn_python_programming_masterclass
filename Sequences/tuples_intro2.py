british = "Dead Sun", "British Murder Boys", 2011
schwefelgelb = "Bis Zum Nachsten Tag", "Schwefelgelb", 2016
liebing = "Tunox", "Chris Liebing", 1992
kruse = "Latin Lovers", "Monika Kruse", 2008
porto = "Sambassim", "Fernanda Porto", 2010

print(liebing)
print(liebing[0])
print(liebing[1])
print(liebing[2])
# We can use indexing with tuples

# liebing[0] = "Something Half Way"
# Tuples do not support item assignment because they're immutable

liebing2 = list(liebing)
print(liebing2)

#Now we can change what's in index position 0:
liebing2[0] = "Something Half Way"
print(liebing2)

print(british, schwefelgelb, liebing) # Returns several tuples

print((british, schwefelgelb, liebing)) # Returns one tuple with several
# tuples in it