def generate_loan_report(principal, rate, time):
    # Convert rate from annual to monthly and time to months
    rate = rate / 12 / 100  # converting annual rate to monthly and to decimal
    time = time * 12  # converting years to months
    
    # Calculate EMI
    emi = principal * rate * (1 + rate) ** time / ((1 + rate) ** time - 1)
    
    # Calculate total payable amount
    total_payable = emi * time
    
    # Calculate total interest paid
    total_interest = total_payable - principal
    
    report = {
        "Principal Amount": principal,
        "Interest Rate": rate * 12 * 100,  # converting back to annual and percentage
        "Loan Tenure (years)": time / 12,  # converting back to years
        "EMI": emi,
        "Total Payable Amount": total_payable,
        "Total Interest Paid": total_interest
    }
    
    return report

# Example usage
loan_amount = 100000  # Principal amount
annual_interest_rate = 10  # Annual interest rate in percentage
loan_tenure_years = 5  # Loan tenure in years

loan_report = generate_loan_report(loan_amount, annual_interest_rate, loan_tenure_years)

# Displaying the report
print("Loan Report:")
for key, value in loan_report.items():
    print(f"{key}: {value}")
