from pprint import pprint

import requests

"""
POST https://api-sams.walmartmobile.cn/api/v1/sams/decoration/portal/show/getPageData HTTP/1.1


"""
headers = {
    'Host': 'api-sams.walmartmobile.cn',
    'Connection': 'keep-alive',
    'Content-Length': '546',
    'device-type': 'mini_program',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; HMA-AL00 Build/HUAWEIHMA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045130 Mobile Safari/537.36 MMWEBID/2679 MicroMessenger/7.0.10.1580(0x27000A59) Process/tools NetType/4G Language/zh_CN ABI/arm64',
    'Content-Type': 'application/json;charset=UTF-8',
    'xweb_xhr': '1',
    'system-language': 'CN',
    # 'treq-id':'48d2653329744ac7840321a539aa6710.303.17012683610800000',
    'rcs': '3',
    # 'auth-token':'740d926b981716f4d4d3bf048e830799cec2d98baaac380693dbf9dec797315c0c60e6345685b46681a1c23129bdffadf5e5b58c075bf613',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://servicewechat.com/wxb344a8513eaaf849/302/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
data = {"pageContentId": "274049627718815766", "modulePagination": True, "pageNum": 1, "pageSize": 20,
        "latitude": 21.544656, "longitude": 115.012133,
        "storeInfoList": [{"storeId": "9991", "storeType": 32, "storeDeliveryAttr": [10]},
                          {"storeId": "6758", "storeType": 256, "storeDeliveryAttr": [2, 3, 4, 5, 6, 9, 12, 13]},
                          {"storeId": "6505", "storeType": 2, "storeDeliveryAttr": [7]},
                          {"storeId": "6672", "storeType": 4, "storeDeliveryAttr": [3, 4]},
                          {"storeId": "9992", "storeType": 8, "storeDeliveryAttr": [1]}], "isOpenRecommend": True,
        "uid": "181838611733",
        "appId": "wxb344a8513eaaf849", "saasId": "1818"
        }
r = requests.get("https://api-sams.walmartmobile.cn/api/v1/sams/decoration/portal/show/getPageData",headers=headers, json=data, verify=False)

r.encoding = "utf-8"
pprint(r.json())
print(r.status_code)
"""
POST https://api-sams.walmartmobile.cn/api/v1/sams/goods-portal/spu/queryDetail HTTP/1.1
Host: api-sams.walmartmobile.cn
Connection: keep-alive
Content-Length: 6899
device-type: mini_program
longitude: 114.012133
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309080f)XWEB/8461
Content-Type: application/json;charset=UTF-8
xweb_xhr: 1
system-language: CN
treq-id: e5f86c97ce7941a38bff215bdab1b245.303.17012693580900000
rcs: 3
auth-token: 740d926b981716f4d4d3bf048e830799cec2d98baaac380693dbf9dec797315c0c60e6345685b46681a1c23129bdffadf5e5b58c075bf613
latitude: 22.544656
Accept: */*
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://servicewechat.com/wxb344a8513eaaf849/302/page-frame.html
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9

{"channel":112,"spuId":"225043177","storeInfoVOList":[{"storeId":"9991","storeName":"全球购美国直邮","storeNum":None,"storeLogo":None,"storeAddress":"印力中心","provinceName":None,"provinceCode":None,"cityName":None,"cityCode":None,"districtName":None,"districtCode":None,"longitude":None,"latitude":None,"storeTel":None,"storeBusiness":None,"deliveryTypeList":None,"isDefault":None,"address":None,"storeType":32,"storeRecmdDeliveryTemplateData":{"id":None,"storeDeliveryTemplateId":"1387134513670399254","storeDeliveryId":"942251494118458134","saasId":None,"storeId":None,"freightTemplateId":"626233881414216726","performanceTemplateId":"1009101603233623318","isOpened":1,"isDeleted":None,"createTime":None,"operator":None,"updateTime":None},"storeDeliveryModeVerifyData":{"deliveryModeId":"1014","modeName":"美国直邮","priority":14,"goodsDeliveryAttri":"10","deliveryType":2,"isUsed":1,"performanceTemplateId":None,"packingExpense":"0","packingComment":None,"packingCommentEn":None},"storeAreaBlockVerifyData":{"areaBlockId":"42522","storeAddress":"印力中心","provinceName":"广东省","provinceCode":"440000","cityName":"深圳市","cityCode":"440300","districtName":"","districtCode":"","blockName":"深圳市","blockType":4,"isUsed":1},"deliveryModeGoodAddriList":[10],"allDeliveryAttrList":[10],"storeDeliveryAttr":[10]},{"storeId":"6758","storeName":"深圳山姆电商拣货中心","storeNum":None,"storeLogo":None,"storeAddress":"龙华街道清祥路23号德信昌工业园B栋102号","provinceName":None,"provinceCode":None,"cityName":None,"cityCode":None,"districtName":None,"districtCode":None,"longitude":None,"latitude":None,"storeTel":None,"storeBusiness":None,"deliveryTypeList":None,"isDefault":None,"address":None,"storeType":256,"storeRecmdDeliveryTemplateData":{"id":None,"storeDeliveryTemplateId":"750842649874934806","storeDeliveryId":"533048063783322902","saasId":None,"storeId":None,"freightTemplateId":"276864346481630742","performanceTemplateId":"1447766009145757718","isOpened":1,"isDeleted":None,"createTime":None,"operator":None,"updateTime":None},"storeDeliveryModeVerifyData":{"deliveryModeId":"1003","modeName":"生鲜直送","priority":2,"goodsDeliveryAttri":"3","deliveryType":2,"isUsed":1,"performanceTemplateId":None,"packingExpense":"100","packingComment":None,"packingCommentEn":None},"storeAreaBlockVerifyData":{"areaBlockId":"291201964988089366","storeAddress":"龙华街道清祥路23号德信昌工业园B栋102号","provinceName":"广东省","provinceCode":"440000","cityName":"深圳市","cityCode":"440300","districtName":"福田区","districtCode":"440304","blockName":"福田区A","blockType":2,"isUsed":1},"deliveryModeGoodAddriList":[3],"allDeliveryAttrList":[2,3,4,5,6,9,12,13],"storeDeliveryAttr":[2,3,4,5,6,9,12,13]},{"storeId":"6505","storeName":"深圳福田店","storeNum":None,"storeLogo":None,"storeAddress":"农林路69号","provinceName":None,"provinceCode":None,"cityName":None,"cityCode":None,"districtName":None,"districtCode":None,"longitude":None,"latitude":None,"storeTel":None,"storeBusiness":None,"deliveryTypeList":None,"isDefault":None,"address":None,"storeType":2,"storeRecmdDeliveryTemplateData":{"id":None,"storeDeliveryTemplateId":"1828732014187119126","storeDeliveryId":"276857916378831126","saasId":None,"storeId":None,"freightTemplateId":"0","performanceTemplateId":"1148517699668974614","isOpened":1,"isDeleted":None,"createTime":None,"operator":None,"updateTime":None},"storeDeliveryModeVerifyData":{"deliveryModeId":"1005","modeName":"特殊订购自提（非标品自提）","priority":11,"goodsDeliveryAttri":"7","deliveryType":4,"isUsed":1,"performanceTemplateId":None,"packingExpense":"0","packingComment":None,"packingCommentEn":None},"storeAreaBlockVerifyData":{"areaBlockId":"35267","storeAddress":"农林路69号","provinceName":"广东省","provinceCode":"440000","cityName":"深圳市","cityCode":"440300","districtName":"福田区","districtCode":"440304","blockName":"福田区","blockType":1,"isUsed":1},"deliveryModeGoodAddriList":[7],"allDeliveryAttrList":[7],"storeDeliveryAttr":[7]},{"storeId":"6672","storeName":"深圳福田DC","storeNum":None,"storeLogo":None,"storeAddress":"广东省深圳市福田区车公庙天展大厦CD座一层","provinceName":None,"provinceCode":None,"cityName":None,"cityCode":None,"districtName":None,"districtCode":None,"longitude":None,"latitude":None,"storeTel":None,"storeBusiness":None,"deliveryTypeList":None,"isDefault":None,"address":None,"storeType":4,"storeRecmdDeliveryTemplateData":{"id":None,"storeDeliveryTemplateId":"317956692073651222","storeDeliveryId":"275582417509768982","saasId":None,"storeId":None,"freightTemplateId":"275212967627378454","performanceTemplateId":"1797674155173520918","isOpened":1,"isDeleted":None,"createTime":None,"operator":None,"updateTime":None},"storeDeliveryModeVerifyData":{"deliveryModeId":"1009","modeName":"极速达","priority":1,"goodsDeliveryAttri":"3,4","deliveryType":2,"isUsed":1,"performanceTemplateId":None,"packingExpense":"100","packingComment":None,"packingCommentEn":None},"storeAreaBlockVerifyData":{"areaBlockId":"312065619921076502","storeAddress":"广东省深圳市福田区车公庙天展大厦CD座一层","provinceName":"广东省","provinceCode":"440000","cityName":"深圳市","cityCode":"440300","districtName":"福田区","districtCode":"440304","blockName":"6672深圳福田DC","blockType":2,"isUsed":1},"deliveryModeGoodAddriList":[3,4],"allDeliveryAttrList":[3,4],"storeDeliveryAttr":[3,4]},{"storeId":"9992","storeName":"山姆全球购保税平潭仓","storeNum":None,"storeLogo":None,"storeAddress":"印力中心","provinceName":None,"provinceCode":None,"cityName":None,"cityCode":None,"districtName":None,"districtCode":None,"longitude":None,"latitude":None,"storeTel":None,"storeBusiness":None,"deliveryTypeList":None,"isDefault":None,"address":None,"storeType":8,"storeRecmdDeliveryTemplateData":{"id":None,"storeDeliveryTemplateId":"1743371277198079766","storeDeliveryId":"1631927832362038550","saasId":None,"storeId":None,"freightTemplateId":"626233881414216726","performanceTemplateId":"262282132641338902","isOpened":1,"isDeleted":None,"createTime":None,"operator":None,"updateTime":None},"storeDeliveryModeVerifyData":{"deliveryModeId":"1010","modeName":"全球购保税","priority":10,"goodsDeliveryAttri":"1","deliveryType":2,"isUsed":1,"performanceTemplateId":None,"packingExpense":"0","packingComment":None,"packingCommentEn":None},"storeAreaBlockVerifyData":{"areaBlockId":"42305","storeAddress":"印力中心","provinceName":"广东省","provinceCode":"440000","cityName":"","cityCode":"","districtName":"","districtCode":"","blockName":"广东省","blockType":3,"isUsed":1},"deliveryModeGoodAddriList":[1],"allDeliveryAttrList":[1],"storeDeliveryAttr":[1]}],"channelType":2,"storeId":"9992","uid":"181838611733","appId":"wxb344a8513eaaf849","saasId":"1818"}
"""

headers = {
    'Host': 'api-sams.walmartmobile.cn',
    'Connection': 'keep-alive',
    # 'Content-Length': '6899',
    'device-type': 'mini_program',
    # 'longitude': '114.012133',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309080f)XWEB/8461',
    'Content-Type': 'application/json;charset=UTF-8',
    'xweb_xhr': '1',
    'system-language': 'CN',
    # 'treq-id': 'e5f86c97ce7941a38bff215bdab1b245.303.17012693580900000',
    'rcs': '3',
    # 'auth-token': '740d926b981716f4d4d3bf048e830799cec2d98baaac380693dbf9dec797315c0c60e6345685b46681a1c23129bdffadf5e5b58c075bf613',
    # 'latitude': '22.544656',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://servicewechat.com/wxb344a8'
               '513eaaf849/302/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
data = {"channel": 112, "spuId": "225043177", "storeInfoVOList": [
    {"storeId": "9991", "storeName": "全球购美国直邮", "storeNum": None, "storeLogo": None, "storeAddress": "印力中心",
     "provinceName": None, "provinceCode": None, "cityName": None, "cityCode": None, "districtName": None,
     "districtCode": None, "longitude": None, "latitude": None, "storeTel": None, "storeBusiness": None,
     "deliveryTypeList": None, "isDefault": None, "address": None, "storeType": 32,
     "storeRecmdDeliveryTemplateData": {"id": None, "storeDeliveryTemplateId": "1387134513670399254",
                                        "storeDeliveryId": "942251494118458134", "saasId": None, "storeId": None,
                                        "freightTemplateId": "626233881414216726",
                                        "performanceTemplateId": "1009101603233623318", "isOpened": 1,
                                        "isDeleted": None, "createTime": None, "operator": None, "updateTime": None},
     "storeDeliveryModeVerifyData": {"deliveryModeId": "1014", "modeName": "美国直邮", "priority": 14,
                                     "goodsDeliveryAttri": "10", "deliveryType": 2, "isUsed": 1,
                                     "performanceTemplateId": None, "packingExpense": "0", "packingComment": None,
                                     "packingCommentEn": None},
     "storeAreaBlockVerifyData": {"areaBlockId": "42522", "storeAddress": "印力中心", "provinceName": "广东省",
                                  "provinceCode": "440000", "cityName": "深圳市", "cityCode": "440300",
                                  "districtName": "", "districtCode": "", "blockName": "深圳市", "blockType": 4,
                                  "isUsed": 1}, "deliveryModeGoodAddriList": [10], "allDeliveryAttrList": [10],
     "storeDeliveryAttr": [10]},
    {"storeId": "6758", "storeName": "深圳山姆电商拣货中心", "storeNum": None, "storeLogo": None,
     "storeAddress": "龙华街道清祥路23号德信昌工业园B栋102号", "provinceName": None, "provinceCode": None,
     "cityName": None, "cityCode": None, "districtName": None, "districtCode": None, "longitude": None,
     "latitude": None, "storeTel": None, "storeBusiness": None, "deliveryTypeList": None, "isDefault": None,
     "address": None, "storeType": 256,
     "storeRecmdDeliveryTemplateData": {"id": None, "storeDeliveryTemplateId": "750842649874934806",
                                        "storeDeliveryId": "533048063783322902", "saasId": None, "storeId": None,
                                        "freightTemplateId": "276864346481630742",
                                        "performanceTemplateId": "1447766009145757718", "isOpened": 1,
                                        "isDeleted": None, "createTime": None, "operator": None, "updateTime": None},
     "storeDeliveryModeVerifyData": {"deliveryModeId": "1003", "modeName": "生鲜直送", "priority": 2,
                                     "goodsDeliveryAttri": "3", "deliveryType": 2, "isUsed": 1,
                                     "performanceTemplateId": None, "packingExpense": "100", "packingComment": None,
                                     "packingCommentEn": None},
     "storeAreaBlockVerifyData": {"areaBlockId": "291201964988089366",
                                  "storeAddress": "龙华街道清祥路23号德信昌工业园B栋102号", "provinceName": "广东省",
                                  "provinceCode": "440000", "cityName": "深圳市", "cityCode": "440300",
                                  "districtName": "福田区", "districtCode": "440304", "blockName": "福田区A",
                                  "blockType": 2, "isUsed": 1}, "deliveryModeGoodAddriList": [3],
     "allDeliveryAttrList": [2, 3, 4, 5, 6, 9, 12, 13], "storeDeliveryAttr": [2, 3, 4, 5, 6, 9, 12, 13]},
    {"storeId": "6505", "storeName": "深圳福田店", "storeNum": None, "storeLogo": None, "storeAddress": "农林路69号",
     "provinceName": None, "provinceCode": None, "cityName": None, "cityCode": None, "districtName": None,
     "districtCode": None, "longitude": None, "latitude": None, "storeTel": None, "storeBusiness": None,
     "deliveryTypeList": None, "isDefault": None, "address": None, "storeType": 2,
     "storeRecmdDeliveryTemplateData": {"id": None, "storeDeliveryTemplateId": "1828732014187119126",
                                        "storeDeliveryId": "276857916378831126", "saasId": None, "storeId": None,
                                        "freightTemplateId": "0", "performanceTemplateId": "1148517699668974614",
                                        "isOpened": 1, "isDeleted": None, "createTime": None, "operator": None,
                                        "updateTime": None},
     "storeDeliveryModeVerifyData": {"deliveryModeId": "1005", "modeName": "特殊订购自提（非标品自提）", "priority": 11,
                                     "goodsDeliveryAttri": "7", "deliveryType": 4, "isUsed": 1,
                                     "performanceTemplateId": None, "packingExpense": "0", "packingComment": None,
                                     "packingCommentEn": None},
     "storeAreaBlockVerifyData": {"areaBlockId": "35267", "storeAddress": "农林路69号", "provinceName": "广东省",
                                  "provinceCode": "440000", "cityName": "深圳市", "cityCode": "440300",
                                  "districtName": "福田区", "districtCode": "440304", "blockName": "福田区",
                                  "blockType": 1, "isUsed": 1}, "deliveryModeGoodAddriList": [7],
     "allDeliveryAttrList": [7], "storeDeliveryAttr": [7]},
    {"storeId": "6672", "storeName": "深圳福田DC", "storeNum": None, "storeLogo": None,
     "storeAddress": "广东省深圳市福田区车公庙天展大厦CD座一层", "provinceName": None, "provinceCode": None,
     "cityName": None, "cityCode": None, "districtName": None, "districtCode": None, "longitude": None,
     "latitude": None, "storeTel": None, "storeBusiness": None, "deliveryTypeList": None, "isDefault": None,
     "address": None, "storeType": 4,
     "storeRecmdDeliveryTemplateData": {"id": None, "storeDeliveryTemplateId": "317956692073651222",
                                        "storeDeliveryId": "275582417509768982", "saasId": None, "storeId": None,
                                        "freightTemplateId": "275212967627378454",
                                        "performanceTemplateId": "1797674155173520918", "isOpened": 1,
                                        "isDeleted": None, "createTime": None, "operator": None, "updateTime": None},
     "storeDeliveryModeVerifyData": {"deliveryModeId": "1009", "modeName": "极速达", "priority": 1,
                                     "goodsDeliveryAttri": "3,4", "deliveryType": 2, "isUsed": 1,
                                     "performanceTemplateId": None, "packingExpense": "100", "packingComment": None,
                                     "packingCommentEn": None},
     "storeAreaBlockVerifyData": {"areaBlockId": "312065619921076502",
                                  "storeAddress": "广东省深圳市福田区车公庙天展大厦CD座一层", "provinceName": "广东省",
                                  "provinceCode": "440000", "cityName": "深圳市", "cityCode": "440300",
                                  "districtName": "福田区", "districtCode": "440304", "blockName": "6672深圳福田DC",
                                  "blockType": 2, "isUsed": 1}, "deliveryModeGoodAddriList": [3, 4],
     "allDeliveryAttrList": [3, 4], "storeDeliveryAttr": [3, 4]},
    {"storeId": "9992", "storeName": "山姆全球购保税平潭仓", "storeNum": None, "storeLogo": None,
     "storeAddress": "印力中心", "provinceName": None, "provinceCode": None, "cityName": None, "cityCode": None,
     "districtName": None, "districtCode": None, "longitude": None, "latitude": None, "storeTel": None,
     "storeBusiness": None, "deliveryTypeList": None, "isDefault": None, "address": None, "storeType": 8,
     "storeRecmdDeliveryTemplateData": {"id": None, "storeDeliveryTemplateId": "1743371277198079766",
                                        "storeDeliveryId": "1631927832362038550", "saasId": None, "storeId": None,
                                        "freightTemplateId": "626233881414216726",
                                        "performanceTemplateId": "262282132641338902", "isOpened": 1, "isDeleted": None,
                                        "createTime": None, "operator": None, "updateTime": None},
     "storeDeliveryModeVerifyData": {"deliveryModeId": "1010", "modeName": "全球购保税", "priority": 10,
                                     "goodsDeliveryAttri": "1", "deliveryType": 2, "isUsed": 1,
                                     "performanceTemplateId": None, "packingExpense": "0", "packingComment": None,
                                     "packingCommentEn": None},
     "storeAreaBlockVerifyData": {"areaBlockId": "42305", "storeAddress": "印力中心", "provinceName": "广东省",
                                  "provinceCode": "440000", "cityName": "", "cityCode": "", "districtName": "",
                                  "districtCode": "", "blockName": "广东省", "blockType": 3, "isUsed": 1},
     "deliveryModeGoodAddriList": [1], "allDeliveryAttrList": [1], "storeDeliveryAttr": [1]}], "channelType": 2,
        "storeId": "9992",
        # "uid": "181838611733", "appId": "wxb344a8513eaaf849",
        "saasId": "1818"}

# r = requests.post("https://api-sams.walmartmobile.cn/api/v1/sams/goods-portal/spu/queryDetail", headers=headers,
#                  json=data, verify=False)

# r.encoding = "utf-8"
# pprint(r.json())
# print(r.status_code)
