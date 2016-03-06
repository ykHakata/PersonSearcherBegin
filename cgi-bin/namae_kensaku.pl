#!/usr/bin/perl

#cgiモジュールインポート
use CGI;
#cgiインスタンス生成
$cgi = new CGI();
#httpヘッダーを出力
print $cgi->header(-type=>'text/html',-charset=>'utf-8');


print '<meta name="viewport" content="width=640;">';
#htmlヘッダーを出力
print $cgi->start_html(-title=>'名前検索「perl」',-lang=>'ja');
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"http://yk.flxsrv.biz/style.css\">\n";


#一度入力した値を次の時も表示
$sei = $cgi->param('sei');#姓の入力枠
$mei = $cgi->param('mei');#名の入力枠
#html本文を出力 webサイトからのソース表示を見やすくするため"で囲んで\で打ち消し改行入れる。
print "<div id=\"container\">\n";
print "<div id=\"header_a\">\n";
print "<h1 id=\"header_a_t\">人名検索</h1>\n";
print "<!-- /#header_a --></div>\n";
print "<form action=\"namae_kensaku.pl\" method=\"post\">\n";
print "<div id=\"navi_a\">\n";
print "<div id=\"navi_a_a\">\n";
print "<h1 id=\"navi_a_a_sei\">姓<input type=\"text\" name=\"sei\" value=\"$sei\" style=\"width: 210px; height: 56px;\" size=\"10\"></h1>\n";
print "<!-- /#navi_a_a --></div>\n";
print "<div id=\"navi_a_b\">\n";
print "<h1 id=\"navi_a_b_mei\">名<input type=\"text\" name=\"mei\" value=\"$mei\" style=\"width: 210px; height: 56px;\" size=\"10\"></h1>\n";
print "<!-- /#navi_a_b --></div>\n";
print "<!-- /#navi_a --></div>\n";
print "<div id=\"navi_b\">\n";
print "<input type=\"image\" width=\"80\" heigth=\"80\" src=\"http://yk.flxsrv.biz/img/botan_2.png\" alt=\"検索する\">\n";
print "<!-- /#navi_b --></div>\n";
print "<div id=\"header_b\">\n";
print "<h1 id=\"header_b_t\">$sei　$mei</h1>\n";#入力した文字を拡大表示
print "<!-- /#header_b --></div>\n";

#DBIモジュールインポート
use DBI;
#データベース接続
$db = DBI->connect('dbi:mysql:address','ykaddress','yk0520');
$db->do('SET NAMES utf8');
#MYSQL,SELECT文を作成
#姓のところの入力値をmysql送り、ひらがなも漢字も検索
$sql_sei = "select yomi,hyozi from namae_sei where yomi = \"$sei\" or hyozi = \"$sei\"";
#名のところの入力値をmysql送り、ひらがなも漢字も検索
$sql_mei = "select yomi,hyozi from namae_mei where yomi = \"$mei\" or hyozi = \"$mei\"";
#問い合わせ、配列のリファレンスで返す、姓のところ
$data_ref_sei = $db->selectall_arrayref($sql_sei);
#問い合わせ、配列のリファレンスで返す、名のところ
$data_ref_mei= $db->selectall_arrayref($sql_mei);
print "<div id=\"content_l\">\n";
print "<fieldset id=\"content_l_fi\">\n";
print "<legend id=\"content_l_le\">検索結果（姓）</legend>\n";
print "<p id=\"content_l_p\">\n";		
#姓、１行ずつ取り出し、左の検索結果に表示
foreach $row_sei(@{$data_ref_sei})#1行ずつ取出しリファレンス
{
    foreach $col_sei(@{$row_sei})#1個ずつ取出し、文字になる
    {
        print "$col_sei";#1個ずつ出力
        print "　";#半角スペースで区切り
    }
    print "<br />\n";#改行する
}
print "</p>\n";
print "<!-- /#content_l_fi --></fieldset>\n";
print "<!-- /#content_l --></div>\n";
#名、１行ずつ取り出し、右の検索結果に表示
print "<div id=\"content_r\">\n";
print "<fieldset id=\"content_r_fi\">\n";
print "<legend id=\"content_r_le\">検索結果（名）</legend>\n";
print "<p id=\"content_r_p\">\n";
foreach $row_mei(@{$data_ref_mei})#1行ずつ取出しリファレンス
{
    foreach $col_mei(@{$row_mei})#1個ずつ取出し、文字になる
    {
        print "$col_mei";#1個ずつ出力
        print "　";#半角スペースで区切り
    }
    print "<br />\n";#改行する
}
print "</p>\n";
print "<!-- /#content_r_fi --></fieldset>";
print "<!-- /#content_r --></div>";
#データベース切断
$db->disconnect();
#HTMLフッターを出力
print $cgi->end_html();