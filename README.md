# NAME

PersonSearcherBegin - 日本語の名前を検索する WEB アプリケーション

# SYNOPSIS

## URL

- <http://becom.sakura.ne.jp/PersonSearcherBegin/index.html> -開発初期の見本、静的なページ
- <http://becom.sakura.ne.jp/PersonSearcherBegin/search.cgi> -アプリケーション
- <http://becom.sakura.ne.jp/PersonSearcherBegin/init.cgi> -アプリケーション初期化

# HISTORY

```
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
```

# DEPLOYMENT

```
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
