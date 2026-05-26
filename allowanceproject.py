name = input("Student name: ")
allowance = int(input("Daily allowance: "))
expenses = int(input("Daily expenses:" ))
days = int(input("School days: "))
savings = allowance - expenses

Tlallowance = allowance * days
Tlexpenses = expenses * days
Tlsavings = savings * days

    
print("   Monthly Allowance Report     ")
print ("Name: " + name)
print("Total Allowance:" , Tlallowance)
print("Total Expenses: " , Tlexpenses)
print("Total savings: " , Tlsavings)
print("Averaged Money saved per day: " , savings  )