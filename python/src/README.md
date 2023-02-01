# 概要

- LOTO6 の当選番号のデータをスクレイピング
  - javascript でレンダリング された結果を取得

# 使用ライブラリ：パッケージ

## chrome / chrome driver / selenium

- javascript でレンダリングされたページからスクレイピング

## BeautifulSoup

- HTML および XML ドキュメントを解析するための Python パッケージ

# LOTO6 の URL について

## （過去）

### 1-460 回

- 0001-0020 回 : https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/loto60001.html
- 0021-0040 回 : https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/loto60021.html
- ...
- 0441-0460 回 : https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/loto60441.html

### 461-1530 回

- 0461-0480 回 : https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/detail.html?fromto=461_480&type=loto6
- ...
- 1521-1530 回 : https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/detail.html?fromto=1521_1530&type=loto6
- ...
- 1641-1651 回 : https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/detail.html?fromto=1641_1651&type=loto6

### 備考

- 2023.01.26 時点では、過去は、1530 回まで（最新はまた別ページ）

# 参考にしたサイト

## 今更 Web スクレイピングを試してロト６のデータを取得

- https://qiita.com/Kis3_/items/1057af45d32617376a67

## スクレイピングで 403 Forbidden：You don’t have permission to access on this server が出た際の対処法

- https://non-dimension.com/solution-403forbidden/

## Javascript でレンダリングされる Web ページを、スクレイピングする

- https://www.yoheim.net/blog.php?q=20170302

## Docker + selenium + chromedriver のスクレイプ環境を構築する

- https://qiita.com/senth/items/c784fa5458e0de9e0256
