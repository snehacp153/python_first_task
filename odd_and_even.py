even_sum = 0
odd_sum = 0
for i in range(15,36):
    if i % 2 == 0:
        # print(i)
        even_sum = even_sum + i
    else:
        # print(i)
        odd_sum = odd_sum + i

print("sum of even numbers between 15 and 35 are:", even_sum)
print("sum of odd numbers between 15 and 35 are:", odd_sum)