
# print without newline
print('string', end="")


#print a range of numbers ( not including 5) 
for number in range(1, 5):
  print(number)

# print   
print("Print", "strings", "with", "white", "spaces")


def print_string_formatted():
    print("%-40s\t%-15s" %  ("Item", "Price"))
    print("%-40s\t%-15s" % ("Fuji Apple", "$3.00"))
    print("%-40s\t%-15s" % ("Watermelon", "$5.00"))
