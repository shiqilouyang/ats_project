import psycopg2
import pytest


@pytest.fixture(scope="module")
def postgre_test_database():
    '''filscan 测试库'''
    conn = psycopg2.connect(database="chain_monitor", user="readonly", password="readonly123456", host="192.168.1.189",
                            port="5432")
    return conn


@pytest.fixture(scope="module")
def postgre_prod_database():
    '''filscan 生产库'''
    conn = psycopg2.connect(database="lotus_monitor", user="readonly", password="123456", host="52.192.139.201",
                            port="5432")
    return conn


@pytest.fixture(scope="module")
def fivetoken_old_mainnet_url():
    '''fivetoken 老版本api主网生产环境 '''
    return 'https://api.filscan.io:8700/rpc/v1'


@pytest.fixture(scope="module")
def fivetoken_old_calibration_url():
    '''fivetoken calibration 老版本api环境 '''
    return 'https://calibration.filscan.io:8700/rpc/v1'


@pytest.fixture(scope="module")
def fivetoken_mainnet_url():
    '''fivetoken 新版本api主网环境 '''
    # return 'https://api.fivetoken.io/api/uip7oegcgxr6ovab296tpqoh'
    return 'http://192.168.1.161:8081/api/test'

@pytest.fixture(scope="module")
def fivetoken_calibration_url():
    '''fivetoken 新版本api calibration '''
    # return 'https://api.calibration.fivetoken.io/api/uip7oegcgxr6ovab296tpqoh'
    return 'http://192.168.1.161:9091/api/test'



@pytest.fixture(scope="module")
def fivetoken_calibration_bls():
    '''测试网新地址'''
    return 't3una2hb5hrlrb6zgaycjrexa5tl5eyofwmcvcl6cg2zmymb4zj4zalnk3du5bwkguzdv273cexgb5oaqu6bpa'



@pytest.fixture(scope="module")
def fivetoken_mainnet_bls():
    '''主网新地址'''
    return 'f3xhhhvzzkmlsfhnuzaa7ebhbchycovesir2viykyjrsxvj56urabh4h7sm3d2seqdky326m32vufqhjttgwpq'



@pytest.fixture(scope="module")
def fivetoken_calibration_exist_message():
    '''存在的 消息 '''
    return 'bafy2bzaced5rv5657brxmdb6enowmfbtnsi4tndln7bkeheg5yw72tr3lmw42'


@pytest.fixture(scope="module")
def fivetoken_calibration_no_exist_message():
    '''不存在的 消息 '''
    return 'bafy2bzaced5rv5657brxmdb6enowmfbtnsi4tndln7bkeheg5yw72tr3lmw421'



@pytest.fixture(scope="module")
def fivetoken_calibration_SysErrInsufficientFunds_message():
    '''失败的消息 '''
    return 'bafy2bzaceam7i4p6km4e44kov5k6pbpxaelmt2ttubdjhzx7wdbvqmhdghadq'



@pytest.fixture(scope="module")
def fivetoken_mainnet_exist_message():
    '''存在的 消息 '''
    return 'bafy2bzacedvs6lmle4rwzailwnjyldhbt2okqfhci4fhb76o6zvbx5zcbj4ak'



@pytest.fixture(scope="module")
def fivetoken_mainnet_SysErrInsufficientFunds_message():
    '''失败的消息 '''
    return 'bafy2bzacebf2rmg5nn66hhkkkpcxnuwb2i5zjawkwvmtzz2ze6nwzys3brii4'


@pytest.fixture(scope="module")
def fivetoken_mainnet_no_exist_message():
    '''不存在的 消息 '''
    return 'bafy2bzacedinmn3a77ohctf2yc4s4hyk2yw5u7lojykshvgstmb3b4uf7oop61'


@pytest.fixture(scope="module")
def fivetoken_mainnet_multisig_address():
    '''多签地址 '''
    return 'f2l265y6jz5qrft54366kv3ubrkxhflb4n2leiwpi'


@pytest.fixture(scope="module")
def fivetoken_calibration_multisig_address():
    '''多签地址 '''
    return 't2i35vaqpkqpx3rcmqpttayaa3k4b7qm2fgrqiq3q'


@pytest.fixture(scope="module")
def fivetoken_mainnet_miner_address():
    '''旷工地址 '''
    return 'f02438'


@pytest.fixture(scope="module")
def fivetoken_calibration_miner_address():
    '''旷工地址 '''
    return 't01246'


@pytest.fixture(scope="module")
def fivetoken_mainnet_no_exist_miner_address():
    '''旷工地址 '''
    return 'f01108573'


@pytest.fixture(scope="module")
def fivetoken_calibration_no_exist_miner_address():
    '''旷工地址 '''
    return 't019277'