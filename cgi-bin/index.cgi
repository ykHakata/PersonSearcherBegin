#!/usr/bin/env perl
use strict;
use warnings;
use utf8;
use FindBin;
use lib ("$FindBin::RealBin/../local/lib/perl5");
use CGI;
use DBI;
use FindBin;
use File::Spec;
use URI::Escape;
use Encode;

binmode STDOUT, ':encoding(utf-8)';
binmode STDIN,  ':encoding(utf-8)';

my $q = CGI->new;

my $last_name  = $q->param('last_name')  || '';
my $first_name = $q->param('first_name') || '';

if ($last_name) {
    $last_name = uri_unescape($last_name);
    $last_name = Encode::decode( 'utf-8', $last_name );
}

if ($first_name) {
    $first_name = uri_unescape($first_name);
    $first_name = Encode::decode( 'utf-8', $first_name );
}

my $db_file = File::Spec->catfile( $FindBin::Bin, '../db', 'persons_name.db' );

my $data_source = 'dbi:SQLite:' . $db_file;
my $username    = '';
my $auth        = '';
my $attr        = +{
    RaiseError     => 1,
    AutoCommit     => 1,
    sqlite_unicode => 1,
};

my $dbh = DBI->connect( $data_source, $username, $auth, $attr );

my $last_names = $dbh->selectall_arrayref(
    q{SELECT * FROM last_name WHERE name = ? OR ruby = ?},
    +{ Slice => +{}, },
    $last_name, $last_name,
);

my $first_names = $dbh->selectall_arrayref(
    q{SELECT * FROM first_name WHERE name = ? OR ruby = ?},
    +{ Slice => +{}, },
    $first_name, $first_name,
);

my $result_last_name = '';

for my $name ( @{$last_names} ) {
    $result_last_name .=
      $name->{ruby} . '&emsp;' . $name->{name} . '<br>' . "\n          ";
}

my $result_first_name = '';

for my $name ( @{$first_names} ) {
    $result_first_name .=
      $name->{ruby} . '&emsp;' . $name->{name} . '<br>' . "\n          ";
}

my $html = <<"END_HTML";
Content-Type: text/html; charset=utf-8

<!DOCTYPE html>
<html lang="ja">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=640">
  <link rel="stylesheet" type="text/css" href="../style.css">
  <title>人名検索</title>
</head>

<body>
  <div id="container">
    <div id="header_a">
      <h1 id="header_a_t">人名検索</h1>
    </div>
    <form action="" method="post">
      <div id="navi_a">
        <div id="navi_a_a">
          <h1 id="navi_a_a_sei">姓<input type="text" name="last_name" value="$last_name" style="width: 210px; height: 56px;" size="10"></h1>
        </div>
        <div id="navi_a_b">
          <h1 id="navi_a_b_mei">名<input type="text" name="first_name" value="$first_name" style="width: 210px; height: 56px;" size="10"></h1>
        </div>
      </div>
      <div id="navi_b">
        <input type="image" width="80" heigth="80" src="../img/botan_2.png" alt="検索する">
      </div>
      <div id="header_b">
        <h1 id="header_b_t">$last_name&emsp;$first_name</h1>
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
