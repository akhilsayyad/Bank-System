import tkinter as tk

def generate_report():
    principal = float(entry_principal.get())
    rate = float(entry_rate.get())
    time = float(entry_time.get())
    
    rate = rate / 12 / 100  # converting annual rate to monthly and to decimal
    time = time * 12  # converting years to months
    
    emi = principal * rate * (1 + rate) ** time / ((1 + rate) ** time - 1)
    total_payable = emi * time
    total_interest = total_payable - principal
    
    report = (
        f"Principal Amount: {principal}\n"
        f"Interest Rate: {rate * 12 * 100}%\n"
        f"Loan Tenure (years): {time / 12}\n"
        f"Your EMI per month will be: {emi:.2f}\n"
        f"Total Payable Amount: {total_payable:.2f}\n"
        f"Total Interest Paid: {total_interest:.2f}"
    )
    
    output_label.config(text=report)


root = tk.Tk()
root.title("Loan Report Generator")

# Input fields
tk.Label(root, text="Principal Amount:").pack()
entry_principal = tk.Entry(root)
entry_principal.pack()

tk.Label(root, text="Interest Rate (% per annum):").pack()
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Loan Tenure (years):").pack()
entry_time = tk.Entry(root)
entry_time.pack()

# Button to generate report
generate_button = tk.Button(root, text="Generate Report", command=generate_report)
generate_button.pack()

# Output label to display the report
output_label = tk.Label(root, text="")
output_label.pack()

# Start the main loop
root.mainloop()
