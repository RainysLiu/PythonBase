import urllib.request
import ssl
import json
import os
import pickle
import requests
from PIL import Image
def ajaxcrawler(url):
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                     'AppleWebKit/537.36 (KHTML, like Gecko) '
                                     'Chrome/66.0.3359.139 Safari/537.36'
    }
    req=urllib.request.Request(url,headers=header)
    response=urllib.request.urlopen(req)
    jsonstr=response.read().decode('utf-8')
    jsondata=json.loads(jsonstr)
    return jsondata

#动态网页的抓取
def zhuaction():
    i=0
    allmoiveinfo=''
    print('动作电影信息抓取中...')
    for x in range(0, 5 + 1):
        url = 'https://movie.douban.com/j/chart/top_list?' \
              'type=5&interval_id=100%3A90&action=&start=' \
              + str(x * 20) + '&limit=20'
        info=ajaxcrawler(url)
        for x in info:
            imgUrl=x['cover_url']
            image = requests.get(imgUrl).content
            i+=1
            with open(('E:\工作区\Rainyspace\Python基础\爬虫基础\\'+'豆瓣动作电影排行榜\\'+str(i)+'.'+x['title']+'.gif'), 'wb') as f:
                f.write(image)
            print('%s.电影：%s 地区：%s 评分：%s 上映日期：%s'%(str(i),x['title'],[m for m in x['regions']],x['rating'][0],x['release_date']))
            moiveinfo='%s.电影：%s 地区：%s 评分：%s 上映日期：%s'%(str(i),x['title'],[m for m in x['regions']],x['rating'][0],x['release_date'])
            allmoiveinfo += moiveinfo + '\n'
    print('动作电影排行榜抓取完毕，共抓取%d个动作电影信息'%i)
    with open(os.path.join(os.getcwd(), '豆瓣动作电影排行榜.txt'), 'wb') as f:
        pickle.dump(allmoiveinfo,f)
    print('动作电影排行榜信息写入文件完毕，共写入%d个动作电影信息' % i)
def zhuaxiju():
    i=0
    allmoiveinfo=''
    print('喜剧电影信息抓取中...')
    for x in range(0, 5 + 1):
        url = 'https://movie.douban.com/j/chart/top_list?type=' \
              '24&interval_id=100%3A90&action=&start='\
              + str(x * 20) + '&limit=20'
        info=ajaxcrawler(url)
        for x in info:
            imgUrl=x['cover_url']
            image = requests.get(imgUrl).content
            i+=1
            with open(('E:\工作区\Rainyspace\Python基础\爬虫基础\\'+'豆瓣喜剧电影排行榜\\'+str(i)+'.'+x['title']+'.gif'), 'wb') as f:
                f.write(image)
            print('%s.电影：%s 地区：%s 评分：%s 上映日期：%s'%(str(i),x['title'],[m for m in x['regions']],x['rating'][0],x['release_date']))
            moiveinfo='%s.电影：%s 地区：%s 评分：%s 上映日期：%s'%(str(i),x['title'],[m for m in x['regions']],x['rating'][0],x['release_date'])
            allmoiveinfo+=moiveinfo+'\n'
    print('喜剧电影排行榜抓取完毕，共抓取%d个动作电影信息' % i)
    with open(os.path.join(os.getcwd(), '豆瓣喜剧电影排行榜.txt'), 'wb') as f:
        pickle.dump(allmoiveinfo,f)
    print('喜剧电影排行榜信息写入文件完毕，共写入%d个动作电影信息'%i )
zhuaction()
zhuaxiju()
def xijulist():
    with open(os.path.join(os.getcwd(), '豆瓣喜剧电影排行榜.txt'), 'rb') as f:
        xijulist=pickle.load(f)
    print(xijulist)
xijulist()
