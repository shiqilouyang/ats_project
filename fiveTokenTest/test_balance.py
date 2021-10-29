import requests
import json

def test_mainnetActorbalance(fivetoken_mainnet_url,fivetoken_mainnet_bls,fivetoken_mainnet_multisig_address):

    ''' 获取地址余额 '''
    # f0地址
    url0 = fivetoken_mainnet_url+'/actor/balance?actor=f02438'
    # f2地址
    url2 = fivetoken_mainnet_url+'/actor/balance?actor={}'.format(fivetoken_mainnet_multisig_address)
    # f1 地址
    url1 = fivetoken_mainnet_url+'/actor/balance?actor=f1ok3h7ylmp7aybzw4cb36h4hmuadbzqom3p5c25q'
    # 新地址
    url3 = fivetoken_mainnet_url+'/actor/balance?actor={}'.format(fivetoken_mainnet_bls)

    header = {'Content-Type': 'application/json'}

    # f0地址
    re = requests.get(url0,headers=header)
    try:
        assert json.loads(re.text).get("data").get("balance") != None
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url0)
        assert json.loads(re.text).get("data").get("balance") != None
    # f1 地址
    re = requests.get(url1,headers=header)
    try:
        assert json.loads(re.text).get("data").get("balance") != None
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url1)
        assert json.loads(re.text).get("data").get("balance") != None
    # f2 地址
    re = requests.get(url2,headers=header)
    try:
        assert json.loads(re.text).get("data").get("balance") != None
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url2)
        assert json.loads(re.text).get("data").get("balance") != None
    # 新地址
    re = requests.get(url3,headers=header)
    try:
        assert json.loads(re.text).get("data") is None
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url3)
        assert json.loads(re.text).get("data") is None



def test_calibrationActorbalance(fivetoken_calibration_url,fivetoken_calibration_bls,fivetoken_calibration_multisig_address):
    ''' 获取地址余额 '''
    # t0地址
    url0 = fivetoken_calibration_url+'/actor/balance?actor=t01247'
    # t2地址
    url2 = fivetoken_calibration_url+'/actor/balance?actor={}'.format(fivetoken_calibration_multisig_address)
    # t1 地址
    url1 = fivetoken_calibration_url+'/actor/balance?actor=t1d2hc5meuprqgt7x2rswe5zhi64n3v5i7vutw2ia'
    # 新地址
    url3 = fivetoken_calibration_url+'/actor/balance?actor={}'.format(fivetoken_calibration_bls)

    header = {'Content-Type': 'application/json'}

    # f0地址
    re = requests.get(url0,headers=header)
    try:
        assert json.loads(re.text).get("data").get("balance") != None
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url0)
        assert json.loads(re.text).get("data").get("balance") != None
    # f1 地址
    re = requests.get(url1,headers=header)
    try:
        assert json.loads(re.text).get("data").get("balance") != None
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url1)
        assert json.loads(re.text).get("data").get("balance") != None
    # f2 地址
    re = requests.get(url2,headers=header)
    try:
        assert json.loads(re.text).get("data").get("balance") != None
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url2)
        assert json.loads(re.text).get("data").get("balance") != None
    # 新地址
    re = requests.get(url3,headers=header)
    try:
        assert json.loads(re.text).get("data") is None
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url3)
        assert json.loads(re.text).get("data") is None
