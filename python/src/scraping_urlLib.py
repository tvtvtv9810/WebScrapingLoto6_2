import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ロト6の当選番号が掲載されているみずほ銀行ページのURL
loto_url1 = 'https://www.mizuhobank.co.jp/retail/takarakuji/loto/backnumber/loto6'  # 1～460回目
loto_url2 = 'https://www.mizuhobank.co.jp/retail/takarakuji/loto/backnumber/detail.html?fromto='  # 461回目以降
num = 1

main_num_list = []  # 本数字6桁を格納するリスト
bonus_num_list = []  # ボーナス数字を格納するリスト


# PhantomJSをselenium経由で利用
# driver = webdriver.PhantomJS()
# ブラウザをheadlessモード（バックグラウンドで動くモード）で立ち上げてwebsiteを表示、生成されたhtmlを取得し、BeautifulSoupで+ 綺麗にする。
options = webdriver.ChromeOptions()
# 必須
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
# エラーの許容
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--disable-web-security')
# headlessでは不要そうな機能
options.add_argument('--disable-desktop-notifications')
options.add_argument("--disable-extensions")
# 言語
options.add_argument('--lang=ja')
# 画像を読み込まないで軽くする
options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome('chromedriver', options=options)

driver.implicitly_wait(10)  # seconds

# 実行したいスクリプト
java_script = '\
    function jquery_exe(){\
        /*\
        console.log("test");\
        */\
    };\
    function require(uri) {\
        var js = document.createElement("script");\
        js.type = "text/javascript";\
        js.src = uri + "?v=" + new Date().getTime().toString();\
        var head = document.getElementsByTagName("head")[0];\
        head.appendChild(js);\
    };\
    require("http://code.jquery.com/jquery-3.4.1.js");\
    setTimeout(jquery_exe, 1000);\
'

while num <= 1341:

    # 第1～460回目までの当選ページのURL
    if num < 461:
        url = loto_url1 + str(num).zfill(4) + '.html'
    # 461回目以降当選ページのURL
    else:
        url = loto_url2 + str(num) + '_' + str(num+19) + '&type=loto6'

    # PhntomJSで該当ページを取得
    driver.get(url)
    print("- driver -----------------------------------")
    print(driver)
    print("------------------------------------")
    # スクリプト実行
    # driver.execute_script(java_script)

    # time.sleep(2) # javascriptのページを読み込む時間
    # 途中から取得先のサイトが非同期になってるため、遅延時間を変更
    print("10秒待機・・・")
    time.sleep(10)
    # elem = WebDriverWait(driver, 16).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "wdt33p")))
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    print("- soup -----------------------------------")
    print(soup)
    print("------------------------------------")

    print(soup.title)

    # ロト6の当選番号がのっているテーブルの取得
    table = soup.find_all("table")
    del table[0]

    for i in table:
        # 本数字の取得
        main_num = i.find_all("tr")[2].find("td")
        print("------------------------------------")
        print(main_num)
        print(main_num.string)
        print("------------------------------------")
        if main_num.string == None:
            print("continue;;;;")
            continue
        main_num_list.append(main_num.string.split(" "))

        # ボーナス数字の取得
        bonus_num = i.find_all("tr")[3].find("td")
        bonus_num_list.append(bonus_num.string)

    num += 20  # 次のページに移動するためにnumに20を追加
    time.sleep(random.uniform(1, 3))  # 1～3秒Dos攻撃にならないようにするためにコードを止める

# csvで出力
df = pd.DataFrame(main_num_list, columns=[
    'main1', 'main2', 'main3', 'main4', 'main5', 'main6'])
df['bonus'] = bonus_num_list
df.index = df.index + 1
df.to_csv('loto6.csv')
