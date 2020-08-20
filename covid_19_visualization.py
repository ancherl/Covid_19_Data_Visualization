import requests

import json

# 导入pyecharts包

from pyecharts.charts import Bar

from pyecharts import options as opt

from pyecharts.charts import Calendar

from pyecharts.charts import Map

from pyecharts.faker import Faker

# 设计目标:

# 1. 爬取国内疫情数据

#    经分析疫情的实时数据， 实际上是通过json 数据加载进来的， 找到对应的发送改请求的url

# 2. 对爬取到的数据进行可视化分析


# 疫情实时数据

baseUrl = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',

}

# cookies = {

#     'Cookie': '_ga=GA1.2.8165382.1595999416; ifVisitOldVerBBS=false; __utma=17875052.8165382.1595999416.1597632369.1597632369.1; __utmc=17875052; __utmz=17875052.1597632369.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmb=17875052.1.10.1597632369; JUTE_SESSION_ID=fea6a155-9f61-4382-bdd9-e747b1814081; CMSSESSIONID=50C0E8BEC4B52D401EBE17C3FF428292-n2; Hm_lvt_8a6dad3652ee53a288a11ca184581908=1597632370; Hm_lpvt_8a6dad3652ee53a288a11ca184581908=1597632370'

# }


response = requests.request('GET', baseUrl, headers=headers, )

response.encoding = 'utf-8'

json_str = response.text

json_data = json.loads(json_str)

china_area = json.loads(json_data.get('data')).get('areaTree')[0]

province_list = []

now_confirmed_list = []

for item in china_area.get('children'):
    province_list.append(item.get('name'))

    now_confirmed_list.append(item.get('total').get('nowConfirm'))

# print(province_list)

# print(now_confirmed_list)


# bar = Bar()

# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])

# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])

# bar.set_global_opts(title_opts=opt.TitleOpts(title='主标题', subtitle='副标题'),

#                     datazoom_opts=opt.DataZoomOpts(is_show=True, type_='slider', range_end=100,), visualmap_opts=opt.VisualMapOpts(max_=100), )


# bar.render('bar_chart.html')

# 构建map所需的二维数组
data = [list(z) for z in zip(province_list, now_confirmed_list)]

# 疫情数据渲染

map = Map()

map.add(series_name='中国各省最新疫情数据', data_pair=data, maptype='china')

map.set_global_opts(title_opts=opt.TitleOpts(

    title='中国各省最新疫情数据'), visualmap_opts=opt.VisualMapOpts(max_=1000))

map.render('map_chart.html')