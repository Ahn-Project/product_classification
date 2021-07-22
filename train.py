import torch
from torchvision import transforms, datasets
import os

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([],[])
])

root_dir = './data/dataset/'
dataset = {x : datasets.ImageFolder(os.path.join(root_dir, x),
                                    transform=transform) for x in ['train', 'val']}

data_loader = {x : torch.utils.data.DataLoader(dataset[x],
                                               shuffle=True,
                                               batch_size=16,
                                               num_workers=4) for x in ['train', 'val']}


