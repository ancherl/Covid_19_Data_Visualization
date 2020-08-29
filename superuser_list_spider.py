# 1. 获取 Power Apps Community 近一个 活跃的 Super User 信息
# 2. 将获取到Super User 信息保存为一个Excel 文件

import requests

from lxml import etree

# 引入Excel  相关库
import xlwt

baseUrl = "https://powerusers.microsoft.com/t5/kudos/kudosleaderboardpage/category-id/PowerApps1/timerange/one_month/page/1/tab/authors"

headers = {

    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

}

cookies = {
    'Cookie': "MC1=GUID=49c54d8949854218a5ba9c4aefb7d689&HASH=49c5&LV=202008&V=4&LU=1598085929757; at_check=true; mbox=session#fedcf56a454d4d1b86b2e65da1ab9c12#1598088035|PC#fedcf56a454d4d1b86b2e65da1ab9c12.38_0#1661330976; AADNonce=6acf41df-a7c5-42cd-88c2-a6da6516e4ee.637342686164800313; ak_bmsc=FF7E85F21BFE7D5988890EFCF9C094A517DBACAD31620000C8CB495F61317A52~plMTygXQRDg4tIfiwf5Ibjhxa0iNfxA5YFtZI7cNMyJ9hwnzC+IkHfIaFqlCnHHI9RPc66J1PGRs0j5bVM6omDi3+80tpCnHkZrLm7ruqiJjnrWCa5pjh5TYJIJ4VIp67LlUDaiCYM8MikDHPpVVyCffwCA5YaoB3/I7bNPWcIdEvtsX6U15kp4MBWmCaDSiFbLcqebCNBfv/vk9ubQOHdJ/t/3OnuiV3d4pb5qDl79J8=; LiSESSIONID=D640AFE414EC6C5DF510F6D7390B2240; ValueSurveyParticipation=1598673226548; LithiumVisitor=~289GJWSQqScVCBWAr~KiSfFul7cHPCwLZkAsgLLmTRw1FX9g7pAZdozjK1e0vd6hSu1-cUfdTVCKetTHwMAJbDbVSxGZsrmBKRj-kjPw..; VISITOR_BEACON=~2ARWlwqE2wnY9J416~UstdPZxQXj69ungiwa0LFDnZv4u3OwT5NQB-Dbm0u_x3SwcnpNsPgsyHKqCE5ZAIMKkcLatzRvWopFGGP2zt3A.."
}

# 实例化xls文件对象
wb = xlwt.Workbook()
sheet1 = wb.add_sheet('Super User List')
sheet1.write(0,0, 'Author Name')
sheet1.write(0,1, 'Profile Link')
sheet1.write(0,2,'Role')
sheet1.write(0,3, 'Rank')

response = requests.request('GET', baseUrl, headers=headers, cookies=cookies)
# response.encoding = 'utf-8'

elements = etree.HTML(response.text)
authors = elements.xpath('//div[@id="authors"]//div[contains(@class, "lia-quilt-column-alley") and contains(@class, "lia-quilt-column-alley-single")]/div[contains(@class, "UserSearchItemContainer")]')

SuperUser_List = []

for item in authors:
    rank = item.xpath('.//div[contains(@class, "lia-user-position") and contains(@class, "lia-component-user-position")]/div[@class="lia-user-position-wrapper"]/text()')[0]
    # author_image = 'https://powerusers.microsoft.com' + item.xpath('.//a[contains(@class, "UserAvatar") and contains(@class, "lia-link-navigation")]/img[@class="lia-user-avatar-message"]/@src')[0]
    author_rank_title = item.xpath('.//div[@class="lia-user-name-and-simple-rank-wrapper"]/span[@class="lia-user-rank-container"]/span/text()')[0]
    author_name = item.xpath('.//div[@class="lia-user-name-and-simple-rank-wrapper"]/span[contains(@class, "UserName")]/a[contains(@class, "lia-link-navigation")]/span/text()')[0]
    profile_link = item.xpath('.//div[@class="lia-user-name-and-simple-rank-wrapper"]/span[contains(@class, "UserName")]/a[contains(@class, "lia-link-navigation")]/@href')[0]

    # print(author_name, '--', author_image, '--', str(rank), '--', author_rank_title)

    if 'Super User' in author_rank_title:
        SuperUser_List.append({'Author Name': author_name, 'Profile Link': profile_link, 'Role': author_rank_title, 'Rank': rank})

# 循环写入Excel
# 定义行索引
i = 1
for item in SuperUser_List:
    # 定义列索引
    j = 0
    for value in item.values():
        sheet1.write(i, j, value)
        j += 1
    i += 1

wb.save('Super User List.xls')
