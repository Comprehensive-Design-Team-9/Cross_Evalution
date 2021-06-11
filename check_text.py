





def check(text, keyword):
    if text != None:
        if keyword in text:
            #print("탬색한 키워드", keyword)
            #print("Hae")
            return 1
        else:
            #print("탬색한 키워드", keyword)
            #print("0")
            return 0
    else:
        #print("0")
        return 0


def check_have_not(check_cnt):
    if check_cnt != 0:
        print("공정위 문구가 포함되어 있습니다")
        print("공정위 키워드 수 : ", check_cnt)
        return 1
    else:
        print("공정위 문구가 포함되어 있지 않습니다")
        #print(check_cnt)
        return 0
