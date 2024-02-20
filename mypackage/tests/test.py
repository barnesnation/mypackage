from mypackage import myModule

def test_top_n():

    assert myModule.top_n([8,1,3,6,9],3) == [9,8,6], 'incorrect'
    assert myModule.top_n([5,2,4,7,9],3) == [9,7,5], 'incorrect'
    assert myModule.top_n([0,1,3,6,10],3) == [10,6,3], 'incorrect'
