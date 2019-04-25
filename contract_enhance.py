from PIL import Image
from PIL import ImageEnhance
import cv2
import random
def contractEnhance(img):

# 对比度增强
    enh_con = ImageEnhance.Contrast(img)
    contrast = 1.5
    img_contrasted = enh_con.enhance(contrast)
    return img_contrasted


def sharpness(img):
    # 锐度增强
    enh_sha = ImageEnhance.Sharpness(img)
    sharpness = 3
    image_sharped = enh_sha.enhance(sharpness)
    return image_sharped

def PepperandSalt(src,percetage):
    NoiseImg=src
    NoiseNum=int(percetage*src.shape[0]*src.shape[1])
    for i in range(NoiseNum):
        randX=random.randint(0,src.shape[0]-1)
        randY=random.randint(0,src.shape[1]-1)
        if random.randint(0,1)<=0.5:
            NoiseImg[randX,randY]=0
        else:
            NoiseImg[randX,randY]=255
    return NoiseImg

if __name__=="__main__":
    img = Image.open('sample_images/F2-1.JPG')
    img=contractEnhance(img)
    img=sharpness(img)
    img.show()