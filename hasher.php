#!/usr/bin/php

<?php
global $argv;
$file = sha1_file( $argv[ 1 ] );

echo 'SHA1: '."\n";
echo '     HEX: ' . strtoupper( $file ) . "\n";
$b32 = new SHA1;
$base32 = $b32->fileSHA1( $argv[ 1 ] );

echo '     BASE32: ' . $base32 . "\n";
echo '     BASE64: ' . base64_encode( sha1_file( $argv[ 1 ], true ) ) . "\n";

echo "\n";
echo 'MD5:'."\n";
echo '     HEX: ' . strtoupper( md5_file( $argv[ 1 ] ) ) . "\n";

$base325 = $b32->fileMD5( $argv[ 1 ] );

echo '     BASE32: ' . $base325 . "\n";
echo '     BASE64: ' . base64_encode( md5_file( $argv[ 1 ], true ) ) . "\n";
 
class SHA1 {

	static $BASE32_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567';
	/** Given a file it creates a magnetmix */
	static function fileMD5($file) {
		$raw = md5_file($file,true);
		return SHA1::base32encode($raw);
	} //fileSHA1


	/** Given a file it creates a magnetmix */
	static function fileSHA1($file) {
		$raw = sha1_file($file,true);
		return SHA1::base32encode($raw);
	} //fileSHA1

	/** Takes raw input and converts it to base32 */
	static function base32encode($input) {
		$output = '';
		$position = 0;
		$storedData = 0;
		$storedBitCount = 0;
		$index = 0;

		while ($index < strlen($input)) {
			$storedData <<= 8;
			$storedData += ord($input[$index]);
			$storedBitCount += 8;
			$index += 1;

			//take as much data as possible out of storedData
			while ($storedBitCount >= 5) {
				$storedBitCount -= 5;
				$output .= SHA1::$BASE32_ALPHABET[$storedData >> $storedBitCount];
				$storedData &= ((1 << $storedBitCount) - 1);
			} //whilte
		} //while

		//deal with leftover data
		if ($storedBitCount > 0) {
			$storedData <<= (5-$storedBitCount);
			$output .= SHA1::$BASE32_ALPHABET[$storedData];
		}

		return $output;
	} //base32encode
}
?>
