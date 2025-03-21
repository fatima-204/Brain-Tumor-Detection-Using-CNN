import torch
import torchvision

import torch
from torch import nn
import torchvision

import torchvision.transforms as T
from torchvision.models import resnet101, ResNet101_Weights

import torch
import torchvision
import torchvision.transforms as T
from torchvision.models import resnet101

def create_model(num_classes=4):
    # Define your own transformations (resize, crop, to tensor, normalize)
    transform = T.Compose([
        T.Resize(128),  # Resize the image to 128x128
        T.CenterCrop(128),  # Crop the image to 128x128
        T.ToTensor(),  # Convert the image to a tensor
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalize
    ])

    # Load the ResNet101 model with the default weights
    model = torchvision.models.resnet101(weights=torchvision.models.ResNet101_Weights.DEFAULT)

    # Adjust the output layer to match the number of classes
    model.fc = torch.nn.Linear(in_features=2048, out_features=num_classes)
    
    return model, transform



