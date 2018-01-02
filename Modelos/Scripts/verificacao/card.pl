#!/usr/bin/perl

#############################################
##                                         ##
##  http://koubacktr.wordpress.com     ##
##  http://twitter.com/kouback_tr_     ##
##                                         ##
#############################################
## Validador de cartão de créditoe  débito ##
## Verify card                             ##
## By KoubackTr 2014                       ##
#############################################

print <<a;
===========================================================
Valid Card // Validador de cartões de crédito e débito //
===========================================================
a
$card=$ARGV[0] || die "Use: validcard.pl <card number> \n";

my $cartao = length($card);

if($cartao==16){ # exigi 16 digitos no numro do cartão

# DIVIDINDO STRINGS E PEGANDO VALORES PARA ENGENHARIA
$numerocartao = "$card";
my @validade = split(//,$numerocartao);

$v1=$validade[0]*2," ";
$s1=$validade[1];
$v2=$validade[2]*2," ";
$s2=$validade[3];
$v3=$validade[4]*2," ";
$s3=$validade[5];
$v4=$validade[6]*2," ";
$s4=$validade[7];
$v5=$validade[8]*2," ";
$s5=$validade[9];
$v6=$validade[10]*2," ";
$s6=$validade[11];
$v7=$validade[12]*2," ";
$s7=$validade[13];
$v8=$validade[14]*2," ";
$s8=$validade[15];
$v9=$validade[16]*2,"";

my $n1="$v1$v2$v3$v4$v5$v6$v7$v8$v9";
my @validade2 = split(//,$n1);
    $vv0=$validade2[0];
    $vv1=$validade2[1];
    $vv2=$validade2[2];
    $vv3=$validade2[3];
    $vv4=$validade2[4];
    $vv5=$validade2[5];
        $vv6=$validade2[6];
    $vv7=$validade2[7];
    $vv8=$validade2[8];
    $vv9=$validade2[9];
    $vv10=$validade2[10];
    $vv11=$validade2[11];
    $vv12=$validade2[12];
    $vv13=$validade2[13];
    $vv14=$validade2[14];
    $vv15=$validade2[15];
    $vv16=$validade2[16];
    $vv17=$validade2[17];
    $vv18=$validade2[18];
    $vv19=$validade2[19];
############### // Somando tudo // ##############
my $d0 = $vv0 + $vv1 + $s1 + $vv2 + $s2 +$vv3 + $s3 + $vv4 + $s4 + $vv5 + $s5 + $vv6 + $s6 + $vv7 + $s7 + $vv8 + $s8 + $vv9 + $vv10 + $vv11 + $vv12 + $vv13 + $vv14 + $vv15 + $vv16 + $vv17 + $vv18 + $vv19;

##### CONDIÇÃO: se ultimo numero do resultado da soma é = 0 isso significa que é divisivel por 10
#####           se é divisiovel por 10, é válido, se não, é inválido

my $val=$d0 / 10;
my @validade3 = split(//,$d0);
    $val0=$validade3[0];
    $val1=$validade3[1];
}else{
die "\n\t\t\t[!] Numero inválido, deve conter 16 digitos.\n\n";
}
if($val1==0){
print "\n\t\t\t[+] Cartão Válido\n\n";   #Retorno válido
}else{
print "\n\t\t\t[!] Cartão Inválido\n\n"; #Retorno inválido
}