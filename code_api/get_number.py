import requests

#定义一个获取手机号码的方法，参数为项目编号
qj_number =''
def get_number(xmid):
    Result = requests.get('http://vip.fxyzm.com:9180/service.asmx/GetHM2Str?token=F2EBB882100BD51AE936578E0245714B&xmid=%s&sl=1&lx=0&a1=&a2=&pk=&ks=0&rj='% xmid)
    new_crazy = filter(str.isdigit, Result.text)
    number = (''.join(list(new_crazy)))
    print(number)
    qj_number = number
    release = requests.get('http://vip.fxyzm.com:9180/service.asmx/sfHmStr?token=F2EBB882100BD51AE936578E0245714B&hm=%s' % number)
    print(release.text)

#get_number(77765)
def Verification():
    headers = {
        "Accept-Encoding: gzip",
        "Accept-Language: zh-CN,zh;q=0.8",
        "Content-Type: application/x-www-form-urlencoded",
        "User-Agent: Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
    url = 'https://api.chehezhi.cn/customer/accountSafe/getRegisterVerificationCode'
    data = {'phone': qj_number, 'deviceType': '1'}
    verification = requests.post(url, headers, data)
    print(verification.text)
def main():
    get_number(77765)
    #Verification()

if __name__ == '__main__':
    main()