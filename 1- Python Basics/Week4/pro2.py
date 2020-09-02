# Given the list of numbers, numbs, create a new list of those same numbers increased by 5.
# Save this new list to the variable newlist.





numbs = [5, 10, 15, 20, 25]
newlist = []

for num in range(len(numbs)):
    newlist.append(numbs[num] + 5)
    print(newlist)
