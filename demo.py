import cv2

from predict import *
result = predict_one_image('./images/receipt.jpeg')
cv2.imwrite('./images/output4.jpg', result)
show(result)
