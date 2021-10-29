import requests
import json

def test_mainnetActortype(fivetoken_mainnet_url,fivetoken_mainnet_bls,fivetoken_mainnet_multisig_address):

    ''' 获取地址余额 '''
    # storage_miner
    url0 = fivetoken_mainnet_url+'/actor/type?address=f02438'
    # multisig
    url2 = fivetoken_mainnet_url+'/actor/type?address={}'.format(fivetoken_mainnet_multisig_address)
    # account
    url1 = fivetoken_mainnet_url+'/actor/type?address=f0127848'
    # 新地址
    url3 = fivetoken_mainnet_url+'/actor/type?address={}'.format(fivetoken_mainnet_bls)

    header = {'Content-Type': 'application/json'}

    # storage_miner
    re = requests.get(url0,headers=header)
    try:
        assert json.loads(re.text).get("data").get("type") == 'storage_miner'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url0)
        assert json.loads(re.text).get("data").get("type") == 'storage_miner'
    # f1 地址
    re = requests.get(url1,headers=header)
    try:
        assert json.loads(re.text).get("data").get("type") == 'account'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url1)
        assert json.loads(re.text).get("data").get("type") == 'account'
    # f2 地址
    re = requests.get(url2,headers=header)
    try:
        assert json.loads(re.text).get("data").get("type") == 'multisig'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url2)
        assert json.loads(re.text).get("data").get("type") == 'multisig'
    # 新地址
    re = requests.get(url3,headers=header)
    try:
        assert json.loads(re.text).get("data").get("exist") == False
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url3)
        assert json.loads(re.text).get("data").get("exist") == False


def test_calibrationActortype(fivetoken_calibration_url,fivetoken_calibration_bls,fivetoken_calibration_multisig_address):
    ''' 获取地址余额 '''
    # storage_miner
    url0 = fivetoken_calibration_url+'/actor/type?address=t03112'
    # multisig
    url2 = fivetoken_calibration_url+'/actor/type?address={}'.format(fivetoken_calibration_multisig_address)
    # account
    url1 = fivetoken_calibration_url+'/actor/type?address=t01163'
    # 新地址
    url3 = fivetoken_calibration_url+'/actor/type?address={}'.format(fivetoken_calibration_bls)

    header = {'Content-Type': 'application/json'}

    # f0地址
    re = requests.get(url0,headers=header)
    try:
        assert json.loads(re.text).get("data").get("type") == 'storage_miner'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url0)
        assert json.loads(re.text).get("data").get("type") == 'storage_miner'
    # f1 地址
    re = requests.get(url1,headers=header)
    try:
        assert json.loads(re.text).get("data").get("type") == 'account'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url1)
        assert json.loads(re.text).get("data").get("type") == 'account'
    # f2 地址
    re = requests.get(url2,headers=header)
    try:
        assert json.loads(re.text).get("data").get("type") == 'multisig'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url2)
        assert json.loads(re.text).get("data").get("type") == 'multisig'
    # 新地址
    re = requests.get(url3,headers=header)
    try:
        assert json.loads(re.text).get("data").get("exist") == False
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url3)
        assert json.loads(re.text).get("data").get("exist") == False
