import requests
import json

def test_mainnet_actor_msig_deposits(fivetoken_mainnet_url,fivetoken_mainnet_bls,fivetoken_mainnet_multisig_address):
    ''' 查询多签充值消息记录 '''

    header = {'Content-Type': 'application/json'}

    # f2 地址
    url = fivetoken_mainnet_url+'/actor/msig/deposits?direction=down&limit=10&actor={}'.format('f2klkxwx5dhp3cuufsy27xn5yo36ij2drwfx46kpq')
    url_down_mid = fivetoken_mainnet_url+'/actor/msig/deposits?direction=down&limit=10&actor={}&mid={}'.format('f2klkxwx5dhp3cuufsy27xn5yo36ij2drwfx46kpq',94616200100)
    url_up_mid = fivetoken_mainnet_url+'/actor/msig/deposits?direction=up&limit=10&actor={}&mid={}'.format('f2klkxwx5dhp3cuufsy27xn5yo36ij2drwfx46kpq',94616200100)



    re = requests.get(url,headers=header)
    try:
        assert json.loads(re.text).get("data").get('messages')[-1]['mid'] == '94615500469'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url)
        assert json.loads(re.text).get("data").get('messages')[-1]['mid'] == '94615500469'
    re = requests.get(url_down_mid, headers=header)
    try:
        assert json.loads(re.text).get("data").get('messages')[-1]['mid'] == '98018300246'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url_down_mid)
        assert json.loads(re.text).get("data").get('messages')[-1]['mid'] == '98018300246'
    re = requests.get(url_up_mid, headers=header)
    try:
        assert json.loads(re.text).get("data").get('messages')[-1]['mid'] == '94615500469'
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url_up_mid)
        assert json.loads(re.text).get("data").get('messages')[-1]['mid'] == '94615500469'






def test_calibration_actor_msig_deposits(fivetoken_calibration_url,fivetoken_calibration_bls,fivetoken_calibration_multisig_address):
    ''' 查询多签充值消息记录 '''

    header = {'Content-Type': 'application/json'}

    # f2 地址
    url = fivetoken_calibration_url+'/actor/msig/deposits?direction=down&limit=10&actor={}'.format(fivetoken_calibration_multisig_address)


    re = requests.get(url,headers=header)
    try:
        assert json.loads(re.text).get("data").get('messages') is not None
    except  AttributeError as e:
        print(json.loads(re.text))
    except Exception:
        print(url)
        assert json.loads(re.text).get("data").get('messages') is not None


