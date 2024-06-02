import pandas as pd

TAG_LIST = ['GPT', 'Bard', '文心一言', 'Bing', 'Claude', 'PaLM', '豆包', 'kimi', '讯飞星火',
            '盘古气象', '盘古小艺']

TAG_LIST2 =['chatbot','聊天机器人','人工智能','生成式AI','大语言模型','大模型']
def match_tags(str_):
    matched = []
    lower_str = str_.lower()
    for tag in TAG_LIST:
        if tag.lower() in lower_str:
            matched.append(tag)
    return matched

def match_tags2(str_):
    matched = []
    lower_str = str_.lower()
    for tag in TAG_LIST2:
        if tag.lower() in lower_str:
            matched.append(tag)
    return matched


if __name__ == "__main__":
    hot_search = pd.read_excel("HotSearches.xlsx")
    pattern = '|'.join(TAG_LIST)
    filtered_hot_search = hot_search[hot_search['Hashtag'].str.contains(pattern, na=False, case=False)].copy()
    filtered_hot_search['Tags'] = filtered_hot_search['Hashtag'].apply(match_tags)
    filtered_hot_search.to_excel("chatbot_hot_search.xlsx", index=False)

    pattern2 = '|'.join(TAG_LIST2)
    gen_hot_search = hot_search[hot_search['Hashtag'].str.contains(pattern2, na=False, case=False)].copy()
    gen_hot_search['Tags'] = gen_hot_search['Hashtag'].apply(match_tags2)
    gen_hot_search.to_excel("gen_hot_search.xlsx", index=False)
    # def find_tag_and_theme(hashtag):
    #     for tag in tags_list:
    #         if tag in hashtag:
    #             return tag, 'LLM'
    #     return '', ''
    #
    #
    # hot_search[['Tags', 'Theme']] = hot_search['Hashtag'].apply(lambda x: pd.Series(find_tag_and_theme(x)))
    # print(hot_search['Tags'].count())

# hot_search = pd.read_excel("/Users/hanjingwang/Documents/GithubCode/tg-wb-trending/HotSearches.xlsx")
# for i in range(len(hot_search)):
#     for tag1 in ['GPT', 'gpt', 'Bard', '文心一言', 'Bing chat', 'Bing AI', 'Claude', 'PaLM',
#                  '豆包', 'kimi', '讯飞星火', '盘古气象', '盘古小艺']:
#         if tag1 in hot_search['Hashtag'].iloc[i]:
#             hot_search.loc['Tags',i] = tag1
#             hot_search.loc['Theme',i] = 'LLM'
#
# print(len(hot_search['Tags']))

# for i in range(len(hot_search)):
#     for tag2 in ['chatbot'，'聊天机器人'，'人工智能'，'生成式AI'，'大语言模型']:
#     if tag2 in hot_search['Hashtag'].iloc[i]:
#         hot_search['Tags'] = tag2
#         hot_search['Theme'] = 'General'
