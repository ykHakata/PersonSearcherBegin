# NAME

    PersonSearcherBegin - 日本語の名前を検索する WEB アプリケーション

# HISTORY

    2012-08
    人名を検索する WEB アプリケーションの開発を開始
    レンタルサーバー: EX-CLOUD livedoor
    CGI.pm を活用、データベースは Mysql

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
