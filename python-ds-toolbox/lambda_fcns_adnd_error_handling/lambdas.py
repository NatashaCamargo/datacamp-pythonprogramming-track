# anonymous functions
nums = [48, 6, 9, 21, 1]

square_all = map(lambda num: num ** 2, nums)

print(square_all)

# turn the map object into a list
print(list(square_all))