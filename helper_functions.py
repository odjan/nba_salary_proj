def clean_name(item):
    first_slash = item.find('\\')
    #name_ending[first_slash]
    return item[0:first_slash]

def clean_jr(item):
    if 'Jr.' in item:
        jr = item.find('Jr')
        return item[0:jr]
    else:
        return item


def remove_dollar_sign(obj):
    """

    """
    return obj.split('').pop(0)

def weird_division(n, d):
    try:
        return n/d
    except ZeroDivisionError:
        return 0

def clean_currency(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    https://pbpython.com/currency-cleanup.html
    """
    if isinstance(x, str):
        return(x.replace('$', '').replace(',', ''))
    return(x)