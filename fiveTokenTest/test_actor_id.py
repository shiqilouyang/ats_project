import requests
import json

def test_mainnetActorid(fivetoken_mainnet_url,fivetoken_mainnet_bls,fivetoken_mainnet_multisig_address):

    ''' 获取地址余额 '''
    # storage_miner
    url0 = fivetoken_mainnet_url+'/actor/id?address=f02438'
    # multisig
    url2 = fivetoken_mainnet_url+'/actor/id?address={}'.format(fivetoken_mainnet_multisig_address)
    # f1 地址
    url1 = fivetoken_mainnet_url+'/actor/id?address=f1acmjfresoxiqav6wn2uwdzkkfmu7hazixcoyqgy'
    # 新地址
    url3 = fivetoken_mainnet_url+'/actor/id?address={}'.format(fivetoken_mainnet_bls)

    header = {'Content-Type': 'application/json'}

    # storage_miner
    re = requests.get(url0,headers=header)
    try:
        assert json.loads(re.text).get("data") == 'f02438'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception as e:
        print(url0)
        assert json.loads(re.text).get("data") == 'f02438'

    # f1 地址
    re = requests.get(url1,headers=header)
    try:
        assert json.loads(re.text).get("data") == 'f0127848'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url1)
        assert json.loads(re.text).get("data") == 'f0127848'

    # f2 地址
    re = requests.get(url2,headers=header)
    try:
        assert json.loads(re.text).get("data") == 'f01170119'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception as e:
        print(url2)
        assert json.loads(re.text).get("data") == 'f01170119'

    # 新地址
    re = requests.get(url3,headers=header)
    try:
        assert json.loads(re.text).get("message") == 'network error'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception :
        print(url3)
        assert json.loads(re.text).get("message") == 'network error'




def test_calibrationActorid(fivetoken_calibration_url,fivetoken_calibration_bls,fivetoken_calibration_multisig_address):
    ''' 获取地址余额 '''
    # storage_miner
    url0 = fivetoken_calibration_url+'/actor/id?address=t03112'
    # multisig
    url2 = fivetoken_calibration_url+'/actor/id?address={}'.format(fivetoken_calibration_multisig_address)
    # account
    url1 = fivetoken_calibration_url+'/actor/id?address=t1rjrugxuhlike4jxrylumg7axk34pef6ii43drtq'
    # 新地址
    url3 = fivetoken_calibration_url+'/actor/id?address={}'.format(fivetoken_calibration_bls)

    header = {'Content-Type': 'application/json'}

    # f0地址
    re = requests.get(url0,headers=header)
    try:
        assert json.loads(re.text).get("data") == 't03112'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url0)
        assert json.loads(re.text).get("data") == 't03112'


    # f1 地址
    re = requests.get(url1,headers=header)
    try:
        assert json.loads(re.text).get("data") == 't090'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url1)
        assert json.loads(re.text).get("data") == 't090'
    # f2 地址
    re = requests.get(url2,headers=header)
    try:
        assert json.loads(re.text).get("data") == 't017880'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url2)
        assert json.loads(re.text).get("data") == 't017880'
    # 新地址
    re = requests.get(url3,headers=header)
    try:
        assert json.loads(re.text).get("message") == 'network error'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url3)
        assert json.loads(re.text).get("message") == 'network error'
