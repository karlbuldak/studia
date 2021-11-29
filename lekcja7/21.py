import json
with open('euro.json') as euro:
    file=json.load(euro)
print('Date\t\tBuying Rate\t\tSelling Rate')
print('='*52)
for n in range(10):
    print(file['rates'][n]['effectiveDate'],'\t',
          file['rates'][n]['bid'],'\t\t',
          file['rates'][n]['ask'])



     