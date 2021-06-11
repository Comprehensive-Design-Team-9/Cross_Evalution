import pyocr
import check_text
import get_url

#파일 저장 위치
csv_path = "파일 저장 위치 "
#파일 저장 위치
img_path = "이미지 저장 위치 "
# 불러올 url 저장된 파일 명칭
url_file_name = "all_url_bin_20210610141422.csv"



check_keyword = ["협찬", "고료", "광고", "후원", "원고", "지원", "제공"]



text = ""
url_list = []

if __name__ == "__main__":
    get_url.mkfile(["url", "keyword_bin"], csv_path+"img_keyword.csv")
    print("url getting")
    url_list = get_url.get_url(url_list, csv_path + url_file_name)
    print("OCR Working")
    t = 0
    for j in url_list:
        t = t + 1
        print(t)
        print(j)
        bin = 0
        #print("file name getting")
        file_list = get_url.get_img_path(j, img_path)
        if file_list == None:
            pass
        else:
            for i in file_list:
                print(i)
                check_cnt = 0
                text = pyocr.OCR(text, img_path + j + i)
                if text == None:
                    pass
                #print("추출된 문장 : ", text)
                else:
                    for k in check_keyword:
                        cnt = check_text.check(text, k)
                        check_cnt = check_cnt + cnt
                    bin = check_text.check_have_not(check_cnt)
                    print(bin)
                    print("\n")
            get_url.img_bin_csv(j, bin, csv_path+"img_keyword.csv")


