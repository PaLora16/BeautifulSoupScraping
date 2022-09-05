from typing import List

import requests
from bs4 import BeautifulSoup

class DigForRates:
    '''
    retrieve raw HTML, parse into soup objects and looks for exchange rates. 
    Echange rates are in <tr> elements. Each <tr> elemet contains <td> exchange rates.
    '''
    URL = "https://www.exchange-rates.org/"

    def __init__(self):
        page = requests.get(self.URL)
        soup = BeautifulSoup(page.content, "html.parser")
        self.table_rows = soup.find_all("tr")

    def remove_inverze_rate(self, rate: str) -> str:
        """soup returns exchange rates as well as reverse rates.
        It is more conscious to remove reverse rates than construct complex soup findings.
        """
        _splitted = rate.split(".")
        # remove reverse rates
        _splitted = _splitted[:2]
        return ".".join(_splitted)

    def dig_for_rates_in_html(self, currency_symbol: str) -> List[float]:
        # 1 USD etc - pattern to find section in HTML containing exchange rates
        one_curency_symbol = f"1 {currency_symbol}"
        rates_float: List[float] = []

        for table_row in self.table_rows:
            # traverse HTML just for given curency
            if table_row.find("a", text=one_curency_symbol):
                # exchage rates are in <td> elements
                rates = table_row.find_all("td")
                rates_float = [
                    float(self.remove_inverze_rate(rate.text))
                    for rate in rates
                    # ignore first td element containing currency description
                    if not rate.find("a", text=one_curency_symbol)
                ]
                break
        return rates_float