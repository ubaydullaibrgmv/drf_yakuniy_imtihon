import requests


def get_cbu_rates():
    url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
    try:
        response = requests.get(url)
        data = response.json()

        rates = {'UZS': 1.0}
        for item in data:
            if item['Ccy'] in ['USD', 'EUR']:
                rates[item['Ccy']] = float(item['Rate'])
        return rates
    except Exception:
        return {'UZS': 1.0, 'USD': 12900.0, 'EUR': 14100.0}