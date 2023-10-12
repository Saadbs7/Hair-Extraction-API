from model import BiSeNet
import torch
import os.path as osp
import numpy as np
from PIL import Image
import torchvision.transforms as transforms
import cv2

def evaluate(cp='model/model.pth', input_path='files\input.jpg'):

    n_classes = 19
    net = BiSeNet(n_classes=n_classes)
    net.cpu()
    save_pth = osp.join('', cp)
    net.load_state_dict(torch.load(save_pth, map_location=torch.device('cpu')))
    net.eval()

    to_tensor = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
    ])
    with torch.no_grad():
        img = Image.open(input_path)
        # imgshape = img.shape[0:2]
        origin = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
        # image = img.resize((512,512))
        # image = img.resize((512, 512), Image.ANTIALIAS)
        # image = img.resize((512, 512), Image.NEAREST)
        # image = img.resize((512, 512), Image.LANCZOS)
        image = img.resize((512, 512), Image.BILINEAR)
        img = to_tensor(image)
        img = torch.unsqueeze(img, 0)
        img = img.cpu()
        out = net(img)[0]
        parsing = out.squeeze(0).cpu().numpy().argmax(0)
        # parsing = cv2.reshape(parsing, imgshape)
        cv2.imwrite('files/initialSegmentation.jpg', parsing, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    return 'Evaluated! '
        

# if __name__ == "__main__":
    # evaluate(input_path='files/14.jpg', output_path='files/7_g.jpg', mode='black')
