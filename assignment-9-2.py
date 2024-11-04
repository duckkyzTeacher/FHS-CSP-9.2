def testHeader(functionToTest):
    print(f"Tests for {functionToTest}:")

# 1. Write a function called 'print_name' that takes one parameter, a name, and prints it.
#    Call the function with different names.


testHeader("print_name")
#Test Cases
print(f"\t{print_name('Finn') = }")
print(f"\t{print_name('Jake') = }")
print(f"\t{print_name('BMO') = }")
print(f"\t{print_name('Bonabell') = }")
print(f"\t{print_name('Marcie') = }\n\n\n")


# 2. Write a function called 'subtract' that takes two parameters, a and b,
#    and returns their difference (a - b). 



testHeader("subtract")
#Test Cases
print(f"\t{subtract(1,2) = }")
print(f"\t{subtract(1,0) = }")
print(f"\t{subtract(1,99) = }")
print(f"\t{subtract(50,10) = }\n\n\n")



# 3. Write a function called 'greet_people' that takes multiple names as arguments using *args,
#    and prints a greeting for each name. For example, calling greet_people("Alice", "Bob") should print:
#    "Hello, Alice" and "Hello, Bob".



testHeader("greet_people")
#Test Cases
print(f"\t{greet_people('Jeff', 'Britta', 'Abed', 'Troy', 'Annie', 'Shirley', 'Pierce') = }")
print(f"\t{greet_people('Lilo', 'Stitch') = }")
print(f"\t{greet_people('Jim') = }")
print(f"\t{greet_people('R', 'A', 'D') = }\n\n\n")


# 4. Write a function called 'calculate_total' that takes a list of prices as a parameter
#    and returns their sum. Demonstrate calling the function with a list of values.




testHeader("calculate_total")
#Test Cases
print(f"\t{calculate_total(1,2) = }")
print(f"\t{calculate_total(1) = }")
print(f"\t{calculate_total(*range(1,100)) = }")
print(f"\t{calculate_total(99, 60, 40, 23, 34, 234, 1, 3) = }\n\n\n")



# 5. Write a function called 'calculate_total_tax' to accept an additional optional parameter 'tax_rate',
#    which adds a tax to the total (default value of tax_rate is 0.05 or 5%).
#    If no tax_rate is provided, it should calculate with the default rate.




testHeader("calculate_total_tax")
#Test Cases
print(f"\t{calculate_total_tax(1, 2, tax_rate = 0.1) = }")
print(f"\t{calculate_total_tax(1, tax_rate = 0.75) = }")
print(f"\t{calculate_total_tax(*range(1,100)) = }")
print(f"\t{calculate_total_tax(99, 60, 40, 23, 34, 234, 1, 3, tax_rate = 0.0) = }\n\n\n")



# 6. Write a function called 'combine_strings' that takes any number of strings as arguments using *args
#    and concatenates them together into one single string. Test it with different numbers of strings.




testHeader("combine_strings")
#Test Cases
print(f"\t{combine_strings('chicken') = }")
print(f"\t{combine_strings('chicken', 'rice') = }")
print(f"\t{combine_strings('steamy', 'chicken', 'rice') = }\n\n\n")
print(f"\t{combine_strings('sweet', 'sour', 'savory', 'steamy', 'fresh', 'pork', 'boa') = }")