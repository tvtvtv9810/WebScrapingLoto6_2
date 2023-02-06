import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ロト6の当選番号が掲載されているみずほ銀行ページのURL（（A表）先月から過去1年間の当せん番号）
# year=2022&month=2
loto_url_latest1Year = 'https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/loto6/index.html?'
start_year = 2022
start_month = 2
end_year = 2023
end_month = 1

# num = startNum

times_list = []  # 第何回目かリスト
lottery_date_list = []  # 抽選日リスト
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

current_year = start_year
current_month = start_month

while current_year < end_year or (current_year == end_year and current_month <= end_month):

    # URL
    url = loto_url_latest1Year + 'year=' + \
        str(current_year) + '&month=' + str(current_month)

    # chromeで該当ページを取得
    driver.get(url)

    # time.sleep(2) # javascriptのページを読み込む時間
    # 途中から取得先のサイトが非同期になってるため、遅延時間を変更
    print("10秒待機・・・")
    time.sleep(10)

    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")

    print(soup.title)

    # ロト6の当選番号がのっているテーブルの取得
    tables = soup.select("table[class='typeTK']")

    isRetry = False
    for table1Dose in tables:
        # table head
        tHead = table1Dose.find("thead")
        # > 回
        times = tHead.find("tr").find_all("th")[1].string
        print("------------------------------------")
        print(times)
        # print("------------------------------------")

        # table body
        tBody = table1Dose.find("tbody")
        trList = tBody.find_all("tr")

        # > 抽選日
        lottery_date = trList[0].find("td").string
        # print("------------------------------------")
        print(lottery_date)
        # print("------------------------------------")

        # 本数字の取得
        main_nums_td_list = trList[1].find_all("td")
        main_num_map = map(lambda td: td.find(
            "strong").string, main_nums_td_list)

        # print("------------------------------------")
        # print(list(main_num_map))
        print("------------------------------------")

        # ボーナス数字の取得
        bonus_num = trList[2].find("td").find("strong").string

        # 保持
        main_num_list.append(list(main_num_map))
        times_list.append(times)
        lottery_date_list.append(lottery_date)
        bonus_num_list.append(bonus_num)

    current_month += 1
    if current_month > 12:
        current_month = 1
        current_year += 1

    time.sleep(random.uniform(1, 3))  # 1～3秒Dos攻撃にならないようにするためにコードを止める

# csvで出力
df = pd.DataFrame(main_num_list, columns=[
    'main1', 'main2', 'main3', 'main4', 'main5', 'main6'])
df['bonus'] = bonus_num_list
df['times'] = times_list
df['date'] = lottery_date_list
df.index = df.index + 1
df.to_csv('loto6.csv')
