#!/usr/bin/env python3

from converter import Converter

a = Converter()
#a.run_cartesian( 'cartesian.dat' )
# a.run_zmatrix('benzene.dat', 'benzene.xyz')
# a.run_zmatrix('acetone.dat', 'acetone.xyz')
a.run_zmatrix('aceticacid.dat', 'aceticacid.xyz')
