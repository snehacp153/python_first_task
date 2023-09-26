employee_id = int(input("enter the employee id:"))
employee_name = input("enter the employee name:")
basic_pay = int(input("enter the basic salary:"))

if basic_pay > 10000 :
    HRA = basic_pay * 15/100
    DA = basic_pay * 8/100
    net_pay = HRA + DA + basic_pay

elif basic_pay < 5000 and basic_pay >10000 :
    HRA = basic_pay * 10/100
    DA = basic_pay * 5/100
    net_pay = HRA + DA + basic_pay

elif basic_pay < 10000:
    HRA = basic_pay * 5/100
    DA = basic_pay * 3/100
    net_pay = HRA + DA + basic_pay
    
print("HRA is:",HRA)
print("DA IS:",DA)
print("Total net salary is :",net_pay)