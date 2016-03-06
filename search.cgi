#!/usr/bin/perl
use strict;
use warnings;
use utf8;
use CGI;

binmode STDOUT, ':encoding(utf-8)';

my $q = CGI->new;

my $sei = '';
my $mei = '';

my $html = <<"END_HTML";
<!DOCTYPE html>
<html lang="ja">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=640">
  <link rel="stylesheet" type="text/css" href="style.css">
  <title>人名検索</title>
</head>

<body>
  <div id="container">
    <div id="header_a">
      <h1 id="header_a_t">人名検索</h1>
    </div>
    <form action="namae_kensaku.pl" method="post">
      <div id="navi_a">
        <div id="navi_a_a">
          <h1 id="navi_a_a_sei">姓<input type="text" name="sei" value="$sei" style="width: 210px; height: 56px;" size="10"></h1>
        </div>
        <div id="navi_a_b">
          <h1 id="navi_a_b_mei">名<input type="text" name="mei" value="$mei" style="width: 210px; height: 56px;" size="10"></h1>
        </div>
      </div>
      <div id="navi_b">
        <input type="image" width="80" heigth="80" src="img/botan_2.png" alt="検索する">
      </div>
      <div id="header_b">
        <h1 id="header_b_t">佐籐　祐之</h1>
      </div>
      <div id="content_l">
        <fieldset id="content_l_fi">
          <legend id="content_l_le">検索結果（姓）</legend>
          <p id="content_l_p">
            さとう　作藤
            <br />さとう　砂東
            <br />さとう　沙藤
            <br />さとう　佐籐
            <br />さとう　佐棟
            <br /> さとう　佐島
            <br />さとう　坂東
            <br />さとう　砂藤
            <br />さとう　砂糖
            <br />さとう　左藤
            <br /> さとう　左登
            <br />さとう　佐藤
            <br />さとう　佐当
            <br />さとう　佐東
          </p>
        </fieldset>
      </div>
      <div id="content_r">
        <fieldset id="content_r_fi">
          <legend id="content_r_le">検索結果（名）</legend>
          <p id="content_r_p">
            ゆうじ　優志
            <br />ゆうじ　優二
            <br />ゆうじ　雄二
            <br />ゆうじ　雄治
            <br />ゆうじ　裕史
            <br /> ゆうじ　裕司
            <br />ゆうじ　祐之
            <br />ゆうじ　祐二
            <br />ゆうじ　祐地
            <br />ゆうじ　祐治
            <br /> ゆうじ　祐滋
            <br />ゆうじ　祐次
            <br />ゆうじ　祐児
            <br />ゆうじ　祐志
            <br />ゆうじ　祐嗣
            <br /> ゆうじ　祐史
            <br />ゆうじ　祐司
            <br />ゆうじ　由治
            <br />ゆうじ　裕嗣
            <br />ゆうじ　裕志
            <br /> ゆうじ　雄次
            <br />ゆうじ　雄児
            <br />ゆうじ　雄志
            <br />ゆうじ　雄士
            <br />ゆうじ　雄史
            <br /> ゆうじ　雄爾
            <br />ゆうじ　邑治
            <br />ゆうじ　邑次
            <br />ゆうじ　裕之
            <br />ゆうじ　裕二
            <br /> ゆうじ　裕治
            <br />ゆうじ　裕次
            <br />ゆうじ　裕児
            <br />ゆうじ　裕詞
            <br />ゆうじ　湧二
            <br /> ゆうじ　有二
            <br />ゆうじ　勇児
            <br />ゆうじ　勇志
            <br />ゆうじ　勇史
            <br />ゆうじ　優治
            <br /> ゆうじ　優次
            <br />ゆうじ　優司
            <br />ゆうじ　佑弐
            <br />ゆうじ　佑二
            <br />ゆうじ　佑治
            <br /> ゆうじ　佑次
            <br />ゆうじ　佑司
            <br />ゆうじ　佑浩
            <br />ゆうじ　愉史
            <br />ゆうじ　勇次
            <br /> ゆうじ　勇治
            <br />ゆうじ　勇示
            <br />ゆうじ　有治
            <br />ゆうじ　有史
            <br />ゆうじ　有司
            <br /> ゆうじ　悠二
            <br />ゆうじ　悠治
            <br />ゆうじ　悠次
            <br />ゆうじ　悠司
            <br />ゆうじ　宥二
            <br /> ゆうじ　友二
            <br />ゆうじ　友治
            <br />ゆうじ　友司
            <br />ゆうじ　友次
            <br />ゆうじ　勇二
            <br />ゆうじ　雄仁
          </p>
        </fieldset>
      </div>
    </form>
  </div>
</body>

</html>
END_HTML

print $html;

__END__
