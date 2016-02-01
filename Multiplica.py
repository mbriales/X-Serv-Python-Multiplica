#!/usr/bin/python
# -*- coding: utf-8 -*-
# Miguel Briales Romanillos

# Reads and checks arguments
for Op_1 in range(1, 11):
    print 'Tabla del %d' % Op_1
    print '-----------'
    for Op_2 in range(1, 11):
        print '%d por %d es %d' % (Op_1, Op_2, Op_1 * Op_2)
