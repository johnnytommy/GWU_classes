print("VS Code - User Input check")

# Complication with VS Code (current version 1.38.0) 
# To use input
# you CANNOT use interactive window, instead, you can run it this way:
# 
# You can run the entire file using "Run Python file in Terminal"
# Make sure your terminal session is in shell mode ( /User/directory$ ), not the python mode ( >>> )
# if the terminal is in python mode, type exit() or Ctrl-D to exit
# 
# Note that Runing the chunk using "Run Selection/Line in Python Terminal" does not work neither.
# You also need to be aware that to "Run Selection/Line in Python Terminal", 
# the terminal should be in python mode ( >>> ). 
# If it is in shell mode, type "python3". (type python will use python 2.7 or other configured version according to your system)

try:
  inp1 = input("Enter a value: ")
except:
  inp1 = 'exception hello'
finally:
  # I usually put some data/input integrity checks here before moving on
  inp1 = 'changed to default' if not inp1 else 'VSCode+iPython error' if (inp1=='exception hello') else inp1

print('This is input1:',inp1)

# By putting the input function inside the try block, all these will also run under 
# interactive python window without error
# you just cannot have user interactivity via the terminal

