stop = True
Employee_dict = {}
while(stop):
    print("Enter employee Name type 'no' to stop")
    Name = input()
    if(Name == "no"):
        stop = False
        break
    Salary = input("Enter emplyee salary")
    Employee_dict.update({Name:Salary})
    if Employee_dict:
        print(Employee_dict)