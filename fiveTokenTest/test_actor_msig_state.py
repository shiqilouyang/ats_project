import requests
import json

def test_mainnetActor_msig_state(fivetoken_mainnet_url,fivetoken_mainnet_multisig_address):

    header = {'Content-Type': 'application/json'}

    ''' 消息详情 '''
    url = fivetoken_mainnet_url+'/actor/msig/state?address={}'.format(fivetoken_mainnet_multisig_address)


    re = requests.get(url,headers=header)
    try:
        assert json.loads(re.text).get("data").get("signers") is not []
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url)
        assert json.loads(re.text).get("data").get("signers") is not []






def test_calibrationActor_msig_state(fivetoken_calibration_url,fivetoken_calibration_multisig_address):
    ''' 消息详情 '''

    header = {'Content-Type': 'application/json'}

    # 多签
    url = fivetoken_calibration_url+'/actor/msig/state?address={}'.format(fivetoken_calibration_multisig_address)

    re = requests.get(url,headers=header)
    try:
        assert json.loads(re.text).get("data").get("signers") is not []
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url)
        assert json.loads(re.text).get("data").get("signers") is not []
