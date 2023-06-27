import pandas as pd  # as pd tiesiog sutrumpinimas pandas kaip ir SQL
import matplotlib.pyplot as plt

# vienmate duomenu struktura(saugo vienos eilutes duomenis su indeksais)
# data = pd.Series([10, 20, 30, 40, 50])
# print(data)

# dvimate duomenu struktura(saugo duomenis lenteles pavidalu su stulpeliu ir eiluciu indeksais)
data = {
    'Name': ['Mantas', 'Deividas', 'Migle', 'Ausrine'],
    'Age': [29, 27, 24, 45],
    'City': ['Marijampole', 'Vilnius', 'Kaunas', 'Vilnius']
    }
df = pd.DataFrame(data) #df - dataframe, reiskia kad printinsim lentele
# print(df)
# print(df.head(3)) #skliausteliu viduje nurodyti kiek norime matyti eiluciu, tiek ir atvaizduos
# print(df['Name']) #atvaizduoja tik vardus
selected_columns = df[['Name', 'City']]
print(selected_columns) #atvaizduos tik tuos stulpelius kuriuos nurodeme

# prideti nauja stulpeli  """
# df['Salary'] = [1600, 1400, 1300, 1200]
# print(df)

# Gruojame duomenis pagal miesta ir gaukime vid. atlyginima"""
# average_salary_by_city = df.groupby('City') ['Salary'].mean() #butent mean veda vidurki
# print(average_salary_by_city)

# Ieskome vid. amziaus
# average_age = df['Age'].mean()
# print(f"Average age: {average_age}")

# filtruojame pagal nurodyta salyga   (siuo atveju metai)"""
# filtered_data = df[df['Age'] > 25][['Name', 'Age']] #dar pridejus skliaustelius pateiks tik name ir age
# print(filtered_data)


# ------- IS employees.csv data -----------
# df = pd.read_csv('employees.csv')
# print(df.head(5))

# grupuoti pagal "first_name" stulpeli ir suskaiciuoti jo dydi
# group_sizes = df.groupby('FIRST_NAME').size()
# print(group_sizes)

# group_average = df.groupby('FIRST_NAME')['SALARY'].mean()
# print((group_average))

# sugrupuoja pagal varda ir pateikia visu vardu atlyginimu statistika procentaliai
# group_stats = df.groupby('FIRST_NAME')['SALARY'].describe()
# print(group_stats)

# sugrupuoja pagal varda ir pateikia is to vardo didziausia atlyginima
# group_max = df.groupby('FIRST_NAME')['SALARY'].max()
# print(group_max)


# sugrupuoja pagal varda ir pateikia statistika kuria pasirenkame (sum, mean, max, size):
# group_agg = df.groupby('FIRST_NAME').agg({'SALARY': ['sum', 'mean', 'max', 'size']})
# print(group_agg)

# atvaizduojama diagrama(bar/line/pie ir t.t. (auksciau parasyto group_agg)
# group_agg.plot(kind='bar', figsize=(8, 4))

# pridedamos diagramos antrastes prie linijines diagramos
# plt.title('Suvestines statistika pagal vardus ir ju atlyginimus')
# plt.xlabel('Vardas')
# plt.ylabel('Atlyginimas')

# komanda atvaizduojama diagrama
# plt.show()
