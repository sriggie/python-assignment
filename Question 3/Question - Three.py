# Part a: Write an algorithm for the scenario
# Initialize a variable total_cost to 0 to keep track of the total cost of items sold.
# Start a loop that runs until the shop attendant decides to stop:
# Ask the shop attendant to enter the item ID, item name, quantity, and unit price.
# Calculate the cost of the items sold by multiplying the quantity by the unit price.
# Calculate the VAT (Value Added Tax) by multiplying the cost by 0.16 (16%).
# Add the VAT to the cost to get the final cost of the items sold.
# Add the final cost to the total_cost.
# Ask the shop attendant if they want to process another transaction. If not, exit the loop.
# Print the total_cost.


# Part b: Design this application using a flow chart
# Here is a flowchart representing the algorithm:


                                    #       +--------+
                                    #       | Start  |
                                    #       +--------+
                                    #            |
                                    #            v
                                    #       +--------+
                                    # +---->| Prompt |
                                    # |     +--------+
                                    # |          |
                                    # |          v
                                    # |     +--------+
                                    # +---->|   End  |
                                    #       +--------+
                                    #            |
                                    #            v
                                    #       +--------+
                                    #       | Prompt |
                                    #       +--------+
                                    #            |
                                    #            v
                                    #       +--------+
                                    #       |Prompt  |
                                    #       |itemID, |
                                    #       |itemName|
                                    #       |quantity|
                                    #       |unitPrice|
                                    #       +--------+
                                    #            |
                                    #            v
                                    #       +--------+
                                    #       | Calculate cost
                                    #       +--------+
                                    #            |
                                    #            v
                                    #       +--------+
                                    #       | Calculate VAT
                                    #       +--------+
                                    #            |
                                    #            v
                                    #       +--------+
                                    #       | Calculate total cost
                                    #       +--------+
                                    #            |
                                    #            v
                                    #       +--------+
                                    #       |  Add total cost to grand_total
                                    #       +--------+
                                    #            |
                                    #            v
                                    #       +--------+
                                    #       |Prompt the customer to pay
                                    #       |for the cost and enter
                                    #       |the amount paid
                                    #       +--------+
                                    #            |
                                    #            v
                                    #       +--------+
                                    #       |Calculate the change
                                    #       +--------+
                                    #            |
                                    #            v
                                    #       +--------+
                                    #       |Print the receipt
                                    #       +--------+
                                    #            |
                                    #            v
                                    #       +--------+
                                    #       | Continue? |
                                    #       +--------+
                                    #            |
                                    #            v
                                    #       +--------+
                                    #       |  Print grand_total
                                    #       +--------+
                                    #            |
                                    #            v
                                    #       +--------+
                                    #       |   End  |
                                    #       +--------+

#  part C ->  implementing the code using python code 

grand_total = 0

while True:
    itemID = input("Enter item ID (or 'q' to quit): ")
    if itemID == 'q':
        break

    itemName = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    unitPrice = float(input("Enter unit price: "))

    cost = quantity * unitPrice
    vat_amount = 0.16 * cost
    total_cost = cost + vat_amount

    print("Cost: $", cost)
    print("VAT: $", vat_amount)
    print("Total Cost: $", total_cost)

    amount_paid = float(input("Enter amount paid: "))
    change = amount_paid - total_cost

    print("Receipt:")
    print("Item ID:", itemID)
    print("Item Name:", itemName)
    print("Quantity:", quantity)
    print("Unit Price:", unitPrice)
    print("Cost:", cost)
    print("VAT:", vat_amount)
    print("Total Cost:", total_cost)
    print("Amount Paid:", amount_paid)
    print("Change:", change)

    grand_total += total_cost

print("Grand Total: $", grand_total)
