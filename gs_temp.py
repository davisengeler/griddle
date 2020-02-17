def calculate_offset(price):
    if price < -3:
        return -2
    elif price >= 0 and price < 4.5:
        return 0
    elif price >= 4.5 and price < 10.0:
        return 1
    elif price >= 10.0 and price < 19.0:
        return 2
    elif price >= 19.0 and price < 30.0:
        return 4
    elif price >= 30.0 and price < 45.0:
        return 8
    elif price >= 45.0:
        return 16