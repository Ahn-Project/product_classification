import torch
from torchvision import transforms, datasets
from torch import nn, optim
import os


def load_dataset(root_dir):
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    dataset = {x : datasets.ImageFolder(os.path.join(root_dir, x),
                                        transform=transform) for x in ['train', 'val']}

    data_loader = {x : torch.utils.data.DataLoader(dataset[x],
                                                   shuffle=True,
                                                   batch_size=16,
                                                   num_workers=4) for x in ['train', 'val']}
    return dataset, data_loader


def define_model():
    from model import resnet

    model = resnet.resnet18(pretrained=True)
    num_features = model.fc.in_features
    model.fc = nn.Linear(num_features, n_classes)
    model = model.to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
    lr_scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)
    return model, criterion, optimizer, lr_scheduler


if __name__ == "__main__":
    n_classes = 2
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    root_dir = './data/dataset/'
    dataset, data_loader = load_dataset(root_dir)

    model, criterion, optimizer, lr_scheduler = define_model()