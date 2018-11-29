import re

def convert_market_value(v):
    print(v)
    number = float(re.search('([0-9]+\.?[0-9]+)', v).group(1))
    print(number)
    scale = re.search('[0-9]*([a-z]+)', v).group(1)
    print(scale)
    if scale == 'k':
        return number*1e3
    elif scale == 'm':
        return number*1e6
    elif scale == 'bn':
        return number*1e9




