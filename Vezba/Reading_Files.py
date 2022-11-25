# Reading a external file with the code of python
try:
    employee_file = open ("Employees.txt" , "r")
    print(employee_file.readlines() [4])
    employee_file.close()

except:
    print ("Nije moguce citanje fajla")