# NAME

    PersonSearcherBegin - 日本語の名前を検索する WEB アプリケーション

# URL

    開発初期の見本、静的なページ
    http://yonabemt.sakura.ne.jp/PersonSearcherBegin/index.html

    アプリケーション
    http://yonabemt.sakura.ne.jp/PersonSearcherBegin/search.cgi

    アプリケーション初期化
    http://yonabemt.sakura.ne.jp/PersonSearcherBegin/init.cgi

# HISTORY

    2012-08
    人名を検索する WEB アプリケーションの開発を開始
    レンタルサーバー: EX-CLOUD livedoor
    CGI.pm を活用、データベースは Mysql
    人名のデーターは 「人名検索くん」サイトから
    サンプルデータダウンロードして利用したが、
    現在このサイトはアクセス出来ない
    http://mobile.shinsv.dyndns.org/jinmei/

    2013-06-24 レンタルサーバー解約

    2016-03-06 remaster 開始

# DEPLOYMENT

レンタルサーバーへ接続

```bash
# 鍵認証による接続
$ ssh yonabemt@yonabemt.sakura.ne.jp
```

レンタルサーバーでのサイトの更新

```sh
# さくらのレンタルサーバーは csh
% pwd
/home/yonabemt/www/PersonSearcherBegin

# (リポジトリを最新の状態に)
% git fetch

# (ローカルと同じ状態)
% git pull origin master
```
