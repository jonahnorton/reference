
# https://docs.python.org/3/library/stdtypes.html#range

start = 1
end = 100
step = 2

# range is actually a special object that defines the range of numbers
# but doesn't generate it automatically
myrange = range(start, end, step)
mylist = list(myrange)

print(myrange)
print(mylist)