import requests
import json

def test_mainnet_recommend_fee(fivetoken_mainnet_url,fivetoken_mainnet_bls,fivetoken_mainnet_multisig_address):
    ''' 获取消息发送推荐手续费 '''

    header = {'Content-Type': 'application/json'}

    # f2 地址
    urlSend = fivetoken_mainnet_url+'/recommend/fee?method={}&actor={}'.format('Send',fivetoken_mainnet_multisig_address)
    urlApprove = fivetoken_mainnet_url+'/recommend/fee?method={}&actor={}'.format('Approve','f0164864')
    urlExec = fivetoken_mainnet_url+'/recommend/fee?method={}&actor={}'.format('Exec',fivetoken_mainnet_multisig_address)
    urlPropose = fivetoken_mainnet_url+'/recommend/fee?method={}&actor={}'.format('Propose',fivetoken_mainnet_multisig_address)


    re = requests.get(urlSend,headers=header)
    try:
        assert json.loads(re.text).get("data").get('method_name') == 'Send'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(urlSend)
        assert json.loads(re.text).get("data").get('method_name') == 'Send'


    re = requests.get(urlApprove,headers=header)
    try:
        assert json.loads(re.text).get("data").get('method_name') == 'Approve'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(urlApprove)
        assert json.loads(re.text).get("data").get('method_name') == 'Approve'


    re = requests.get(urlExec,headers=header)
    try:
        assert json.loads(re.text).get("data").get('method_name') == 'Exec'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(urlExec)
        assert json.loads(re.text).get("data").get('method_name') == 'Exec'


    re = requests.get(urlPropose,headers=header)
    try:
        assert json.loads(re.text).get("data").get('method_name') == 'Propose'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(urlPropose)
        assert json.loads(re.text).get("data").get('method_name') == 'Propose'







def test_calibration_recommend_fee(fivetoken_calibration_url,fivetoken_calibration_bls,fivetoken_calibration_multisig_address):
    ''' 获取消息发送推荐手续费 '''

    header = {'Content-Type': 'application/json'}

    # f2 地址
    urlSend = fivetoken_calibration_url + '/recommend/fee?method={}&actor={}'.format('Send', fivetoken_calibration_multisig_address)
    urlApprove = fivetoken_calibration_url + '/recommend/fee?method={}&actor={}'.format('Approve',
                                                                                    fivetoken_calibration_multisig_address)
    urlExec = fivetoken_calibration_url + '/recommend/fee?method={}&actor={}'.format('Exec', fivetoken_calibration_multisig_address)
    urlPropose = fivetoken_calibration_url + '/recommend/fee?method={}&actor={}'.format('Propose',
                                                                                    fivetoken_calibration_multisig_address)

    re = requests.get(urlSend, headers=header)
    try:
        assert json.loads(re.text).get("data").get('method_name') == 'Send'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(urlSend)
        assert json.loads(re.text).get("data").get('method_name') == 'Send'


    re = requests.get(urlApprove, headers=header)
    try:
        assert json.loads(re.text).get("data").get('method_name') == 'Approve'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(urlApprove)
        assert json.loads(re.text).get("data").get('method_name') == 'Approve'


    re = requests.get(urlExec, headers=header)
    try:
        assert json.loads(re.text).get("data").get('method_name') == 'Exec'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(urlExec)
        assert json.loads(re.text).get("data").get('method_name') == 'Exec'


    re = requests.get(urlPropose, headers=header)
    try:
        assert json.loads(re.text).get("data").get('method_name') == 'Propose'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(urlPropose)
        assert json.loads(re.text).get("data").get('method_name') == 'Propose'


