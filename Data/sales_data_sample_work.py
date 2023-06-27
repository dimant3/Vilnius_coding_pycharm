import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data_sample.csv', encoding="ISO-8859-1")

# unique countries count - 19
unique_countries_count = df.COUNTRY.nunique()
# print(unique_countries_count)

# unique product lines - 7
unique_product_lines = df.PRODUCTLINE.nunique()
# print(unique_product_lines)

# 1. Suskaiciuoti kiek uzsakymu pateikta is kiekvienos salies

    # gale value_counts() rodo visas reiksmes, value_counts().nlargest(10) - 10 didziausiu
group_by_country = df['COUNTRY'].value_counts().nlargest(10)
# print(group_by_country)

plt.figure(figsize=(15, 10))     # grafiko dydis nustatomas
plt.bar(group_by_country.index, group_by_country.values)

plt.title('Customers grouped by countries')
plt.xlabel('Salys')
plt.xticks(rotation=90)     #salys pasukamos 90 laipsniu kampu grafike
plt.ylabel('Klientu skaicius')
plt.show()


# ---- 2. Atrinkti uzsakymus, kuriu suma virsija 5000 euru

# df['TOTAL'] = df['QUANTITYORDERED'] * df['PRICEEACH'] # create new column
# order_sum_bigger = df[df['TOTAL'] > 5000][['ORDERNUMBER', 'CUSTOMERNAME', 'STATUS', 'TOTAL']]
# df.to_csv('sales_data_sample.csv', index=False)    # created new column to CSV file!!!
# print(order_sum_bigger)


# --- 3. Isfiltruokite uzsakymus kurie buvo pristatyti nuo 2003/09/30 iki 2005/03/15
# keiciamas datos formatas
# df['ORDERDATE']=pd.to_datetime(df['ORDERDATE'], format='%d/%m/%Y %H:%M', errors='coerce')
# filtered_date = df[(df['ORDERDATE'] >= "9/30/2003") & (df['ORDERDATE'] <= "3/15/2005")]
# print(filtered_date)


# --- 4. Išfiltruokite užsakymus, kurių statusas 'Disputed';
# status_disputed = df[df['STATUS']=='Disputed']
# print(status_disputed)
