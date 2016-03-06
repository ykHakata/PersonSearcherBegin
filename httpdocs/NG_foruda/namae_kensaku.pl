#!/usr/bin/perl

#cgiモジュールインポート
use CGI;
#cgiインスタンス生成
$cgi = new CGI();

#httpヘッダーを出力
print $cgi->header( -charset => "utf-8", );
print $cgi->zinmeidemo.html( 
　　　-lang => 'ja', 
　　　-encoding => 'utf-8'
 );



#htmlヘッダーを出力
print $cgi->start_html(-title=>'名前検索「perl」',-lang=>'ja');
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"http://yk.flxsrv.biz/style.css\">";
$sei = $cgi->param('sei');
$mei = $cgi->param('mei');

#html本文を出力

print '<div id="container">';
	print '<div id="header_a">';
		print '<h1 id="header_a_t">人名検索</h1>';
	print '<!-- /#header_a --></div>';
	print '<form action="namae_kensaku.pl" method="post">';
	print '<div id="navi_a">';
		print '<div id="navi_a_a">';
			print "<h1 id=\"navi_a_a_sei\">姓<input type=\"text\" name=\"sei\" value=\"$sei\" style=\"width: 210px; height: 56px;\" size=\"10\"></h1>";
		print '<!-- /#navi_a_a --></div>';
		print '<div id="navi_a_b">';
			print "<h1 id=\"navi_a_b_mei\">名<input type=\"text\" name=\"mei\" value=\"$mei\" style=\"width: 210px; height: 56px;\" size=\"10\"></h1>";
		print '<!-- /#navi_a_b --></div>';
	print '<!-- /#navi_a --></div>';
	print '<div id="navi_b">';
		print '<input type="image" width="80" heigth="80" src="http://yk.flxsrv.biz/img/botan_2.png" alt="検索する">';
	print '<!-- /#navi_b --></div>';
	print '<div id="header_b">';
		print "<h1 id=\"header_b_t\">$sei　$mei</h1>";
	print '<!-- /#header_b --></div>';

#DBIモジュールインポート
use DBI;
#データベース接続
$db = DBI->connect
			('dbi:mysql:address','ykaddress','yk0520');
#MYSQL,SELECT文を作成

		$sql_mei = "select yomi,hyozi from namae_mei where
		yomi = \"$mei\" or
		hyozi = \"$mei\"";

		$sql_sei = "select yomi,hyozi from namae_sei where
		yomi = \"$sei\" or
		hyozi = \"$sei\"";


#問い合わせ
$data_ref_m = $db->selectall_arrayref($sql_sei);

#問い合わせ
$data_ref = $db->selectall_arrayref($sql_mei);

	#１行ずつ取り出す姓
	print '<div id="content_l">';
		print '<fieldset id="content_l_fi">';
			print '<legend id="content_l_le">検索結果（姓）</legend>';
				print '<p id="content_l_p">';		
	foreach $row_m(@{$data_ref_m})
		{
			foreach $col_m(@{$row_m})
			{
			print "$col_m";
			print "　";
			}
		print "<br />\n";
		}
	print "</p>";
print '<!-- /#content_l_fi --></fieldset>';
		print '<!-- /#content_l --></div>';

		
	print '<div id="content_r">';
		print '<fieldset id="content_r_fi">';
			print '<legend id="content_r_le">検索結果（名）</legend>';
				print '<p id="content_r_p">';
#１行ずつ取り出す名前
	foreach $row(@{$data_ref})
		{
			foreach $col(@{$row})
			{
			print "$col";
			print "　";
			}
		print "<br />\n";
		}
	print "</p>";
	print '<!-- /#content_r_fi --></fieldset>';
print '<!-- /#content_r --></div>';


		

#データベース切断
$db->disconnect();

#HTMLフッターを出力
print $cgi->end_html();