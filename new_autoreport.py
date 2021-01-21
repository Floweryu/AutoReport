import json

import requests
import urllib3

url = "https://eai.buct.edu.cn/ncov/wap/default/save"

users = [
    {
        'name': '',
        'address': '',
        "position": {
            "Q": '',
            "R": '', 
            "lng": '', 
            "lat": ''
        }, 
        "citycode": "", 
        "adcode": "", 
        'area': '',  # 手机定位地址
        'province': '',    # 所在省
        'city': '',   # 所在市,
        'cookies': {
            'eai-sess': '',
            'UUkey': ''
        }
    }
]

def auto_report(user):
    urllib3.disable_warnings()
    # init
    s = requests.session()
    headers = {}
    data = {
        'ismoved': '0',  # 是否在校
        'jhfjrq': '',
        'jhfjjtgj': '',
        'jhfjhbcc': '',
        'sfxk': '0',
        'xkqq': '',
        'szgj': '',
        'szcs': '',
        'zgfxdq': '0',
        'mjry': '0',
        'csmjry': '0',
        'tw': '3',  # 体温范围（下标从 1 开始），此处是36.6 - 36.9
        'sfcxtz': '0',
        'sfjcbh': '0',
        'sfcxzysx': '',
        'qksm': '',
        'sfyyjc': '0',
        'jcjgqr': '0',
        'remark': '',
        'address': user['address'],
        'geo_api_info': {
            "type": "complete", 
            "info": "SUCCESS", 
            "status": 1, 
            "$Da": "jsonp_546186_", 
            "position": user['position'], 
            "message": "Get ipLocation success.Get address success.", 
            "location_type": "ip", 
            "accuracy": None, 
            "isConverted": True, 
            "addressComponent": {
                "citycode": user['citycode'], 
                "adcode": user['adcode'], 
                "businessAreas": [], 
                "neighborhoodType": "", 
                "neighborhood": "", 
                "building": "", 
                "buildingType": "", 
                "street": "", 
                "streetNumber": "", 
                "country": "", 
                "province": "", 
                "city": "", 
                "district": "", 
                "township": ""
            }, 
            "formattedAddress": "", 
            "roads": [], 
            "crosses": [], 
            "pois": []
        },
        'area': user['area'],  # 手机定位地址
        'province': user['province'],    # 所在省
        'city': user['city'],   # 所在市
        'sfzx': '0',
        'sfjcwhry': '0',
        'sfjchbry': '0',
        'sfcyglq': '0',  # 是否处于隔离期
        'gllx': '',
        'glksrq': '',
        'jcbhlx': '',
        'jcbhrq': '',
        'bztcyy': '',
        'sftjhb': '0',
        'sftjwh': '0',
        'sfsfbh': '0',
        'xjzd': '',
        'jcwhryfs': '',
        'jchbryfs': '',
        'szsqsfybl': '0',
        'sfygtjzzfj': '',
        'gtjzzfjsj': '',
        'gtjzzchdfh': '',
        'fjqszgjdq': '',
        'jcjg': '',
    }

    result = s.post(url, data=data, headers=headers,
                    cookies=user['cookies'], verify=False)
    print(user['name'] + ':' + json.loads(result.text)['m'])

if __name__ == '__main__':
    for item in users:
        auto_report(item)

