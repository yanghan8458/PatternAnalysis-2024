import os
import numpy as np
import torch
from torch.utils.data import Dataset

class ProstateMRIDataset(Dataset):
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.file_list = []
        for root, dirs, files in os.walk(root_dir):
            for file_name in files:
                if file_name.endswith('.npy'):
                    self.file_list.append(os.path.join(root, file_name))

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        img_path = self.file_list[idx]
        image = np.load(img_path)
        
        # Normalize image data to the range of [0,1]
        image = image / np.max(image)  、
        image = torch.tensor(image, dtype=torch.float32).unsqueeze(0)  # Add channel dimension
        return image
