# Use of format for different kind of problem to get a solution:
#W3school pexample:
txt = "For only {price:.2f} dollars!"
print(txt.format(price=float(input("Enter the price : "))))
# Home work:
bro="Avi's monthly salary is {salary_mth:.2f},medical bill {medical_costs:.2f},bus bill {bus:.2f} euro !"
print(bro.format(salary_mth=float(input("Enter salary : ")), medical_costs=float(input("Enter medical costs : ")), bus = float(input("Enter monthly bus bill : "))))



