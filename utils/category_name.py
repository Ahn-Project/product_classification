import json

category_name = {'유제품':'dairy_product', '의약외품':'quasi_drugs'}

with open('category_name.json', 'w') as fp:
    json.dump(category_name, fp)