

def bat_log_format(code,*args):
    if code == "0001":
        text = "処理開始"

    elif code == "0010":
        text = "二重起動"

    elif code == "0002":
        text = "処理対象ファイルなし"

    elif code == "0020":
        text = "入力データ異常(フォーマット) [ファイル名:{0},行数:{1},項目名:{2},チェック項目:{3},チェック値:{4}]".format(args[0],args[1],args[2],args[3],args[4])

    elif code == "0030":
        text = "入力データ異常(指定カテゴリ) [ファイル名:{0},行数:{1},チェック値:{2}]".format(args[0],args[1],args[2])

    elif code == "0040":
        text = "入力データ異常(指定ファイル) [ファイル名:{0},行数:{1},チェック値:{2}]".format(args[0],args[1],args[2])

    elif code == "0100":
        text = "API連携実行[URL:{}, ボディ:{}]".format(args[0],args[1])

    elif code == "0110":
        text = "API連携異常[API名:{}, レスポンスコード:{}]".format(args[0],args[1])

    elif code == "0120":
        text = "ファイルアップロード異常[ファイル名:{},レスポンスコード:{}]".format(args[0],args[1])

    elif code =="0000":
        text = "正常終了"

    elif code == "9000":
        text = "異常終了"

    return text


if __name__ == "__main__":
    # This is the test run
    print('bat_log_format( "0001")')
    ret = bat_log_format( "0001")
    print(ret)

    print('bat_log_format( "0010")')
    ret = bat_log_format( "0010")
    print(ret)

    print('bat_log_format( "0020", "data01.csv", 47, "ABCD-01-01")')
    ret = bat_log_format( "0020", "data01.csv", 47, "ABCD-01-01",'5555','88888')
    print(ret) 
 
    print('bat_log_format( "0030", "data01.csv", 47, "ABCD-01-01")')
    ret = bat_log_format( "0030", "data01.csv", 47, "ABCD-01-01",'5555','88888')
    print(ret) 

    print('bat_log_format( "0040", "data01.csv", 47, "ABCD-01-01")')
    ret = bat_log_format( "0040", "data01.csv", 47, "ABCD-01-01",'5555','88888')
    print(ret) 

    print('bat_log_format( "0100", "data01.csv", 47, "ABCD-01-01")')
    ret = bat_log_format( "0100", "data01.csv", 47, "ABCD-01-01",'5555','88888')
    print(ret) 

    print('bat_log_format( "0110", "data01.csv", 47, "ABCD-01-01")')
    ret = bat_log_format( "0110", "data01.csv", 47, "ABCD-01-01",'5555','88888')
    print(ret) 

    print('bat_log_format( "0120", "data01.csv", 47, "ABCD-01-01")')
    ret = bat_log_format( "0120", "data01.csv", 47, "ABCD-01-01",'5555','88888')
    print(ret) 

    print('bat_log_format( "0000", "data01.csv", 47, "ABCD-01-01")')
    ret = bat_log_format( "0000", "data01.csv", 47, "ABCD-01-01",'5555','88888')
    print(ret) 

    print('bat_log_format( "9000", "data01.csv", 47, "ABCD-01-01")')
    ret = bat_log_format( "9000", "data01.csv", 47, "ABCD-01-01",'5555','88888')
    print(ret) 

