#Write a program to ask for a purchase amount and the number of installments
#Add 5 percent to then amount as interest
#Get the nett amount and divide by the number of installments requested
#Finally, display the purchase amount cum interest and installments amount

amount_purchase = float(input("Enter amount purchased: "))
number_of_payment_installment = int(input("Enter number of payment installment: "))

percent_added = 0.05

total_amount_purchased = amount_purchase * (1 + percent_added)

installment = total_amount_purchased / number_of_payment_installment

print(f"Purchase amount: ${total_amount_purchased:.2f} ")
print(f" Nett purchased: ${total_amount_purchased:.2f}")
print(f"Total amount installment: ${installment:.2f}")