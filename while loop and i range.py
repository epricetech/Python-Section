#while loop is less consice as a for loop and i range


print ('My name is ')
i = 0
while i < 5:
    print ('Jimmy five times (' + str(i) + ')')
    i = i + 1

# starting, stopping and stepping arguments in a range

#starting  and starting  arguments  pick where the numbers begin and end
for i in range (12, 16):
    print (i)

#Steping arguments
for i in range (0, 10, 2):
    print (i)

# negagtime stepping
for i in range (5, -1, -1):
    print(i)

