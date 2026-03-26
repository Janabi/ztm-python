from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def capitalize(item: str):
    return item.capitalize()
print(list(map(capitalize, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_numbers.sort()
print(list(zip(my_numbers, my_strings)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def passed(score):
    return score > 50

print(list(filter(passed, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item
total_scores = reduce(accumulator, scores, 0)
total_numbers = reduce(accumulator, my_numbers)
total = total_numbers + total_scores
print(total)