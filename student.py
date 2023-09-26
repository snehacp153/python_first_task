maths = int(input("enter the mark:"))
physics = int(input("enther the mark:"))
chemistry = int(input("enter the mark:"))
english = int(input("enter the mark:"))
malayalam = int(input("enter the mark:"))
IT = int(input("enter the mark:"))

Total_mark = maths + physics + chemistry + english + malayalam + IT
avg_mark = Total_mark / 6
# print(Total_mark)
# print(avg_mark)
if avg_mark > 90 :
    print("grade is A")

elif avg_mark < 90 and avg_mark > 70 :
    print("grade is B")

elif avg_mark < 70 and avg_mark > 50 :
    print("grade is C")

elif avg_mark < 50 and avg_mark > 30 :
    print("grade is D")

else:
    print("FAIL")




