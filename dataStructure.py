#!/usr/bin/python

# list
my_list = [1, 2, 3, "this", "is", "python list"]
print '--------------------'
print my_list
for i in range(len(my_list)):
    print "%d:" % i, my_list[i]

# dict
my_dict = {
        "apple" : 10,
        "pear" : 4,
        "banana" : 8
        }
print '--------------------'
print my_dict
for key,value in my_dict.items():
    print "%s : %s" % (key, str(value))

# tuple
my_tuple = ('a', 'b', 1, 2)
print '--------------------'
print my_tuple
print my_tuple[1:3]
