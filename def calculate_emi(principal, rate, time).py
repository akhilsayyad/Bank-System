def calculate_emi(principal, rate, time):
    # Convert rate from annual to monthly and time to months
    rate = rate / 12 / 100  # converting annual rate to monthly and to decimal
    time = time * 12  # converting years to months
    
    # EMI formula calculation
    emi = principal * rate * (1 + rate) ** time / ((1 + rate) ** time - 1)
    
    return emi

# Example usage
loan_amount = 100000  # Principal amount
annual_interest_rate = 10  # Annual interest rate in percentage
loan_tenure_years = 5  # Loan tenure in years

emi = calculate_emi(loan_amount, annual_interest_rate, loan_tenure_years)
print(f"Your monthly EMI: {emi:.2f}")
