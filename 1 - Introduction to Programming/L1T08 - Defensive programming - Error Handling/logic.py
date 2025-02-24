# This program displays a tenants invoice. However when the code is run for the desired Tenant, 
# it doesnt print the tenants name correctly.The program however still runs in the terminal.

# Fix the code so that it displays the correct name of the tenant.

def display_invoice(username, amount, due_date):
 print(f"Hello username")  # Logical Error: Missing curly brackets for username
 print(f"The amount due is {amount}")
 print(f"The due date is {due_date}")

display_invoice("Joe", 100, "2025-03-24")
