print("Hello world!")
print(5 / 8)
print (7+10)
print("HELLO!")
#%%[markdown]
#
# # Python Class 01
# 
# This is our first class of the semester.
# Hello to everyone.   
# Two spaces in the previous line doesn't make a new line in this environment. 
#
# You will need a blank line to get a new paragraph.

# The above is not considered a blank line without the # sign.
#
# This can get you a [link](http://www.gwu.edu).
#
# You can find some cheatsheets to do other basic stuff like bold-face, italicize, tables, etc.

#%%
# # Four basic data type 
# BIFS - boolean, integer, float, string

abool = True    # boolean
aboolstr = "True"     # str
azero = 0    # int
aint = 35    # int
aintstr = "35"     # str
afloat = -2.8     # float
afloatstr = "-2.8"     # str
anumbzerostr = "0"     # str
aemptystr = ""     # str
aletter = 'a'     # str
astr = "three-five"     # str

#%%
# higher level data types (class)
# list / array
alist = [1,'person',1,'heart',10,'fingers']

# tuple # like list, but immutable (faster access and processing)
atuple = (1,'person',1,'heart',10,'fingers')

# set  # un-ordered, and distinct elements.  
aset = { 1,'person',1,'heart',10,'fingers' }
  #Sets are distinct elements

#%%
# dictionary # like associative array in other lang.  
# The list is not indexed (by integers), but reference by a key.
# The key must be a primitive data type
adictionary = { "name": "Einstein", 1: "one", "love": 3.14159 }
# access elements with 
adictionary['love']

#%%
# This kind of works too?! 
# Also kind of strange to use float and bool as key though, but it is possible and you might find it reasonable in certain situations.
adictionary2 = { "name": "Einstein", 1: "one", 3.14: 3.14159, True: 'love', "last": alist }
print(adictionary2)
print(type(adictionary2["last"]))
print(len(adictionary2))

#%%
# ######## BUT BE VERY CAREFUL if you use bool and float. They might not be what you expect.
adictionary3 = { "name": "Einstein", 2: "two", 3.14: 3.14159, True: 'loves', "last": alist }
print(adictionary3)
print(len(adictionary3))
adictionary4 = { "name": "Einstein", 2: "two", 2.0: 3.14159, True: 'loves', "last": alist }
print(adictionary3)
print(len(adictionary3))
# below does not work. you can try by uncommenting it and run the line code
# notadicationary = { ['a',2]: "sorry", {1,2}: ('not','ok') }

#%%
# ###################  1. Exercise    Exercise    Exercise   ################################## 
# Try to create some more complicated entities. List of tuples, dictionary of dictionary, see if you find anything unexpected. 
print("This is exercise 1")




#%%
# ###################  2. Exercise    Exercise    Exercise   ################################## 
# Implicit conversion, which is also called coercion, is automatically done. (different lang has different coercion rules.)
# Explicit conversion, which is also called casting, is performed by code instructions.
print("This is exercise 2")


#%%
# Example, try 
int(abool)
str(abool)
str(int(abool))
# int(str(abool))

#%%
# Try it yourself, using the functions bool(), int(), float(), str() to convert. 
# what are the ones that you surprises you? List them out for your own sake




#%% 
# ####################  3. Exercise - binary operations:  ################################## 
# try to add or multiply differnt combinations and see the result. 
# Show your work here
print("This is exercise 3")

# Example -- implicit conversion is automatic here
add_bool_zero = abool + azero
print('result: type= ' + str(type(add_bool_zero)) + ' , value= ' +str(add_bool_zero) )



#%%
# ####################  4. Exercise - copying/cloning/deep cloning/shallow copy  ################################## 
# copy vs reference 
print("This is exercise 4")
cbool = abool
abool = False
print(abool)
print(cbool)
#do the same for the four differnt types


#%%
# ####################  Next, try it on tuple, list, set, dictionary ####################
ctuple = atuple
ctuple = (1,'person','2','hearts', 6 , 'fingers')
print(atuple)
print(ctuple)

#%%
# notice that tuples cannot assign a new value individually like atuple[1]='guy', but you can reassign the entire variable
clist = list(alist)
clist = alist[:]
# clist = alist
clist[2]=2
clist[3] = 'hands'
print(alist)
print(clist)
# Is it what you expect??

#%%
# Now try the other data types: set, dictionary, set of dictionaries, list of tuples, 
# etc etc
# These are shallow copies. They just copy the reference address, not the (primitive) values. 
# How do we make static clones that are no longer tied?
# Try google
# Does that work for deep level objects like list of dictionaries?

len(adictionary3)


# Logical operators
# and or not
# logic boolean operator
# 