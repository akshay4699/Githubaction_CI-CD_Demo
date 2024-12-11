from src.math_operations import add_nums,sub_nums,mul_nums,div_nums

def test_add():
    assert add_nums(4,5)==9
    assert add_nums(-4,5)==1
    assert add_nums(0,5)==5

def test_sub():
    assert sub_nums(4,5)==-1
    assert sub_nums(-4,5)==1
    assert sub_nums(0,5)==-5

def test_mul():
    assert mul_nums(4,5)==20
    assert mul_nums(-4,5)==-20
    assert mul_nums(0,5)==0

def test_div():
    assert div_nums(4,5)==0.8
    assert div_nums(-4,5)==-0.8
    assert div_nums(0,5)==0
