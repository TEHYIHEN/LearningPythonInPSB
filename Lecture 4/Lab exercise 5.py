# At one college, the tuition for a full-time student is $8,000 per semester.
# It has been announced that the tuition will increase by 3 percent each year for the next 5 years.
# Write a program with a loop that displays the projected semester tuition amount for the next 5 years.

INCREMENT_RATE = 0.03  # rate is fixed
num_periods = 10
fees = 10000

for i in range(1, num_periods+1):
    fees = fees * (1 + INCREMENT_RATE)
    print(f"Fees for year {i}: ${fees:,.2f}")   #print 2 decimals with commas for thousand places

print("----------------")