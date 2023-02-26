import pytest

from src.scraping import presents_rates


@pytest.mark.parametrize(
    ["input", "expected"],
    [
        ("CAD", "Today 100 USD is worth 137.89 CAD"),
        ("EUR", "Today 100 USD is worth 103.134 EUR"),
        ("JPY", "Today 100 USD is worth 14685.45 JPY"),
    ],
)
def test_present_rates(mocker, input, expected):
    mocker.patch(
        "src.soup.DigForRates.dig_for_rates_in_html",
        return_value=[
            1.0,
            1.03134,
            146.8545,
            0.903121,
            0.998821,
            1.3789,
            1.5945,
            7.85015,
        ],
    )
    assert presents_rates(100, "USD", input) == expected
