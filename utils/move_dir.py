import os
import shutil

root_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))

from_dir = os.path.join(root_dir, 'data/convert')
to_dir = os.path.join(root_dir, 'data/dataset')

for phase in os.listdir(from_dir):
    from_phase_path = os.path.join(from_dir, phase)
    to_phase_path = os.path.join(to_dir,phase)

    if not os.path.isdir(to_phase_path):
        os.mkdir(to_phase_path)

    for product in os.listdir(from_phase_path):
        from_product_path = os.path.join(from_phase_path, product)

        shutil.move(from_product_path, to_phase_path)
