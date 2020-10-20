# -*- coding: utf-8 -*-
# @Time    : 9:55 2020/10/20 
# @Author  : Haohao Song
# @Email   : songhaohao2018@cqu.edu.cn
# @File    : ijcai_spider.py
import json
from urllib import request

import lxml.html as lh

response=request.urlopen('http://static.ijcai.org/2020-accepted_papers.html')
text_html=response.read().decode('utf8')

html=lh.document_fromstring(text_html)
sections=html.xpath('/html/body/main/section')

ijcai20_accepted_dict=dict()
for one_section in sections:
    section_title=one_section.xpath('./div/h3/text()')[0]
    section_title=section_title.replace('\'','').strip()

    ijcai20_accepted_dict[section_title]=list()

    print(section_title)

    all_papers=one_section.xpath('./div/li')

    for one_paper in all_papers:
        one_paper_title=one_paper.xpath('./strong/text()')[0]
        one_paper_title=one_paper_title.replace('\'','').strip()

        one_paper_authors=one_paper.xpath('./em/text()')[0]
        one_paper_authors=one_paper_authors.replace('\'','').strip()

        ijcai20_accepted_dict[section_title].append((one_paper_title,one_paper_authors))

        print(one_paper_title)
        print(one_paper_authors)


with open('./data/ijcai20.json','w',encoding='utf8') as fw:
    fw.write(json.dumps(ijcai20_accepted_dict,ensure_ascii=False))

