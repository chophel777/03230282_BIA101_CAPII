class Citizen: #  defines a class named Citizen with an initializer method (__init__).
    def __init__(self, identity, earnings, employment, organization): # The initializer takes four parameters: identity, earnings, employment, and organization.
        # These parameters are then assigned to instance variables of the same names within the class.
        self.identity = identity
        self.earnings = earnings
        self.employment = employment
        self.organization = organization

    def evaluate_tax(self):
        deductions = self.compute_deductions() # The evaluate_tax method calculates tax deductions by calling compute_deductions.

        # Calculate taxable_earnings by subtracting deductions from total earnings.
        taxable_earnings = self.earnings - deductions

        # calculate tax by calling method assess_tax_rate, passing taxable_earnings as an argument, and assign result to the variable tax.
        tax = self.assess_tax_rate(taxable_earnings)

        # Apply bonus if necessary
        if tax >= 1000000:
            tax += tax * 0.10

        return tax # This will return the value to the tax.
    
    def compute_deductions(self):
        deductions = 0 # It initialize the variable deductions to 0, preparing it for further calculations.

        # Health insurance deduction
        if self.employment == 'Ordinary' and self.organization != 'Public': # Check if the type of employment is ordinary and the organization is not public.
            deductions += 0.10 * self.earnings # If the conditions are met, increase deductions by 10% of earnings.

        # Pension deduction (NPPF)
        if self.employment == 'Ordinary': # Check if the type of employment is Ordinary.
            deductions += 0.05 * self.earnings # If it is, apply a deduction of 5% of earnings.

        # Professional development deduction
        deductions += 350000 # Adding a deductions of 350000 for professional development expenses.

        # Additional deductions
        deductions += 0.30 * self.earnings # It calculates additional deductions based on a 30% of the earnings.

        return deductions # This will return the value to the deductions of the citizens.

    def assess_tax_rate(self, taxable_earnings): # Define a function assess_tax_rate based on taxable earnings.
        if taxable_earnings <= 300000: # If earnings are less than or equals to 300000, no tax.
            return 0
        elif taxable_earnings <= 400000: # If earnings are less than or equals to 400000, apply 10% tax rate.
            return taxable_earnings * 0.10
        elif taxable_earnings <= 650000: # If earnings are less than or equal to 650000, apply 15% tax rate.
            return taxable_earnings * 0.15
        elif taxable_earnings <= 1000000: # If earnings are less than or equal to 1000000, apply 20% tax rate.
            return taxable_earnings * 0.20
        elif taxable_earnings <= 1500000: # If earnings are less than or equal to 1500000, apply 25% tax rate.
            return taxable_earnings * 0.25
        else:
            return taxable_earnings * 0.30 # For those who earns more than 1500000, apply 30% tax rate.


def start():
    try:
        identity = input("Enter your name: ") # Asking the user to enter their name.
        earnings = float(input("Enter your income: ")) # Prompting the user to enter their income.
        employment = input("Enter employment type (Ordinary/Contractual): ") # Asking the user to enter their type of employment.
        organization = input("Enter organization type (Public/Private/Corporate): ") # Asking the user to enter the organozation they work.

        citizen = Citizen(identity, earnings, employment, organization) # # Define a class named Citizen with attributes: identity, earnings, employment, organization.

        if earnings < 300000: # # It checks if the earnings of the citizen is less than 300000.
            print("This individual is exempt from tax payment.") # If earnings are below the 300000, the person is exempted from paying tax.
        else:
            tax = citizen.evaluate_tax() # # If earnings are above the threshold, call the evaluate_tax method of the Citizen class to calculate tax.
            print(f"{identity} need to pay Nu {tax:.2f} as taxes.") # # Print the amount of tax the citizen needs to pay, formatted to two decimal places.

    except ValueError: # Handle any ValueError exceptions that might occur during the execution of the code.
        print("Invalid input. Please provide a valid earnings value.") # Print a message indicating that the input earnings value is invalid


if __name__ == "__main__": # This line checks if the current module is being run as the main program. If the conditions are fulfilled the code will be executed.
    start() # Call the function start() to begin the main execution.
