import pyocr
import check_text
import get_url
from datetime import datetime

#파일 저장 위치
csv_path = ""
#img 파일 저장 위치
seoul_img_path = ""
img_path = ""
# 불러올 url 저장된 파일 명칭
today_hour = datetime.today().strftime("%Y%m%d%H%M%S")
url_file_name = "drop_submission.csv"
seoul_url_file_name = "seoul_url_bin_20210612095453.csv"
save_file_name = "new_img_keyword_{}.csv".format(today_hour)



check_keyword = ["협찬", "고료", "광고", "후원", "원고", "지원", "제공", "업체", "서비스"]


test_url = "https://blog.naver.com/gkwork90/222352139632/"

text = ""
url_list = []
if __name__ == "__main__":
    get_url.mkfile(["url", "keyword_bin"], csv_path+save_file_name)
    print("url getting")
    url_list = get_url.get_url(url_list, csv_path + url_file_name)
    print("OCR Working")

    t = 0
    for j in url_list:
        t = t + 1
        print(t)
        print(j)
        bin = 0
        save_bin = 0
        #print("file name getting")
        file_list = get_url.get_img_path(j, img_path)
        if file_list == None:
            print("file list None")
            get_url.img_bin_csv(j, save_bin, csv_path + save_file_name)
        else:
            for i in file_list:
                print(i)
                check_cnt = 0
                text = pyocr.OCR(text, img_path + j + i)
                if text != None:
                    for k in check_keyword:
                        cnt = check_text.check(text, k)
                        check_cnt = check_cnt + cnt
                        #print("공정위 키워드 포함 횟수 check_cnt : ",check_cnt)
                    bin = check_text.check_have_not(check_cnt)
                    #print("공정위 키워드 포함 여부 :", bin)
                    #print("추출된 문장 : ", text)
                    #print("\n")
                else:
                    print("추출된 문장 문장이 없습니다 : ", text)
                save_bin = save_bin + bin
            print("입력되는 바이너리 값", save_bin)
            get_url.img_bin_csv(j, save_bin, csv_path+save_file_name)





