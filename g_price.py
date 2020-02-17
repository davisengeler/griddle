from datetime import datetime
import re
import requests
from bs4 import BeautifulSoup

def get_current(load_zone):
    # Scrape the current price
    pricing_url = "http://www.ercot.com/content/cdr/html/current_np6788"
    request = requests.get(pricing_url)
    data = request.text
    soup = BeautifulSoup(data, "html.parser")
    settlement_points = soup.find_all('tr')
    prices = {}
    for zone in settlement_points:
        try:
            details = zone.find_all('td', {'class': 'tdLeft'})
            price_text = details[3].text
            price_text = price_text.replace(',', '')
            prices[details[0].text] = round(float(price_text) / 10, 1)
            # print(f"{details[0].text}")
        except Exception as e:
            pass
            # print(f"Problem: {e}")

    for elem in soup(text=re.compile(r'Updated')):
        match = re.search(r'\d{2}:\d{2}:\d{2}', elem.parent.text)

    # Scrape the time of last price update
    elem = soup(text=re.compile(r'Updated'))[0]
    extracted_time = re.search(r'\d{2}:\d{2}:\d{2}', elem.parent.text).group(0)
    time = datetime.strptime(extracted_time, "%H:%M:%S")
    updated_at = time.strftime("%-I:%M %p")

    # Prep the final details
    new_price = prices[load_zone]

    return new_price, updated_at