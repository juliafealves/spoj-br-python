# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: juliafealves
# Problem: QUERM - Quermesse

number_test = 0

while True:
    n = int(raw_input())
    number_test += 1

    if n == 0:
        break
    else:
        tickets = map(int, raw_input().split())

        for i in xrange(n):
            if i + 1 == tickets[i]:
                print 'Teste %i\n%i\n' % (number_test, tickets[i])
