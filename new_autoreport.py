import json

import requests
import urllib3

url = "https://eai.buct.edu.cn/ncov/wap/default/save"

users = [
    {
        'name': '',
        'cookies': {
            'eai-sess': '',
            'UUkey': ''
        }
    },
    {
        'name': '',
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
        'sfyyjc': '0',
        'jcjgqr': '0',
        'remark': '',
        'address': '北京市朝阳区和平街街道北京化工大学北京化工大学东校区',
        'geo_api_info': {
            "type": "complete", 
            "info": "SUCCESS", 
            "status": 1, 
            "$Da": "jsonp_228523_", 
            "position": {
                "Q": 39.97203, 
                "R": 116.42286999999999, 
                "lng": 116.42287, 
                "lat": 39.97203
            }, 
            "message": "Get ipLocation success.Get address success.", 
            "location_type": "ip", 
            "accuracy": None, 
            "isConverted": True, 
            "addressComponent": {
                "citycode": "010", 
                "adcode": "110105", 
                "businessAreas": [
                    {
                        "name": "小关",
                        "id": "110105",
                        "location": {
                            "Q": 39.980391,
                            "R": 116.41376500000001,
                            "lng": 116.413765,
                            "lat": 39.980391
                        }
                    },
                    {
                        "name": "太阳宫村",
                        "id": "110105",
                        "location": {
                            "Q": 39.974437,
                            "R": 116.445607,
                            "lng": 116.445607,
                            "lat": 39.974437
                        }
                    },
                    {
                        "name": "和平里",
                        "id": "110101",
                        "location": {
                            "Q": 39.959266,
                            "R": 116.42125599999997,
                            "lng": 116.421256,
                            "lat": 39.959266
                        }
                    }
                ], 
                "neighborhoodType": "科教文化服务;学校;高等院校", 
                "neighborhood": "北京化工大学", 
                "building": "", 
                "buildingType": "", 
                "street": "北三环东路", 
                "streetNumber": "15号", 
                "country": "中国", 
                "province": "北京市", 
                "city": "", 
                "district": "朝阳区", 
                "township": "和平街街道"
            }, 
            "formattedAddress": "北京市朝阳区和平街街道北京化工大学北京化工大学东校区", 
            "roads": [], 
            "crosses": [], 
            "pois": []
        },
        'area': '北京市  朝阳区',  # 手机定位地址
        'province': '北京市',    # 所在省
        'city': '北京市',   # 所在市
        'sfzx': '1',
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
        'sfsfbh': '1',
        'xjzd': '北京市朝阳区北京化工大学东校区',
        'jcwhryfs': '',
        'jchbryfs': '',
        'szsqsfybl': '0',
        'sfygtjzzfj': '0',
        'gtjzzfjsj': '',
        'jcjg': '',
        'gtjzzchdfh': '',
        'fjqszgjdq': '',
        'fxyy': '返校注册，毕业设计'
    }

    result = s.post(url, data=data, headers=headers,
                    cookies=user['cookies'], verify=False)
    print(user['name'] + ':' + json.loads(result.text)['m'])

if __name__ == '__main__':
    for item in users:
        auto_report(item)

