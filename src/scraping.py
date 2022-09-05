from typing import List
from src.soup import DigForRates


def get_exchange_matrix(symbols: List[str]) -> dict[str, dict[str, float]]:
    """
    returns exchange rates for given currencies symbol
    returned shape example {"USD": {"USD" : 1.0,'EUR': 1.00472, 'JPY': 140.211}..}
    """
    matrix = {}
    dig_for_rates = DigForRates()

    for symbol in symbols:
        # for given currency find coresponding exchange rates
        rates_float = dig_for_rates.dig_for_rates_in_html(symbol)
        rates_dict = dict(zip(symbols, rates_float))
        matrix[symbol] = rates_dict

    return matrix


def presents_rates(amount: float, from_currency: str, to_currency: str) -> str:
    """
    prints actual exchange rates for given currency
    """
    allowed_symbols = ["USD", "EUR", "JPY", "GPB", "CHF", "CAD", "AUD", "HKD"]
    if from_currency not in allowed_symbols or to_currency not in allowed_symbols:
        return "Incompatible currency"
    matrix = get_exchange_matrix(allowed_symbols)
    return f"Today {amount} {from_currency} is worth {round(amount * matrix[from_currency][to_currency],6)} {to_currency}"
