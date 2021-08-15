loan_amt = float(input("Wartość początkowa kredytu [PLN]:"))
loan_rate = float(input("Oprocentowanie kredytu [%]:"))
loan_emi = float(input("Kwota raty kredytu [PLN]:"))

# January
inflation = 1.59282448436825
loan_amt_new = (1 + ((inflation + loan_rate) / 1200)) * loan_amt - loan_emi
loan_amt_diff = loan_amt - loan_amt_new
print(f"Twoja pozostała kwota kredytu to {loan_amt_new} PLN, to {loan_amt_diff} PLN mniej niż w poprzednim miesiącu.")
loan_amt = loan_amt_new

# February
inflation = -0.453509101198007
loan_amt_new = (1 + ((inflation + loan_rate) / 1200)) * loan_amt - loan_emi
loan_amt_diff = loan_amt - loan_amt_new
print(f"Twoja pozostała kwota kredytu to {loan_amt_new} PLN, to {loan_amt_diff} PLN mniej niż w poprzednim miesiącu.")
loan_amt = loan_amt_new