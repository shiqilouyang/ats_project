
def test_mainnetActorById(postgre_prod_database):

    ''' 判断大额转账cid是否有重复  '''
    db = postgre_prod_database
    cursor = db.cursor()
    cursor.execute("SELECT cid from large_amount_transfer_new")
    data = cursor.fetchall()
    cid_list = []
    for i in data:
        cid_list.append(i[0])
    set_lst = set(cid_list)
    if len(set_lst) == len(cid_list):
        print('列表里的元素互不重复！')
        assert 1
    else:
        print('列表里有重复的元素！')
        assert 0

    db.close()


