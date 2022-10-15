from data.localVar import *

import requests

#高德地图公交路径规划
transitUrl = "https://restapi.amap.com/v3/direction/transit/integrated"

#用高德地图API获取公共交通规划路径数据
def getRouteDetail(origin):
    paramdata = {'origin': origin, 'destination': destionationLocation, 'city': mycity, 'output': "xml",
                 'key': mykey}
    res = requests.get(transitUrl, params=paramdata)
    source = res.text
    return source


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    pass
