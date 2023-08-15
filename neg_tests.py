from checker import checkout_neg

badarx = "/home/user/badarx"
folder = "/home/user/folder1"


def test_step1():
    res1 = checkout_neg(f"cd {badarx}; 7z e arx2.7z -o{folder} -y", "ERRORS")
    assert res1, "test1 FAIL"


def test_step2():
    assert checkout_neg(f"cd {badarx}; 7z t arx2.7z", "ERRORS"), "test2 FAIL"

