import os
import json

# load category name
with open('./category_name.json', 'r') as f:
    category_name = json.load(f)

keylist = list(category_name.keys())

root_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
dataset_path = os.path.join(root_dir, 'data/convert')

for phase in os.listdir(dataset_path):
    phase_path = os.path.join(dataset_path, phase)
    for category in os.listdir(phase_path):
        category_path = os.path.join(phase_path, category)
        if category in keylist:
            category_name_new = category_name[category]
            category_renamed = os.path.join(phase_path, category_name_new)
            os.rename(category_path, category_renamed)  # 상품 분류명 한영 변환
            category_path = category_renamed
        else:
            category_name_new = category
            category_path = os.path.join(phase_path, category_name_new)

        for product in os.listdir(category_path):
            product_name_new = category_name_new + '_' + product.split('_')[0]
            product_path = os.path.join(category_path, product)
            product_renamed = os.path.join(category_path, product_name_new)
            try:
                os.rename(product_path, product_renamed)    # 상품명 변환
            except FileExistsError:
                pass


