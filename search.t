use strict;
use warnings;
use utf8;
use Test::More;
use Encode;
use Data::Dumper;

my $cgi_std = `carton exec -- perl search.cgi`;
$cgi_std = Encode::decode( 'utf-8', $cgi_std );

like( $cgi_std, qr{\Q人名検索\E},          'html title' );
like( $cgi_std, qr{\Qname="last_name"\E},      'input from' );
like( $cgi_std, qr{\Qname="first_name"\E},     'input from' );
like( $cgi_std, qr{\Q検索結果（姓）\E}, 'view last_name' );
like( $cgi_std, qr{\Q検索結果（名）\E}, 'view first_name' );

$cgi_std = `carton exec -- perl search.cgi last_name=さとう`;
$cgi_std = Encode::decode( 'utf-8', $cgi_std );
like( $cgi_std, qr{さとう&emsp;佐藤}, 'content last_name' );

$cgi_std = `carton exec -- perl search.cgi first_name=ゆうじ`;
$cgi_std = Encode::decode( 'utf-8', $cgi_std );
like( $cgi_std, qr{ゆうじ&emsp;祐之}, 'content first_name' );

done_testing

__END__
