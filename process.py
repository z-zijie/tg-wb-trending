import os
import pandas as pd


BASE_DIR = './archives'


def find_hashtag(str_):
    a = str_.find('[')
    b = str_.rfind(']')
    return str_[a+1:b]


def find_url(str_):
    a = str_.find('(')
    b = str_.rfind(')')
    return str_[a+1:b]


def find_category(str_):
    a = str_.find('`')
    b = str_.rfind('`')
    return str_[a+1:b]


def parse_markdown_file(fpath):
    lst = []
    date = fpath.split('/')[-1][:-3]
    file_ = open(fpath, 'r')
    lines = file_.readlines()
    for i, line in enumerate(lines):
        if i == 0:
            continue
        if len(line) < 4:
            continue
        hashtag = find_hashtag(line)
        url = find_url(line)
        cat = find_category(line)
        lst.append((date, hashtag, cat, url))
    file_.close()
    return lst

if __name__ == "__main__":
    filelist = os.listdir(BASE_DIR)
    filelist = sorted(filelist)
    df = pd.DataFrame(columns=["Date", "Hashtag", "Category", "URL"])
    for idx, filename in enumerate(filelist):
        filepath = f'{BASE_DIR}/{filename}'
        print(f"Reading FILE:   {filepath}")
        res = parse_markdown_file(filepath)
        tmp = pd.DataFrame(res, columns=["Date", "Hashtag", "Category", "URL"])
        df = pd.concat([df, tmp], ignore_index=True)

    df.to_excel("HotSearches.xlsx", index=False)

