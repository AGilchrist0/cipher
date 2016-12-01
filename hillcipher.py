#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 17:26:51 2016

@author: aarongilchrist
"""

import numpy

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

cipher = 'HTPEGWEEHWAOHCPNIRXEIEXZGOGDQKUEGBYKHWAOCDOTQOTSLYOELDUMOSEQOQYTPRNNIGABADVQIAXVOODEEGWSSFQRGGSYEGWSSEQSXBTKBRFTGBYKBKEUQNETCKSOQBFOTSYQEOSURBCTEKYORMTPLRATTKMOBKEUOKCNDZMROTRNCOYWQKPSHVTCVNFTQETCALWAVVFUKBSKFHRASAQVFCRSGBTTTQWNEVYFRHEAQCHSQQTNNDPBTCPZEGREAKKOHURROCXNQGKNCQSTBSNQBMTZOOSEBORXKDEHEHROYKEOBBFIKQTTCIZCCORUIHGYTIMBAHOAWOOZSOQROCDSSOQDGEYMKLOAQKXOBKPSFHSVLKWTEHNATKTOUKNSIOCYDLTQGITNUOCRKCEPOSRQCQQCQSRHLWNOSKENNBTFLOLENAWBOCYTNETRNOWDEKSOQIPDWHEAWLOVVYFSCDOTLINSOSYQOPYNHTOCONRPTHNAWCOODYTCORETHLULAEQRPBNZCSEHCISDNRTNDTSPSQFCRBNPSYSRBEUELKEQTEYQQLZLYKSOBDKNTGTWBURRBLQAKBSCVLIIUVTFQBPAKGSTCLSFSCKSKSOBAOREBQEVCBHQBLSVIQOULKOTHQNFOIOSAHRATKTOXQUEHRYNBKPSKQOFNWSEUOCXSOQYOVEFSCNREQSPUOEDLFWKFORUINGTKGOASDQSGEYMKQOPIODEVSFNCERSQUPESOQYWBEKBQKPIADCOIUGNCTOIIVOQBTZCPENBHZKAGOYCQPCDETMIWFEBGEUEORYCGSYEKMOQIPDAOCUINGTHWAOQVTETVCUBTOYSOQYBQYBGLTNKVTFVQTFHSTQESRQDEUMUKNSIOCYFERRBLSRHQSTHKPETRPEWBEOSBQKQMPZBRUEBLHTHHCSBDACIGCYRENTHRAUQNENKTONOTWTHUIKHIOOSGQEGOHXIRWTEINSQYFFQNKTLTRSCNETRGEYDANRLHFPTKTOFDQTSOQRAGFTLHVNTSNYIIVOQETSBKFYOSEPQIVLTOYEHMIRWHEAWGOTBOQXRHRAKBRRGTXPRSEHFLRBIFLQOODEGAENOOUXWLELSEHTHMIRUDKQADVTIHROICCQTOYEHMIRIHWOIBCRQLPLWHEAWXOBOFYQEVRTRGXQLBQNTBYYREBTRTTEENRMSDHQOQXTCLOIFEQTHUATOOUWBNTSIBDUKHSNQVRARCTHVRSECQSNSOQYSFHRGUTROUREIOVUQPUTTLAVNVMTSLXDNHOAWBOEPGQECKEOTHEAUOTUVLCLBPEQGCEEKQNTBGEUEORYEBTQGELRSOQYVTTYHMIRVTTXHQOVFOKRKQFENKNOBLELCQRRWGOEOLSOGEYNHUATOVUFNHTZXDSTULQFSCQQGHYCNVSCUEURLKASLODTSBQRMRPETLMENHTASGSTFOTDHQTUNIWQIPOKOMEGGFTTGOEXVTCMBMARGEYNKFOSKTYEOBDUKBSEMCTRQVRIUITZBRYDCFSOSCQRLIQOEAEBBSRQGPECDAQVBDUBGCYEQETSBKFYGEYNOUTEQTTNGSUQDKSYSGBZUFKRLOBGTVWIWSOQOKDYSGBZUCKRGEYIGOENKKOMANE'

wordlen = 2

key = numpy.matrix('7 14; 11 4')

finished = []

vectors = []

plaintext = ''

for i in range(len(cipher) // wordlen):
    finished.append(cipher[i*wordlen:(i+1)*wordlen])

finished.append(cipher[len(cipher)-len(cipher)%wordlen:])

i = 0
for thing in finished:
    matrixtext = ''
    for letter in thing:
        matrixtext = matrixtext + str(alphabet.index(letter))
        matrixtext = matrixtext + ';'
        i+=1
    matrixtext = matrixtext[:-1]
    ''''if i%3 == 1:
        matrixtext = matrixtext + ';0'
    elif i%3 == 2:
        matrixtext = matrixtext + ';0'''
    vectors.append(matrixtext)

while i%3 != 2:
    vectors[len(vectors)-1] += ';0'
    i+=1
    
for vector in vectors:
    result = numpy.matmul(key,numpy.matrix(vector))
    for x in range(0,wordlen):
        plaintext = plaintext + alphabet[result.item(x)%26]
print(plaintext)

cipher = numpy.matrix('1;2;3')