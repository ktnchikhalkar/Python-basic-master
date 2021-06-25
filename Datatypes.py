Data types and operators in Python
#######Strings###############
#syntax for string is "  string or text " or ' text '

#Accesing Value in Strings    or slicing the values
Name = "Ketan"    #positive and negative formats

 # N i k i t a 
 # 0 1 2 3 4 5
# -5 -4 -3 -2 -1 

Name
print(Name)

print(Name[-6])

Name[3]

print(Name[1:4]) #1,2,3  

print(Name[-1])

print(Name[-3:-1])  #-3,-2
   # Name[-3:]

#Update Strings    

var1 = "Hello World!"
out =  var1 +  ' Python'
print ("Updated  ", var1 + ' Python')


# String Formating 
#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
# %. <number of frations we want>f
#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

print("My name is %s and weight is %.3f kgs! my  father name is %s " % ('Anil', 70,'Ramu'))


############# Hardcoding /Softcoding############

number  = 10  #hardcoding

number = input("enter num:  ") #Softcoding

number_1 = eval(input("enter number: "))

#Ex :1 

Name = input("Enter your name: ")  # string - just input 
Weight = eval(input("Enter your Weight: ")) # int or float
(Name,Weight)

#Triple Quotes

# my name is 'nikhil' and my age is '25'

Statement = """my name is "Ketan" and my age is "28" new"""

Name = "Nikita Salunkhe"
Name.lower() #lower case

Name.center(50)

Name.count("Ketan") # to count

#count() method returns the number of occurrences of the substring in the given string.
string = "My name is Ketan"
substring = "n"

string.count(substring)
count = string.count(substring) # assignment operators

# print count
("The count is:", count)

##Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.

Num = "f1234"  # No space in this string

print(Num.isalnum())

Num = "this is string example"
Num.isalnum() # or .isdigit()

#This method returns true if all characters in the string are alphabetic and there is at least one character, false otherwise.
Num = "this";  # No space & digit in this string
Num.isalpha()

Num = "this is string example0909090!!!";
Num.isalpha()



#This method returns true if all characters in the string are digits and there is at least one character, false otherwise.

Num = "123456";  # Only digit in this string
Num.isdigit()

Num = "this is string example!!!"
Num.isdigit()

#his method returns a copy of the string in which all case-based characters have been lowercased.
Num = "THIS IS STRING EXAMPLE!!!";
Num.lower()

#his method returns a copy of the string in which all case-based characters have been Uppercase.
Num = "this is string example!!!";

alpha = Num.upper()


#The following example shows the usage of replace() method.

reply = "it is string example!!! is really a string"
print(reply.replace("is", "was"))             #.replace   # DF or list or string
reply.replace("is", "was", 1)



#The following example shows the usage of split() method.
split1 = "Line1-abcdef,nLine2-abc,nLine4-abcd"
split1.split(",")

###############################   List   ################################
#collection of elements or items which are ordered
#List is represented by [""] . It is Mutable.

list1 = ['Ketan', 'Nikita', 2020, 2018]
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];

list_n = [list1,list2,list3]



python_class = ["Ketan", "Aditya", "Neel"]


list1 = ['Ketan', 'Nikita', 2020, 2018];

list1[0]


list2 = [1, 2, 3, 4, 5, 6, 7 ];

list2[1:5]

list1 = ['Ketan', 'Nikita', 2020, 2018];
print(list1[2])


list1[2] = 8055;   #updating the list
print(list1)

list1[0] = "Divya";


list1 = ['Ketan', 'Nikita', 2020, 2018];
list1
del(list1[2])   #deleting any item/element by using index number
del(list1)
print(list1)


# Append

aList = [123, 'adi', 'zara', 'omi'] 
aList.append( 2009 ); # adding from last
print(aList)

#Pop

print (aList.pop())  # removing items from the last
print (aList.pop(2))


#Insert
aList.insert( 1, 2008)
print (aList)

aList.insert(2,"gopi")
#Extend

aList = [123, 'xyz', 'tommy', 'abc', 123];
bList = [2009, 'beneli'];
 
aList.extend(bList)   # adding two list

print(aList)

#Reverse

aList.reverse();
print(aList)


#Sort
blist = [8,99,45,33]
blist.sort();
print(blist)

#count
aList = [123, 'xyz', 'zara', 'abc', 123, "zara"];
print(aList.count("zara"))


##################################### Tuples ####################################
# A tuple is represented with :("") . They are immutable are ordered

## Create a tuple dataset
tup1 = ('Street triple','Detona','Beneli', 8055);
tup2 = (1, 2, 3, 4, 5 );
tup3 = ("a", "b", "c", "d");

### Create a empty tuple 
tup1 = ()

#Create a single tuple
tup1 = (50,)

#Accessing Values in Tuples
tup1 = ('Street triple','Detona','Beneli', 8055);
print(tup1[0]);

tup2 = (1, 2, 3, 4, 5, 6, 7 );
print(tup2[1:5]);

#Updating Tuples
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# So,create a new tuple as follows
tup1 = tup1 + tup2;
print(tup1);

#Delete Tuple Elements
tup = ('Street triple','Detona','Beneli', 8055)
print (tup)
del(tup)
print ("After deleting tup : ")
print(tup)

#Basic Tuples Operations

#To know length of the tuple 
tup = (1,2,3,'Ketan','Python')
len(tup)

#To add two elements
tup2 =(4,5,6) 

tup3 = tup+tup2

tup3 = ('Hi!',)

tup3*3


# Membership operator

3 in (1, 2, 3)


# Max and min in tuple
tuple1 = (456, 700, 200)
print(max(tuple1))

print(min(tuple1))



############################## Dictionary #################################
# Used Unordered collection of items
# A dictionary is written : {"key": value}.They are mutable and indexed

#Accessing Values in Dictionary   #keys:values
dict1 = {'Name': 'Ketan', 'Age': 28, 'bike': 'Thunderbird'}
print(dict1)
dict1['Name']
print(dict1['Age'])   
print(dict1['bike'])


##Updating Dictionary
dict1 = {'Name': 'Ketan', 'Age': 28, 'bike': 'Thunderbird'}
dict1['Age'] = 18; # update existing entry
dict1['School'] = "SMK School"; # Add new entry
dict1['Sal'] = 50000;

print(dict1['Age'])
print(dict1['School'])


#Delete Dictionary Elements
dict1 = {'Name': 'Ketan', 'Age': 28, 'bike': 'Thunderbird'}
del(dict1['Name']); # remove entry with key 'Name'
dict1.clear();     # remove all entries in dict
del(dict1) ;        # delete entire dictionary

print(dict1['Age'])
print(dict1['School'])

####################Sets##################

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Adding an item
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Adding multiple items
thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)

print(len(thisset)) #length

#Removing
thisset.remove("banana")
print(thisset)

#Joining to sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)

#Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
print(set3)