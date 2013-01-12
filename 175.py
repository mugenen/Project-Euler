#http://d.hatena.ne.jp/inamori/20121116/p1

import fractions

a = 123456789
b = 987654321
#a = 13
#b = 17

gcd = fractions.gcd(a, b)
a /= gcd
b /= gcd

a, b = max(a, b), min(b, a)
result = []
while a % b != 0:
    quotient, remainder = divmod(a, b)
    print a, b, quotient, remainder
    a, b = b, min(b, remainder)
    result.append(quotient)

print a, b
result.append(a / b)

#Ç»Ç∫Ç©ÇÌÇ©ÇÁÇ»Ç¢ÅcÅc
if len(result) % 2 == 0:
    result[-1] -= 1
    result += [1]

print ','.join(map(str, result[::-1]))
