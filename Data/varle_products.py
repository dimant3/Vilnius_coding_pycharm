
# duomenu scrapinimas - paemimas is tinklalapiu

import requests
from bs4 import BeautifulSoup
import psycopg2

def create_and_insert_product():
    connection = psycopg2.connect(
        host ="localhost",
        port=5432,
        database="products",
        user="postgres",
        password="barabanas12"
    )

    # creating management with database
    cursor = connection.cursor()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS varle_products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        price DECIMAL(10, 2),
        quantity INT
        )
    """
    # execute SQL statement
    # cursor.execute(create_table_query)
    # print("Table created successfully!")

    # define website
    url = "https://www.varle.lt/nesiojami-kompiuteriai/nesiojami-kompiuteriai/"

    # response from the website
    response = requests.get(url) # pasiima visa informacija is URL

    # create a bs4(beautifulsoup4) object (musu objektas) to parse (analizuoti) the HTML content
    soup = BeautifulSoup(response.content, 'html.parser') #soup kad galetume pasiimt produktu info

    # find all product elements in the category (ajax-container)
    product_elements = soup.find_all('div', class_='ajax-container')
    # print(product_elements)


    # iterate over each product element and extract product information
    for product_element in product_elements:
        product_name = product_element.find('div', class_='product-title').text.strip() #gauna teksta ir pasalina tarpus
        product_price = product_element.find('span', class_='price-value').text.strip()[:3]
        product_quantity = product_element.find('b').text.strip()[:1]

        # inserting product data into the 'varle_products' table.
        insert_query = "INSERT INTO varle_products (name, price, quantity) VALUES (%s, %s, %s)"
        # %s - string formatu grazins reiksmes
        cursor.execute(insert_query, (product_name, product_price, product_quantity))


    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    create_and_insert_product()
