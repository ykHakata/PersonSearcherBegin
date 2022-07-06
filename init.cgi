#!/usr/bin/env perl
use 5.014;
use strict;
use warnings;
use utf8;
use FindBin;
use File::Spec;
use Carp;
use Time::Piece;
use File::Temp;

binmode STDOUT, ':encoding(utf-8)';

my $tp_obj     = localtime;
my $time_stamp = $tp_obj->datetime( 'T' => ' ' );

my $dir_db = File::Spec->catfile( $FindBin::RealBin, 'db' );

my $last_name = File::Temp->new(
    DIR    => $dir_db,
    SUFFIX => '.txt',
);

my $first_name = File::Temp->new(
    DIR    => $dir_db,
    SUFFIX => '.txt',
);

my $db     = File::Spec->catfile( $dir_db,           'persons_name.db' );
my $schema = File::Spec->catfile( $FindBin::RealBin, 'persons_name.sql' );
my $data   = File::Spec->catfile( $dir_db,           'ime-import.txt' );

# スキーマー読み込み初期化
my $cmd = "sqlite3 $db <$schema";
system $cmd
  and croak "Couldn'n run: $cmd ($!)";

open my $fh, '<:encoding(utf8)', $data
  or croak "Can't open '$data': $!";

open my $fh_last_name, '>>:encoding(utf8)', $last_name
  or croak "Can't open '$last_name': $!";

open my $fh_first_name, '>>:encoding(utf8)', $first_name
  or croak "Can't open '$first_name': $!";

my $last_id    = 0;
my $first_id   = 0;
my $not_import = '';

while ( my $row = <$fh> ) {
    chomp $row;
    my ( $ruby, $name, $type ) = split "\t", $row;
    if ( $type && $type eq '姓' ) {
        $last_id += 1;
        my $text_row = join ',',
          ( $last_id, $name, $ruby, $time_stamp, $time_stamp );
        $fh_last_name->say($text_row);
    }
    elsif ( $type && $type eq '名' ) {
        $first_id += 1;
        my $text_row = join ',',
          ( $first_id, $name, $ruby, $time_stamp, $time_stamp );
        $fh_first_name->say($text_row);
    }
    else {
        $not_import .= '<p>' . $row . '</p>' . "\n  ";
    }
}

my $import_data = +{
    last_name  => $last_name,
    first_name => $first_name,
};

# csv ファイル読み込み
IMPORT_ACTION:
while ( my ( $table, $file, ) = each %{$import_data} ) {
    next IMPORT_ACTION if !$file;
    $cmd = qq{sqlite3 -separator , $db '.import $file $table'};
    system $cmd
      and croak "Couldn'n run: $cmd ($!)";
}

my $html = <<"END_HTML";
Content-Type: text/html; charset=utf-8

<!DOCTYPE html>
<html lang="ja">

<head>
  <meta charset="UTF-8">
  <title>人名検索データ初期化</title>
</head>

<body>
  <p>とりこまれなかったデータ</p>
  $not_import
  <p>last_name テーブル (性)</p>
  <p>$last_id 件</p>
  <p>first_name テーブル (性)</p>
  <p>$first_id 件</p>
</body>

</html>
END_HTML

print $html;

__END__
