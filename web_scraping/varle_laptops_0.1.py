from bs4 import BeautifulSoup
import requests

url = "https://www.varle.lt/nesiojami-kompiuteriai/nesiojami-kompiuteriai/"

response = requests.get(url)
# print(response)

soup = BeautifulSoup(response.content, 'html.parser')

laptop = soup.find('div', class_='GRID_ITEM')
# find_all all will be deleted as we work only with 1st item to prevent too much information

laptop_title = laptop.find('div', class_='product-title').text.strip()
laptop_title_parts = laptop_title.split('/')  # Splitting the title using '/'
# ensure that there are at least three elements in the split result
if len(laptop_title_parts) >= 3:
    element1 = laptop_title_parts[0].strip()    # title
    element2 = laptop_title_parts[1].strip()    # processor
    element3 = laptop_title_parts[2].strip()    # disk
    element4 = laptop_title_parts[3].strip()    # ram
    element5 = laptop_title_parts[4].strip()    # graphics

    print(f"Title: {element1}")
    print(f"Processor: {element2}")
    print(f"Disk: {element3}")
    print(f"RAM: {element4}")
    print(f"Graphics: {element5}")
else:
    print("Unable to split the title into three elements.")

laptop_price = laptop.find('span', class_='price-value').text.strip()
laptop_manufacturer = laptop.find('div', class_='spec-shortcuts').span.text
print(f"Laptop price: {laptop_price}")
print(f"Manufacturer: {laptop_manufacturer}")

# cia tureciau ideti url nuoroda i to laptopo info
# more_info = laptop.div('product-title').a
# print(more_info)


# manufacturer_name = laptop.find('div', class_='spec-shortcuts')
# print(laptop_title)
# print(laptop_price)
# print(laptop_manufacturer)