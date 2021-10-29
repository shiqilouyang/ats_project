import requests
import json

def test_mainnet_miner_active(fivetoken_mainnet_url,fivetoken_mainnet_multisig_address):

    ''' 获取 Owner 活跃矿工列表 '''
    # owner
    url0 = fivetoken_mainnet_url+'/owner/miner/active?address=f0137992'
    # multisig
    # url2 = fivetoken_mainnet_url+'/owner/miner/active?address={}'.format(fivetoken_mainnet_multisig_address)

    header = {'Content-Type': 'application/json'}

    # storage_miner
    re = requests.get(url0,headers=header)
    try:
        assert len(json.loads(re.text).get("data").get("miners")) !=[]
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url0)
        assert len(json.loads(re.text).get("data").get("miners")) !=[]

    # f2 地址
    # re = requests.get(url2,headers=header)
    # try:
    #     assert json.loads(re.text).get("data").get("miners") !=[]
    # except  AttributeError as e:
    #     print(json.loads(re.text))



def test_calibration_miner_active(fivetoken_calibration_url,fivetoken_calibration_multisig_address):
    ''' 获取 Owner 活跃矿工列表 '''

    # owner
    url0 = fivetoken_calibration_url+'/owner/miner/active?address=t01119'
    # multisig
    # url2 = fivetoken_calibration_url+'/owner/miner/active?address={}'.format(fivetoken_calibration_multisig_address)


    header = {'Content-Type': 'application/json'}

    # f0地址
    re = requests.get(url0,headers=header)
    try:
        assert len(json.loads(re.text).get("data").get("miners")) !=[]
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url0)
        assert len(json.loads(re.text).get("data").get("miners")) !=[]

    # f2 地址
    # re = requests.get(url2,headers=header)
    # try:
    #     assert len(json.loads(re.text).get("data").get("miners")) !=[]
    # except  AttributeError as e:
    #     print(json.loads(re.text))
