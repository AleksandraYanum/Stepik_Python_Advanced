from csv import DictReader


DELIMITER = ';'
STORE_COL_NAME = 'Магазин'


def find_cheapest_product(file_name):

    cheapest_product = None
    cheapest_store = None
    min_price = float('inf') # infinitely large value

    with open(file_name, encoding='utf-8') as file:
        reader = DictReader(file, delimiter=DELIMITER)

        for row in reader:
            store = row.pop(STORE_COL_NAME) 
            for product, price in row.items():
                price = int(price)
                if price < min_price:
                    min_price = price
                    cheapest_product = product
                    cheapest_store = store

                elif price == min_price:
                    if product < cheapest_product: # Lexicographic product check
                        cheapest_product = product
                        cheapest_store = store
                    elif product == cheapest_product and store < cheapest_store:
                        cheapest_store = store

    cheapest_product_store_result = f"{cheapest_product}: {cheapest_store}"

    return cheapest_product_store_result


def main():
    cheapest_product = find_cheapest_product('prices.csv')
    print(cheapest_product)


main()