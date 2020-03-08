def main():

    print('hello world')

    for i in range(0,4):
        print(i)
    # VARIABLES
    my_int = 10
    my_string = "hello world"
    my_float = 33333.145656
    my_bool = True
    MY_CONSTANT = 3.145

    # Print 
    # %s - String (or any object with a string representation, like numbers)
    # %d - Integers
    # %f - Floating point numbers
    # %N.Pf   number of characters to show used to add spacing before number
    #  , p precision number of digits to right of decimal point
    # %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
    # %x/%X - Integers in hex representation (lowercase/uppercase)
    print("hello world")
    print("my_int - %d my_string - %s my_float - %.4f" % (my_int, my_string, my_float))
    print(my_int)
    print("%s bool" % my_bool)

    # print format
    print("hello {0}, our balance {1:15.3f}".format(my_string, my_float))
    print("hello {name}, our balance {num:9.3f}".format(name=my_string, num=my_float))
    print("hello {name}, our balance {num}".format(name=my_string, num=my_float))
    print("hello {}, our balance {}".format(my_string, my_float))
    print("hello  {0!s}, our balance {1}".format(my_int, my_float))

    print("""
        _____ ___ 
        /___|/| / |/ || //|| //|/| ||_/___| //|__/|
        ||_|| // ||
        \_____/ /_/ _____ _ / _ \||
        // /_/
        ||__| ||||___ |
        """
    )
    # Comments - this is a comment
    #
    # no real multi link comments /* */ does not work
    """
        this is a hack but it works
        multi line comment
    """

    # LISTS
    list1 = ['physics', 'chemistry', 1997, 2000]
    list2 = [1, 2, 3, 4, 5 ]
    list3 = ["a", "b", "c", "d"]

    # list slcices
    print('list slices')
    
    print ("list1[0]: ", list1[0])
    print ("list2[1:5]: ", list2[1:5])
    print ("list3[1:-2]: ", list3[1:-2])
    print('reverse list')
    print(list1[::-1])

    list4 = [1] * 3
    print("list4 ", list4)

    list = ['physics', 'chemistry', 1997, 2000]
    print ("Value available at index 2 : ", list[2])

    list[2] = 2001
    print ("New value available at index 2 : ", list[2])

    # deletes item from list
    del list[2]
    print ("After deleting value at index 2 :    del list[2] ", list)
    print("len of array len(list1): ", len(list1))
    print("[1, 2, 3] + [4, 5, 6]", [1, 2, 3] + [4, 5, 6])

    # check if item is in list
    print(" 3 in [1, 2, 3]", 3 in [1, 2, 3])

    print('\n')
    list2.append(1)
    print("list2.append(1) ", list2)

    # count
    aList = [123, 'xyz', 'zara', 'abc', 123]

    print ("Count for 123 : ", aList.count(123))
    print ("Count for zara : ", aList.count('zara'))
    
    #Remove by value
    list1 = ['physics', 'Biology', 'chemistry', 'maths']
    print(list1)
    print ("remove biology : ", list1.remove('Biology'))
    print ("list now : ", list1)
    print ("remove maths : ", list1.remove('maths'))
    print ("list now : ", list1)


    # Fill a list
    numbers = [i for i in range(10)]    
    print(numbers)

    #loop through list
    print('loop through array')
    for x in [1,2,3]: 
        print (x,end = ' ')

    #loop range function
    print('for i in range(5):')
    for i in range(5):
        print(i)

    print('for i in range(3,6):')
    for i in range(3,6):
        print(i)

    print('for i in range(0, -10, -2):')
    for i in range(0, -10, -2):
        print(i)

    print('for i in range(10, 0, -2):')
    for i in range(10, 0, -1):
        print(i)

    # DICTIONARY
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    print ("dict['Name']: ", dict['Name'])
    print ("dict['Age']: ", dict['Age'])

    #edti and add entry
    dict['Age'] = 8 # update existing entry
    dict['School'] = "DPS School" # Add new entry

    print ("dict['Age']: ", dict['Age'])
    print ("dict['School']: ", dict['School'])
    print(dict)

    nodes = {0: None, 1: None}
    
    number = 3
    nodes[0] == nodes[0] or print('got here')
    print(bool(nodes[0] == nodes[0]))




if __name__ == '__main__':
    main()
    