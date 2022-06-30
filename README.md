# NAME

PersonSearcherBegin - 日本語の名前を検索する WEB アプリケーション

## SYNOPSIS

### URL

- <https://psb.becom.co.jp/> - アプリケーション
- <https://psb.becom.co.jp/index.cgi> -アプリケーションcgiファイルを指定して
- <https://psb.becom.co.jp/init.cgi> -アプリケーション初期化
- <https://psb.becom.co.jp/sample.html> -開発初期の見本、静的なページ

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
2022-06-30 レンタルサーバー環境変更のため若干の修正
```

## Setup

事前に`plenv`を使えるようにしておき指定バージョンのPerlを使えるように

git clone にてソースコードを配置後プロジェクト配下にてモジュールをインストール

```zsh
./cpanm -l ./local --installdeps .
```

## Work

ローカル開発時の起動方法など

cgi ファイルを起動の場合

```zsh
python3 -m http.server 3000 --cgi
```

リクエスト

```zsh
curl 'http://localhost:3000/cgi-bin/index.cgi'
```

公開環境へ公開

```sh
ssh becom2022@becom2022.sakura.ne.jp
cd ~/www/PersonSearcherBegin
git fetch && git checkout master && git pull
```

### Environment

初動時の環境構築に関するメモ

ignore

```zsh
echo 'local' > .gitignore
echo 'db' >> .gitignore
echo '.DS_Store' >> .gitignore
```

Perl

```zsh
echo '5.32.1' > .perl-version
echo "requires 'CGI';" > cpanfile
echo "requires 'URI';" >> cpanfile
echo "requires 'DBD::SQLite';" >> cpanfile
```

Module

```zsh
curl -L https://cpanmin.us/ -o cpanm
chmod +x cpanm
./cpanm -l ./local --installdeps .
```

公開環境

```sh
ssh becom2022@becom2022.sakura.ne.jp
cd ~/www/
git clone git@github.com:ykHakata/PersonSearcherBegin.git
# sakuraが提供しているモージュールだけで動くのでcpanmは実行しない
```
