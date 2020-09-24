# NAME

PersonSearcherBegin - 日本語の名前を検索する WEB アプリケーション

## SYNOPSIS

### URL

- <http://becom.sakura.ne.jp/PersonSearcherBegin/sample.html> -開発初期の見本、静的なページ
- <http://becom.sakura.ne.jp/PersonSearcherBegin/index.cgi> -アプリケーション
- <http://becom.sakura.ne.jp/PersonSearcherBegin/init.cgi> -アプリケーション初期化
- <https://psb.becom.co.jp/> - 独自ドメインでのアプリケーション実行

## HISTORY

```md
2012-08
人名を検索する WEB アプリケーションの開発を開始
レンタルサーバー: EX-CLOUD livedoor
CGI.pm を活用、データベースは Mysql
人名のデーターは 「人名検索くん」サイトから
サンプルデータダウンロードして利用したが、
現在このサイトはアクセス出来ない
http://mobile.shinsv.dyndns.org/jinmei/

2013-06-24 レンタルサーバー解約
2016-03-06 remaster
2020-09-24 レンタルサーバー公開のための調整など
```

## DEPLOYMENT

```console
(鍵認証による接続)
$ ssh becom@becom.sakura.ne.jp

(さくらのレンタルサーバーは csh)
% pwd
/home/becom/www/PersonSearcherBegin

(リポジトリを最新の状態に)
% git fetch

(ローカルと同じ状態)
% git pull origin master
```

## DOCKER

```console
(イメージ作成からコンテナ、バックグラウンド起動まで)
$ docker-compose up --build -d

(作ったコンテナで作業)
$ docker-compose exec app /bin/bash

(コンテナに入り、初動のときはモジュールをインストール)
# carton install

(コンテナの中でテストコード実行)
# carton exec -- perl search.t

(コンテナ終了)
# exit

(コンテナのバックグラウンド終了)
$ docker-compose stop

(次回からの実行)
$ docker-compose start
```
