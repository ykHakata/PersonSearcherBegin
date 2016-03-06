#!/usr/bin/perl
use strict;
use warnings;
use utf8;
use CGI;
use DBI;
use FindBin;
use File::Spec;

binmode STDOUT, ':encoding(utf-8)';

my $q = CGI->new;

my $sei = $q->param('sei') || '';
my $mei = $q->param('mei') || '';

my $db = File::Spec->catfile( $FindBin::Bin, 'db', 'persons_name.db' );

my $data_source = 'dbi:SQLite:' . $db;
my $username    = '';
my $auth        = '';
my $attr        = +{
    RaiseError     => 1,
    AutoCommit     => 1,
    sqlite_unicode => 1,
};

my $dbh = DBI->connect( $data_source, $username, $auth, $attr );

my $sql         = q{SELECT * FROM first_name WHERE name = ? OR ruby = ?};
my $attr        = +{ Slice => +{}, };
my @bind_values = ( $mei, $mei );

my $first_names = $dbh->selectall_arrayref( $sql, $attr, @bind_values );

$sql         = q{SELECT * FROM last_name WHERE name = ? OR ruby = ?};
$attr        = +{ Slice => +{}, };
@bind_values = ( $sei, $sei );

my $last_names = $dbh->selectall_arrayref( $sql, $attr, @bind_values );

my $result_first_name;

for my $name ( @{$first_names} ) {
    $result_first_name
        .= $name->{ruby} . ' ' . $name->{name} . '<br>' . "\n          ";
}

my $result_last_name;

for my $name ( @{$last_names} ) {
    $result_last_name
        .= $name->{ruby} . ' ' . $name->{name} . '<br>' . "\n          ";
}

my $html = <<"END_HTML";
Content-Type: text/html; charset=utf-8

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
    <form action="search.cgi" method="post">
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
          $result_last_name
          </p>
        </fieldset>
      </div>
      <div id="content_r">
        <fieldset id="content_r_fi">
          <legend id="content_r_le">検索結果（名）</legend>
          <p id="content_r_p">
          $result_first_name
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
