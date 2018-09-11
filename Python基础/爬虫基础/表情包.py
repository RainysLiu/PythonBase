import requests
i=1
for m in range(0, 10):
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%A1%A8%E6%83%85%E5%8C%85&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%E8%A1%A8%E6%83%85%E5%8C%85&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&pn=' + str(
        30 * m) + '&rn=30&1517662599209='

    header = {

        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 60.0.3112.113Safari / 537.36'

    }

    html = requests.get(url, headers=header)



    html.encoding = 'utf-8'

    # 200

    # print(html.status_code)

    for n in range(30):
        # print(html.json()['data'][n]['thumbURL'])

        # 图片网址

        urll = html.json()['data'][n]['thumbURL']

        # 用于取名字

        #urls = html.json()['data'][n]['thumbURL'][-20:]
        # 以二进制方式
        urls=str(i)+'.gif'
        i+=1

        data = requests.get(urll).content

        # print(urls)

        with open('E:\Rainy\Pictures\表情包包\\' + urls, 'wb') as f:
            # 写入本地

            f.write(data)






