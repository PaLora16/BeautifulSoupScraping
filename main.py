from src.scraping import presents_rates

if __name__ == "__main__":
    # Give conversion between 100 USD and CAD
    print(presents_rates(100, "USD", "CAD"))