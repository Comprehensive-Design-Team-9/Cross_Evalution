import csv
import os


def get_url(url_list, csv_path):
    with open(csv_path, 'r', encoding='utf-8-sig') as url_csv:
        url = csv.reader(url_csv)
        next(url)
        for i in url:
            url_list.append(str(i[1])+"/")
            #print(url_list)
        return url_list


def get_img_path(url, img_path):
    # file_list = os.listdir(img_path + url)
    # print(file_list)
    # return file_list
    try:
        file_list = os.listdir(img_path + url)
        for i in file_list:
            if i[-3:-1] != 'jpg':
                file_list.remove(i)
        print(file_list)
        return file_list
    except FileNotFoundError:
        print("Get_img_path : FileNotFoundError")
        return None


def img_bin_csv(url, bin, csv_path):
    with open(csv_path, 'a', encoding='utf-8-sig') as bin_file:
        file = csv.writer(bin_file)
        file.writerow([url, bin])


def mkfile(data, csv_path):
    with open(csv_path, 'a', encoding='utf-8-sig') as bin_file:
        file = csv.writer(bin_file)
        file.writerow(data)