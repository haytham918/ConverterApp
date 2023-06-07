import requests
import pprint

convertURL = "http://data.fixer.io/api/convert"
symbolsURL = "http://data.fixer.io/api/symbols"
latestURL = "http://data.fixer.io/api/latest"
flagURL = "https://www.countryflags.io/"

symbols_params = {"access_key": "0ccba43ed82b96bca5e8206f5f1f094a"}
symbol_response = requests.get(symbolsURL, symbols_params)
symbol_response.raise_for_status()
symbol_response = symbol_response.json()
kinds_currency = symbol_response["symbols"]
abb = kinds_currency.keys()
abb = list(abb)
total_name = kinds_currency.values()
total_name = list(total_name)
options_currency = {}
string = ""

for i in range(len(abb)):
    options_currency[abb[i] + "(" + total_name[i] + ")"] = abb[i]

for s in options_currency.values():
    string = string + f"{s},"

first_params = {
    "access_key": "0ccba43ed82b96bca5e8206f5f1f094a",
    "symbols": string
}
first_response = requests.get(latestURL, first_params)
first_response.raise_for_status()
first_response = first_response.json()
all_rates = first_response["rates"]

# print(rates)


def currency_conversion(before, after, amount):
    first_rate = all_rates[before]
    second_rate = all_rates[after]
    rate = second_rate / first_rate
    get = amount * rate
    value = {"Rate": f"1 : {rate}", "Amount": get}
    return value


def choose_flag(a, country_code):
    if country_code[0] != "x":
        if country_code[:2] == "eu":
            a.set_source(
                "https://cdn.pixabay.com/photo/2013/07/13/01/09/european-union-155207_960_720.png"
            )
        else:
            if country_code[:3] == "btc":
                a.set_source(
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdcdgYath_Xgz17FT5XVe-0N88lYW36IR2WumOSe5a9vPJl6N2"
                )
            else:
                a.set_source(f"{flagURL}{country_code[:2]}/flat/64.png")
    else:
        a.set_source(
            "https://user-images.githubusercontent.com/505739/34508579-1d3b7f8a-f00f-11e7-98e4-2edd02ee3465.png"
        )


def check_currency(a, b, c):
    if a == "" or b == "" or c == "":
        return False
    else:
        return True