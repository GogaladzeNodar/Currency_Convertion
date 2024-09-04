from Config import conversion_rates

def convert_currency(amount, from_currency, to_currency):
    rate = conversion_rates[from_currency][to_currency]
    return amount * rate