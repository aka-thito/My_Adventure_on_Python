# Clase 31 Parte 2
# la profe llamo a este archivo new_data_csv.py, yo lo llamre como
# quiera xD

import csv

new_product = {
    'name': "Wireless Chatger",
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2024-07-01'
}

with open('products.csv', mode = 'a', newline = '') as file:
    
    file.write('\n')

    csv_writer = csv.DictWriter(file, fieldnames = new_product.keys())
    csv_writer.writerow(new_product)

# hay que tener cuidado al ejecutar más de una vez este tipo de 
# codigo porque puedes replicar la informacion en el archivo que se
# edita