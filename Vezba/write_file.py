try: 
    employee_file = open("Employees.txt", "a")
    print(employee_file.write("Toby - Human Resources"))
    employee_file.close
except:
    print ("Podatak je upisan u tekstu  ")
