def predict_profit():
    while True:
        try:
            sales = float(input("Enter the sales amount: "))
            if sales < 0:
                print("Sales amount cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for sales.")
    profit = sales * 0.23
    print (f"The predicted profit is: ${profit:.2f}")
print(predict_profit())

