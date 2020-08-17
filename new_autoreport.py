import json

import requests
import urllib3

url = "https://eai.buct.edu.cn/xisuncov/wap/open-report/save"

if __name__ == '__main__':

    urllib3.disable_warnings()
    # init
    s = requests.session()
    headers = {}

    # report
    cookies = {}
    data = {
        'sfzx': '1',  # 是否在校
        'tw': '2',  # 体温范围（下标从 1 开始），此处是36 - 36.5
        'area': '北京市 昌平区',  # 所在区域
        'province': '北京市',  # 所在省
        'city': '北京市',  # 所在市
        'address': '北京市昌平区南口镇南涧路29号北京化工大学昌平校区',  # 地址
        'sfcyglq': '0',  # 是否处于隔离期
        'sfyzz': '0',  # 是否有症状
        'askforleave': '0',  # 是否请假外出
        'qtqk': '',  #其他情况
        'geo_api_info': {
            'type': 'complete',
            'info': 'SUCCESS',
            'status': 1,
            'Eia': 'jsonp_913580_',
            'position': {
                'O': 116.231204,  # 经度
                'P': 40.22066,  # 纬度
                'lng': 116.231204,  # 经度
                'lat': 40.22066  # 纬度
            },
            'message': 'Get+ipLocation+success.Get+address+success.',
            'location_type': 'ip',
            'accuracy': None,
            'isConverted': True,
            'addressComponent': {
                'citycode': '',
                'adcode': '',  # 行政区划代码
                'businessAreas': [],
                'neighborhoodType': '',
                'neighborhood': '',
                'building': '',
                'buildingType': '',
                'street': '',
                'streetNumber': '',
                'province': '',  # 所在省
                'city': '',  # 所在市
                'district': '',  # 所在区
                'township': ''  # 所在街道
            },
            'formattedAddress': '',  # 拼接后的地址
            'roads': [],
            'crosses': [],
            'pois': []
        },
    }


    name = ''
    cookies['eai-sess'] = ''
    result = s.post(url, data=data, headers=headers, cookies=cookies, verify=False)
    print(name + ':' + json.loads(result.text)['m'])