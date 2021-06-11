from pytesseract import *
from PIL import Image





def OCR(text, img_path):
    try:
        img = Image.open(img_path)
        text = pytesseract.image_to_string(img, lang='kor')
        return text
    except FileNotFoundError:
        pass
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




