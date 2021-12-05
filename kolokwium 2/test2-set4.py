
total = 0
pts = 5
print('TEST 2')
print('-------------')


try:
    from F1 import f1
    assert f1([13,7,4,16,3,12,8],8) == 3
    assert f1([10,10,11,7,15],8) == 4
    total += pts
    print('F1:', pts, 'pts')
except:
    print('F1:', 0, 'pts')


try:
    from F2 import f2
    assert f2([23,7,16,34],[1,18,79,20]) == True
    assert f2([27],[1,18,4,9]) == True
    assert f2([23,7],[1,18,4,19,4]) == False
    total += pts
    print('F2:', pts, 'pts')
except:
    print('F2:', 0, 'pts')


try:
    from F3 import f3
    assert f3("78, 302 29; 14 - 69") == 14
    assert f3("31-650; B17 => G777") == 17
    total += pts
    print('F3:', pts, 'pts')
except:
    print('F3:', 0, 'pts')


try:
    from F4 import f4
    assert f4({"x":4,"y":7,"z":5}, False) == 12
    assert f4({"x":4,"y":7,"z":5,"n":9}, False) == 21
    assert f4({"x":4,"y":7}, True) == 4
    assert f4({"x":4,"y":8,"z":5, "n":8, "k":6}, True) == 26
    total += pts
    print('F4:', pts, 'pts')
except:
    print('F4:', 0, 'pts')


try:
    from F5 import f5
    assert f5(9,16) == "greet him"
    assert f5(6,19) == "came, "
    total += pts
    print('F5:', pts, 'pts')
except:
    print('F5:', 0, 'pts')


try:
    from F6 import f6
    assert f6(10000,15000,"Aquamarine") == 4
    assert f6(5000,19000,"Violet") == 7
    total += pts
    print('F6:', pts, 'pts')
except:
    print('F6:', 0, 'pts')




print('TOTAL:', total, 'pts')

