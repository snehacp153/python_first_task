length = int(input("enter the length in cm:"))
if length <= 0 :
    print("the length is invalid")
else:
    # convert into inches 
    length = length / 2.54
    print("length in inches is:",length)