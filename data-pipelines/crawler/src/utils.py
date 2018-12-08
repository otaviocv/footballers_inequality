import re

def convert_market_value(v):
    number_search = re.search('([0-9]+\.?[0-9]+)', v)
    if number_search is None:
        return 0
    number = float(number_search.group(1))
    scale = re.search('[0-9]*([a-z]+)', v).group(1)
    if scale == 'k':
        return number*1e3
    elif scale == 'm':
        return number*1e6
    elif scale == 'bn':
        return number*1e9
