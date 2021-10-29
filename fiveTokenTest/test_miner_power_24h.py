import requests
import json

def test_mainnet_miner_power_24h(fivetoken_mainnet_url,fivetoken_mainnet_miner_address,fivetoken_mainnet_no_exist_miner_address):
    ''' 矿工基础指标统计 '''

    header = {'Content-Type': 'application/json'}

    ''' 消息详情 '''
    url = fivetoken_mainnet_url+'/miner/power/24h?address={}'.format(fivetoken_mainnet_miner_address)

    re = requests.get(url,headers=header)
    try:
        assert json.loads(re.text).get("data").get("blocks_rewards") !=None
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url)
        assert json.loads(re.text).get("data").get("blocks_rewards") !=None






# def test_calibration_miner_power_24h(fivetoken_calibration_url,fivetoken_calibration_miner_address,fivetoken_calibration_no_exist_miner_address):
#     ''' 矿工基础指标统计 '''
#
#     header =  {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
#
#     # 多签
#     url = fivetoken_calibration_url+'/miner/base?address={}'.format(fivetoken_calibration_miner_address)
#     print(url)
#     re = requests.get(url,headers=header)
#     try:
#         assert json.loads(re.text).get("data").get("epoch") is not None
#     except  AttributeError as e:
#         print(json.loads(re.text))