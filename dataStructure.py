#!/usr/bin/python

my_list = [1, 2, 3, "this", "is", "python list"]
print my_list
for i in range(len(my_list)):
    print "%d:" % i, my_list[i]

my_dict = {
        "apple" : 10,
        "pear" : 4,
        "banana" : 8
        }
print my_dict
for key,value in my_dict.items():
    print "%s : %s" % (key, str(value))
