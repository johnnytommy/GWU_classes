#%%
# print("Hello world!")

#%%[markdown]
# # Sample markdown cell
#
# This is a sample markdown cell.  
# Two spaces in the previous line doesn't make a new line in this environment. 
#
# You will need a blank line to get a new paragraph.

# The above is not considered a blank line without the # sign.
#
# This can get you a [link](http://www.gwu.edu).
#
# You can find some cheatsheets to do other basic stuff like bold-face, italicize, tables, etc.

#%%
# Question 1: Create a Markdown cell with the followings:
# Two paragraphs about yourself. In one of the paragraphs, give a hyperlink of a website 
# that you want us to see. Can be about yourself, or something you like.

#My name is Johnny Thomas; I am from Philadelphia, PA and I am currently
#studying for my Masters of Science in Statistics here at GWU. I did my undergrad
#at Ursinus College in Collegeville, PA. Currently, I work as a Residence Director
#on campus and I oversee the GW residential halls on I Street (Lafayette, Munson & JBKO)
#
#In my free time, I like to hang out with my friends, play trombone, listen to jazz,
#and bother my neighbors. Jazz is awesome and I have a lot of favorite artists, number
#one being Jazz legend Maynard Ferguson. My favorite song is Maynard's 
# [MacArthur Park](https://www.youtube.com/watch?reload=9&v=fC6ykRiQcvA).

#%%
# Question 2: Follow our InClass01.py python file, create
# a list of all the class titles that you are planning to take in the data science program. 
# Have at least 6 classes, even if you are not a DS major
# Then print out the last entry in your list.

classes = ['Introduction to Data Science','Introduction to Data Mining',
            'Machine Learning I','Statistical Data Mining', 'Data Analysis',
            'African Dance']
print(classes)

#%%
# Question 3: After you completed question 2, you feel Intro to data mining is too stupid, so you are going 
# to replace it with Intro to Coal mining. Do that in python here.

classes[1] = "Introduction to Coal Mining"
print(classes)

#%%
# Question 4: Before you go see your acadmic advisor, you are 
# asked to create a python dictionary of the classes you plan to take, 
# with the course number as key. Please do that. Don't forget that your advisor 
# probably doesn't like coal. And that coal mining class doesn't even have a 
# course number.

classDict = {'DATS6101': 'Introduction to Data Science',
             'DATS6103': 'Introduction to Data Mining',
             'DATS6202': 'Machine Learning I',
             'STAT6241': 'Statistical Data Mining', 
             'STAT6216': 'Data Analysis',
             'DANC4412': 'African Dance' }

#%%
# Question 5: print out and show your advisor how many 
# classes (print out the number, not the list/dictionary) you plan 
# to take.

print(len(classes))