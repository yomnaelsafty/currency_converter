import requests

def get_available_currencies():
    # Use the provided API key to fetch the currencies list
    url = "http://data.fixer.io/api/symbols?access_key=816c44b3b3a9c83ba67450f66b547acc"
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        if "symbols" in data:
            return list(data["symbols"].keys())  # List of available currencies
        else:
            print("The 'symbols' key is missing or not available.")
            return []
    else:
        print(f"Error fetching currency data. Status Code: {response.status_code}")
        print("Response:", response.text)
        return []

def convert_currency(from_currency, to_currency, amount):
    url = f"http://data.fixer.io/api/latest?access_key=816c44b3b3a9c83ba67450f66b547acc&symbols={to_currency}&base={from_currency}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "rates" in data and to_currency in data["rates"]:
            conversion_rate = data["rates"][to_currency]
            converted_amount = amount * conversion_rate
            return converted_amount
        else:
            print("Conversion rate not found.")
            return None
    else:
        print(f"Error fetching conversion data. Status Code: {response.status_code}")
        print("Response:", response.text)
        return None

def main():
    available_currencies = get_available_currencies()
    if not available_currencies:
        print("No currencies available. Exiting.")
        return

    print("Available currencies:")
    for currency in available_currencies:
        print(currency)

    from_currency = input("Enter the 'from' currency: ").upper()
    while from_currency not in available_currencies:
        print("Invalid 'from' currency. Please choose again.")
        from_currency = input("Enter the 'from' currency: ").upper()

    to_currency = input("Enter the 'to' currency: ").upper()
    while to_currency not in available_currencies:
        print("Invalid 'to' currency. Please choose again.")
        to_currency = input("Enter the 'to' currency: ").upper()

    try:
        amount = float(input("Enter the amount to convert: "))
        while amount <= 0:
            print("Amount must be greater than zero. Please try again.")
            amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Invalid amount entered. Exiting.")
        return

    converted_amount = convert_currency(from_currency, to_currency, amount)
    if converted_amount is not None:
        print(f"The amount {amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")

if __name__ == "__main__":
    main()

