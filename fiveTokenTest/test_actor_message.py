import requests
import json

def test_mainnet_actor_message(fivetoken_mainnet_url,fivetoken_mainnet_bls,fivetoken_mainnet_multisig_address):
    ''' 查询地址普通消息列表 '''

    header = {'Content-Type': 'application/json'}

    # f2 地址
    url = fivetoken_mainnet_url+'/actor/messages?direction=down&limit=10&actor={}'.format(fivetoken_mainnet_multisig_address)
    url_down_mid = fivetoken_mainnet_url+'/actor/messages?direction=down&limit=10&actor={}&mid={}'.format(fivetoken_mainnet_multisig_address,116552300242)
    url_up_mid = fivetoken_mainnet_url+'/actor/messages?direction=up&limit=10&actor={}&mid={}'.format(fivetoken_mainnet_multisig_address,116552300242)


    # 新地址
    url1 = fivetoken_mainnet_url + '/actor/messages?direction=down&limit=10&actor={}'.format(fivetoken_mainnet_bls)

    re = requests.get(url,headers=header)
    try:
        assert json.loads(re.text).get("data").get("messages") is not None
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url)
        assert json.loads(re.text).get("data").get("messages") is not None

    re = requests.get(url1,headers=header)
    try:
        assert json.loads(re.text).get("data").get('messages') is None
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url1)
        assert json.loads(re.text).get("data").get('messages') is None
    re = requests.get(url_down_mid, headers=header)
    try:
        assert json.loads(re.text).get("data").get('messages')[-1]['mid'] == '116553000300'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception as e:
        print(url_down_mid)
        assert json.loads(re.text).get("data").get('messages')[-1]['mid'] == '116553000300'
    re = requests.get(url_up_mid, headers=header)
    try:
        assert json.loads(re.text).get("data").get('messages')[-1]['mid'] == '114222200315'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url_up_mid)
        assert json.loads(re.text).get("data").get('messages')[-1]['mid'] == '114222200315'






def test_calibration_actor_message(fivetoken_calibration_url,fivetoken_calibration_bls,fivetoken_calibration_multisig_address):
    ''' 查询地址普通消息列表 '''

    header = {'Content-Type': 'application/json'}

    # f2 地址
    url = fivetoken_calibration_url+'/actor/messages?direction=down&limit=10&actor={}'.format(fivetoken_calibration_multisig_address)
    url_down_mid = fivetoken_calibration_url+'/actor/messages?direction=down&limit=10&actor={}&mid={}'.format(fivetoken_calibration_multisig_address,29188600024)
    url_up_mid = fivetoken_calibration_url+'/actor/messages?direction=up&limit=10&actor={}&mid={}'.format(fivetoken_calibration_multisig_address,29188900022)

    # 新地址
    url1 = fivetoken_calibration_url+'/actor/messages?direction=down&limit=10&actor={}'.format(fivetoken_calibration_bls)

    re = requests.get(url,headers=header)
    try:
        assert json.loads(re.text).get("data").get('messages') is not None
    except  AttributeError as e:
        print(json.loads(re.text))
    re = requests.get(url1,headers=header)
    try:
        assert json.loads(re.text).get("data").get('messages') is None
    except  AttributeError as e:
        print(json.loads(re.text))

    re = requests.get(url_down_mid, headers=header)
    try:
        assert json.loads(re.text).get("data").get('messages')[-1]['mid'] == '29188900022'
    except  AttributeError as e:
        print(json.loads(re.text))
    re = requests.get(url_up_mid, headers=header)
    try:
        assert json.loads(re.text).get("data").get('messages')[-1]['mid'] == '26038900004'
    except  AttributeError as e:
        print(json.loads(re.text))
