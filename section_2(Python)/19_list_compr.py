num=[1,3,5]
doubled=[x*2 for x in num]
print(doubled)

# ----------------------
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
friends_2 = ["Sam", "Samantha", "Saurabh",]
starts_s =[x for x in friends if x.startswith("S")]
print(starts_s)

### checking id which shows they are stored seperately so they are not the same!!
print("freinds_2:",id(friends_2) ,"starts_s:",id(starts_s))