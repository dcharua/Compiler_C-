#dDaniel Charua - A01017419

from globalTypes import *
from parser import *
from semantica import *
from cgen import *

f = open('sample.c-', 'r')
programa = f.read()
progLong = len(programa)
programa = programa + '$'
posicion = 0

globales(programa, posicion, progLong)
AST = parser(True)
semantica(AST, True)
codeGen(AST, 'file.s')