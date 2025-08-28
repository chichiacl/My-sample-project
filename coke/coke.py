amount_due = 50
print("Amount Due: 50")
while True :
    insert_amount = input("Insert Amount: ")
    if insert_amount in ["25","10","5"]:
        amount_due = amount_due - int(insert_amount)
        if amount_due > 0:
            print("Amount Due:", amount_due)
        elif amount_due < 0:
            print("Change Owed:", abs(amount_due))
            break
        else:
            print("Change Owed:",amount_due)
            break
    else:
         print("Amount Due:", amount_due)
