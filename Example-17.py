# Program to calculate total amount payable with GST

while True:
    print("\n" + "=" * 50)
    print("        GST Calculator")
    print("=" * 50)

    try:
        # Input from user
        item_name = input("\nEnter item name: ").strip()
        if not item_name:
            print("Item name cannot be empty!")
            continue

        price = float(input("Enter price (in Rs.): "))
        if price < 0:
            print("Price cannot be negative!")
            continue

        gst_rate = float(input("Enter GST rate (%): "))
        if gst_rate < 0:
            print("GST rate cannot be negative!")
            continue

        # Calculate GST and total amount
        gst_amount = (price * gst_rate) / 100
        total_amount = price + gst_amount

        # Display results
        print("\n" + "-" * 50)
        print(f"Item Name:       {item_name}")
        print(f"Original Price:  Rs. {price:.2f}")
        print(f"GST Rate:        {gst_rate}%")
        print(f"GST Amount:      Rs. {gst_amount:.2f}")
        print(f"Total Amount:    Rs. {total_amount:.2f}")
        print("-" * 50)

    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        continue

    # Ask if user wants to continue
    while True:
        choice = (
            input("\nDo you want to calculate for another item? (Yes/No): ")
            .lower()
            .strip()
        )
        if choice in ["yes", "y"]:
            break
        elif choice in ["no", "n"]:
            print("\nThank you for using GST Calculator!")
            exit()
        else:
            print("Please enter 'Yes' or 'No'")
