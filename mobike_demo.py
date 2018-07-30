import requests, json, jsonpath

# 如果headers里面没有referer则会访问异常
# referer表示上一个页面是什么。
headers = {
'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E304 MicroMessenger/6.5.7 NetType/WIFI Language/zh_CN',
'Content-Type': 'application/x-www-form-urlencoded',
'Referer': 'https://servicewechat.com/wx80f809371ae33eda/23/page-frame.html',
}

url = 'https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do'

data = {
'longitude':'121.1883',# 经度
'latitude':'31.05147', # 纬度
'citycode':'021',
'errMsg':'getMapCenterLocation:ok'
}

response = requests.post(url,data=data,headers=headers)
rs_json = response.text
rs_py = json.loads(rs_json)
# print(rs_json)
# print(rs_py)

# 以下都要先把json转换为python对象, 进行操作

# Python数据结构的操作
rs_py_object = rs_py.get('object')
for i in rs_py_object:
    dis = i.get('distance')
    print(dis)

# jsonpath的操作
dis = jsonpath.jsonpath(rs_py, '$..distance')
print(dis)

