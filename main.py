# Use of format for different kind of problem to get a solution:
#W3school pexample:
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
# Home work:
bro="Avi´s monthly salary is {salary_mth:.2f},medical bill {medical_costs:.2f},bus bill {bus:.2f} euro !"
salary_mth=input("Enter salary : ")
medical_costs=input("Enter medical costs : ")
bus = input("Enter monthly bus bill : ")
print(bro.format(salary_mth, medical_costs, bus))



