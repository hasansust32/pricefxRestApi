#
#
# sourcefile = open('demo.text', 'w')
# print("hello Hasan, this is file in python " , file= sourcefile)
# print("Hello Babor , this is file operator" , file = sourcefile )
# sourcefile.close()


import sys

# Saving the reference of the standard output
original_stdout = sys.stdout

with open('demo1.txt', 'w') as f:
    sys.stdout = f
    print('Hello, Python!')
    print('This message will be written to a file.')
    # Reset the standard output
    sys.stdout = original_stdout
