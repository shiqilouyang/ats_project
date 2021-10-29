import requests
import json


def test_mainnet_propose_detail(fivetoken_mainnet_url,fivetoken_mainnet_no_exist_message,fivetoken_mainnet_SysErrInsufficientFunds_message):
    ''' 获取 Propose 详情 '''

    header = {'Content-Type': 'application/json'}

    ''' 消息详情 '''
    url = fivetoken_mainnet_url+'/message?cid={}'.format('bafy2bzacebf2rmg5nn66hhkkkpcxnuwb2i5zjawkwvmtzz2ze6nwzys3brii4')

    # 不存在的消息
    url1 = fivetoken_mainnet_url + '/message?cid={}'.format(fivetoken_mainnet_no_exist_message)

    # 失败的消息
    url2 = fivetoken_mainnet_url+'/message?cid={}'.format(fivetoken_mainnet_SysErrInsufficientFunds_message)


    re = requests.get(url,headers=header)
    try:
        assert json.loads(re.text).get("data").get("from") != None
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url)
        assert json.loads(re.text).get("data").get("from") != None

    re = requests.get(url1,headers=header)
    try:
        assert json.loads(re.text).get("data") is None
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url1)
        assert json.loads(re.text).get("data") is None

    re = requests.get(url2,headers=header)
    try:
        assert json.loads(re.text).get("data").get("exit_code") == 6
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url2)
        assert json.loads(re.text).get("data").get("exit_code") == 6





def test_calibration_propose_detail(fivetoken_calibration_url,fivetoken_calibration_exist_message,fivetoken_calibration_no_exist_message,fivetoken_calibration_SysErrInsufficientFunds_message):
    ''' 获取 Propose 详情 '''


    header = {'Content-Type': 'application/json'}

    # 存在的消息
    url = fivetoken_calibration_url+'/message?cid={}'.format('bafy2bzaceam7i4p6km4e44kov5k6pbpxaelmt2ttubdjhzx7wdbvqmhdghadq')
    # 不存在的消息
    url1 = fivetoken_calibration_url+'/message?cid={}'.format(fivetoken_calibration_no_exist_message)

    # 失败的消息
    url2 = fivetoken_calibration_url+'/message?cid={}'.format(fivetoken_calibration_SysErrInsufficientFunds_message)

    re = requests.get(url,headers=header)
    try:
        assert json.loads(re.text).get("data").get("from") != None
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url)
        assert json.loads(re.text).get("data").get("from") != None
    re = requests.get(url1,headers=header)
    try:
        assert json.loads(re.text).get("data") is None
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url1)
        assert json.loads(re.text).get("data") is None
    re = requests.get(url2,headers=header)
    try:
        assert json.loads(re.text).get("data").get("exit_code") == 6
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url2)
        assert json.loads(re.text).get("data").get("exit_code") == 6


