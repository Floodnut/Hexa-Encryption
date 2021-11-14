'''
#2021 정보보안
#4조
#20163048 남시현
'''

from mkeyShift      import Mstate, Mkey, Shift, dShift
from box            import fill_box, down_row_shift, up_row_shift, left_col_shift, right_col_shift
from hexadoku       import CreateTable
from table          import p_table, xor_table
from test           import hexadoku, puzzle
import numpy as np

#import mkeyShift,hexadoku,box,table,test


def CreateState(_text): #평문 -> 256 16*16
    state = Mstate(_text)
    return state

def CreateKey(_text):    #평문 -> 키
    key = Mkey(_text)
    return key

def CreateBox(_key): #키 -> 박스
    cBox = fill_box(_key)
    return cBox

def CreateTable(_box) : #key -> box -> table
    eTable = CreateTable( _box )      #empty table
    #Table = hexadoku(eTable, 0, 0)   #Create Table

    #table = puzzle(cTable)         #return?.. 일단 코드 있길레 씀.

    return 0#table



def Round(_state, _key,_box,_table) :  #key_s - 테이블전치 - xor - box_s

    _key = Shift(_key)             #shift key
    _table = p_table(_state, _table)   #table 전치
    state = xor_table(_state, _key)    #XOR

    return state

def BoxShift(_box,_round):    #8까지 우하 16까지 좌상

    if round < 9:
        if _round % 2 == 0 :
            _box = down_row_shift(_box)
        else:
            _box = right_col_shift(_box)

    else :
        if _round % 2 == 0:
            _box = left_col_shift(_box)
        else:
            _box = up_row_shift(_box)

    return 0


def main():
    #평문패딩 생략 8bit * 32자.
    t = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    state = CreateState(t)
    key = CreateKey(t)
    box = CreateBox(key)
    table = CreateTable(box)

    '''
    for i in range(16):
        state = Round(state,key,box,table)  #key_s - table 전치 - xor - box_s

        Round(state,key,box,table)
        BoxShift(box, i)
    '''


    print (state)


if __name__=="__main__":
    main()