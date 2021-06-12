from pytesseract import *
from PIL import Image, ImageOps, ImageFilter
import cv2


def gray_s(img_path):
    #image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    #gray = cv2.medianBlur(gray, 10)
    grayImg = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(img_path, grayImg)
    cv2.imshow('gray', grayImg)
    cv2.waitKey(0)

def img_Contrast(img):
    #-----Converting image to LAB Color model-----------------------------------
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    #-----Splitting the LAB image to different channels-------------------------
    l, a, b = cv2.split(lab)
    #-----Applying CLAHE to L-channel-------------------------------------------
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    #-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
    limg = cv2.merge((cl, a, b))
    #-----Converting image from LAB Color model to RGB model--------------------
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    return final





def OCR(text, img_path):
    try:
        img = Image.open(img_path)
        text = pytesseract.image_to_string(img, lang='kor')
        #print(text)
        return text
    except FileNotFoundError:
        print("OCR : FileNotFoundError")
        return 0
    # if text != "":
    #     #print(text)
    #
    #     #문구가 있으면 문자 1 반환
    #     print("있으면 1")
    #     return text
    #
    # else:
    #     #없으면 문자 0을 반환
    #     print("없으면 0")

#
# img_path = "/Users/sonjung-yeong/Desktop/naver_blog_post/seoul_naver_blog_post_img/https:/blog.naver.com/gkwork90/222352139632/82.jpg"
# # check_keyword = ["협찬", "고료", "광고", "후원", "원고", "지원", "제공", "업체", "서비스"]
# #
# # # img = cv2.imread(img_path)
# # # img = img_Contrast(img)
# # # img.save(img_path)
# #
# #
# # gray_s(img_path)
# text = ""
# OCR(text, img_path)

