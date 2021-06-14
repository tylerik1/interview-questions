import requests

def get_ticker_page(symbol):
    url = 'https://money.cnn.com/quote/forecast/forecast.html?symb=' + str(symbol)

    r = requests.get(url)

    if (f'Your search for &ldquo;<strong>{symbol.upper()}</strong>&rdquo; was not found') in r.text:
        return None, None, None, None


    price = float(r.text.split('wsod_last')[1].split('>')[2].split('<')[0])


    if 'There is no forecast data available' in r.text:
        return price, None, None, None

    high = float(r.text.split('high estimate of ')[1].split(' ')[0])
    median = float(r.text.split('median target of ')[1].split(',')[0])
    low = float(r.text.split('low estimate of ')[1].split('. ')[0])

    return price, high, median, low





def verify_price_and_forcast(symbol):
    'verify a stock has a price, forcasted high price, forcasted median price, and forcasted low price'

    prices = get_ticker_page(str(symbol))

    if None in prices:
        print(f'Unable to verify price data. price (${prices[0]}), forcasted high price (${prices[1]}), '
              f'forcasted median price (${prices[2]}), and forcasted low price (${prices[3]}).')
        return False

    print(f'Successfully verified price (${prices[0]}), forcasted high price (${prices[1]}), '
          f'forcasted median price (${prices[2]}), and forcasted low price (${prices[3]}).')
    return True






verify_price_and_forcast('load')