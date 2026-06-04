# Predefined stock prices

stock_prices = {
    "TCS": 3500,
    "Infosys": 1500,
    "Wipro": 450,
    "HCL": 1200
}

portfolio = {}

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock name: ")
    quantity = int(input("Enter quantity: "))
    portfolio[stock] = quantity

total_value = 0

print("\nPortfolio Summary:")

for stock, quantity in portfolio.items():
    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        total_value += value
        print(stock, ":", quantity, "shares =", value)

print("\nTotal Portfolio Value =", total_value)
