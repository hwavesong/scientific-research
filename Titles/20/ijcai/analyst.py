# -*- coding: utf-8 -*-
# @Time    : 22:05 2020/10/18 
# @Author  : Haohao Song
# @Email   : songhaohao2018@cqu.edu.cn
# @File    : analyzer.py
import json

with open('./data/ijcai20.json','r',encoding='utf8') as fr:
    ijcai_dict=json.loads(fr.read())

ijcai_papper_titles=list()
for section_name,section_paper in ijcai_dict.items():
    for paper_name,paper_authors in section_paper:
        ijcai_papper_titles.append(paper_name)

print('the number of the ijcai2020 is {}\n'.format(len(ijcai_papper_titles)))

#loweer
for idx in range(len(ijcai_papper_titles)):
    ijcai_papper_titles[idx]=ijcai_papper_titles[idx].lower()
    # print(ijcai_papper_titles[idx])

title_for_purposes_method=list()
title_for_purposes=list()
title_name_description=list()
title_popular=list()
title_to=list()
title_with_via=list()
title_in_on=list()
title_of=list()
title_based_guided=list()
title_enhanced=list()

def find_colon_in_words(words_list):
    for idx,one_word in enumerate(words_list):
        if ':' in one_word:
            return idx

def find_based_guided_in_words(words_list):
    for one_word in words_list:
        if 'guided' in one_word or 'based' in one_word:
            return True
    return False

title_for_purposes_remainder=list()
for one_title in ijcai_papper_titles:
    splited_title=one_title.split()

    if ':' in one_title:
        word_with_colon_idx=find_colon_in_words(splited_title)
        if word_with_colon_idx!=0:
            title_popular.append(one_title)
        else:
            title_name_description.append(one_title)
        continue

    if 'for' in splited_title:
        index_for=splited_title.index('for')
        if 'with' in splited_title:
            index_with=splited_title.index('with')
            if index_with<index_for:
                title_for_purposes.append(one_title)
            else:
                title_for_purposes_method.append(one_title)
        elif 'via' in splited_title:
            title_for_purposes_method.append(one_title)
        else:
            title_for_purposes.append(one_title)
    elif 'to' in splited_title:
        title_to.append(one_title)
    elif 'with' in splited_title or 'via' in splited_title or 'using' in splited_title or 'by' in splited_title:
        title_with_via.append(one_title)
    elif 'in' in splited_title or 'on' ==splited_title[0]:
        title_in_on.append(one_title)
    elif 'of' in splited_title:
        title_of.append(one_title)
    elif find_based_guided_in_words(splited_title):
        title_based_guided.append(one_title)
    elif 'enhanced' in splited_title:
        title_enhanced.append(one_title)
    else:
        title_for_purposes_remainder.append(one_title)

with open('./data/enhanced.txt','w',encoding='utf8') as fw:
    for one_title in title_based_guided:
        fw.write(one_title+'\n')

with open('./data/based_guided.txt','w',encoding='utf8') as fw:
    for one_title in title_based_guided:
        fw.write(one_title+'\n')

with open('./data/of.txt','w',encoding='utf8') as fw:
    for one_title in title_of:
        fw.write(one_title+'\n')

with open('./data/in_on.txt','w',encoding='utf8') as fw:
    for one_title in title_in_on:
        fw.write(one_title+'\n')

with open('./data/with_via_using_by.txt','w',encoding='utf8') as fw:
    for one_title in title_with_via:
        fw.write(one_title+'\n')

with open('./data/to.txt','w',encoding='utf8') as fw:
    for one_title in title_to:
        fw.write(one_title+'\n')

with open('./data/popular.txt','w',encoding='utf8') as fw:
    for one_title in title_popular:
        fw.write(one_title+'\n')

with open('./data/name_description.txt','w',encoding='utf8') as fw:
    for one_title in title_name_description:
        fw.write(one_title+'\n')

with open('./data/for_purpose_method.txt','w',encoding='utf8') as fw:
    for one_title in title_for_purposes_method:
        fw.write(one_title+'\n')

with open('./data/for_purpose.txt','w',encoding='utf8') as fw:
    for one_title in title_for_purposes:
        fw.write(one_title+'\n')

with open('./data/for_purpose_remainder.txt','w',encoding='utf8') as fw:
    for one_title in title_for_purposes_remainder:
        fw.write(one_title+'\n')
