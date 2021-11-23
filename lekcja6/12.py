lista=open('shopping.txt','a')
produkt=str(input('Dodaj produkt do listy: '))
lista.write(f'{produkt}\n')
lista.close()


