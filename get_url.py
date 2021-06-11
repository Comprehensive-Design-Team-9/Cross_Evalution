import csv
import os


def get_url(url_list, csv_path):
    with open(csv_path, 'r', encoding='utf-8-sig') as url_csv:
        url = csv.reader(url_csv)
        next(url)
        for i in url:
            url_list.append(str(i[0])+"/")
            #print(url_list)
        return url_list


def get_img_path(url, img_path):
    try:
        file_list = os.listdir(img_path + url)
        #print(type(file_list))
        return file_list
    except FileNotFoundError:
        return None


def img_bin_csv(url, bin, csv_path):
    with open(csv_path, 'a', encoding='utf-8-sig') as bin_file:
        file = csv.writer(bin_file)
        file.writerow([url, bin])


def mkfile(data, csv_path):
    with open(csv_path, 'a', encoding='utf-8-sig') as bin_file:
        file = csv.writer(bin_file)
        file.writerow(data)