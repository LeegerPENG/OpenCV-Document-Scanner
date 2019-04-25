# from PIL import Image
# # import cv2
# # from pylab import *
# #
# # def histeq(img, nbr_bins=256):
# #     """ Histogram equalization of a grayscale image. """
# #
# #     # 获取直方图p(r)
# #     imhist, bins = histogram(img.flatten(), nbr_bins, normed=True)
# #
# #     # 获取T(r)
# #     cdf = imhist.cumsum()  # cumulative distribution function
# #     cdf = 255 * cdf / cdf[-1]
# #
# #     # 获取s，并用s替换原始图像对应的灰度值
# #     result = interp(img.flatten(), bins[:-1], cdf)
# #
# #     return result.reshape(img.shape), cdf
# #
# # if __name__ == "__main__":
# #     image_path='sample_images/F2-1.jpg'
# #     #image = cv2.imread(image_path)
# #     image = array(Image.open(image_path).convert('L'))
# #     newImage,cdf=histeq(image)
# #     cv2.imwrite('sharpen/F2-1.jpg',newImage)


# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt
#
# img = cv.imread('sample_images/F2-1.jpg', 0)
#
# hist, bins = np.histogram(img.flatten(), 256, [0,256])
#
# cdf = hist.cumsum()
# cdf_normalized = cdf*float(hist.max())/cdf.max()
#
# plt.plot(cdf_normalized, color = 'b')
# plt.hist(img.flatten(),256,[0,256], color = 'r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'), loc = 'upper left')
# plt.show()
#
# cdf = (cdf-cdf[0]) *255/ (cdf[-1]-1)
# cdf = cdf.astype(np.uint8)
#
# img2 = cdf[img]
#
# cv.imshow(img2)


import cv2
import numpy as np
from matplotlib import pyplot as plt
def histogram_equalization(img):



    #
    # # calculate hist
    # hist, bins = np.histogram(img, 256)
    # # calculate cdf
    # cdf = hist.cumsum()
    # # plot hist
    # plt.plot(hist,'r')
    #
    # # remap cdf to [0,255]
    # cdf = (cdf-cdf[0])*255/(cdf[-1]-1)
    # cdf = cdf.astype(np.uint8)# Transform from float64 back to unit8
    #
    # # generate img after Histogram Equalization
    # img2 = np.zeros((384, 495, 1), dtype =np.uint8)
    # img2 = cdf[img]
    #
    # hist2, bins2 = np.histogram(img2, 256)
    # cdf2 = hist2.cumsum()
    # plt.plot(hist2, 'g')
    #
    # #cv.imshow("after", img2)
    # cv.imwrite('sharpen/F2-1.jpg',img2)
    # #plt.show()
    # #cv.waitKey(0)

    # # create a CLAHE object (Arguments are optional).
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    img2= clahe.apply(img)
    # cv.imwrite('sharpen/F2-1.jpg', img)

    # equ = cv2.equalizeHist(img)
    # img2 = np.hstack((img, equ))  # stacking images side-by-side
    return img2

