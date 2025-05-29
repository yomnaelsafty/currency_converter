import requests

init_currency = input("Enter an initial currency: ")
target_currency = input("Enter an target currency: ")

while True:
    try:
        amount = float(input("Enter the amount: "))
    except:
        print("The amount must be numberical value!")
        continue
    if amount == 0:
        print("The amount must be greater than 0 ")
        continue
    else:
        break

url = (f"https://api.apilayer.com/currency_data/convert?to={target_currency}&from={init_currency}&amount={amount}")

payload = {}
headers= {
  "apikey": "SX0XFgEX4MWPUL3Mu2rN2yNZTdnHuWCw"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
if status_code != 200:
    print(" Sorry, there was aproblem please try again later")
    quit()

result = response.json()
coverted_corrency = result['result']

print(f"{amount}{init_currency} = {coverted_corrency}{target_currency}")
