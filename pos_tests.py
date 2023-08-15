from checker import checkout

tst = "/home/user/tst"
out = "/home/user/out"
folder = "/home/user/folder1"


def test_step1():
    res1 = checkout(f"cd {tst}; 7z a {out}/arx2", "Everything is Ok")
    res2 = checkout(f"ls {out}", "arx2.7z")
    assert res1 and res2, "test1 FAIL"


def test_step2():
    res1 = checkout(f"cd {out}; 7z e arx2.7z -o{folder} -y", "Everything is Ok")
    res2 = checkout(f"ls {folder}", "test1")
    res3 = checkout(f"ls {folder}", "test2")
    assert res1 and res2 and res3, "test2 FAIL"


def test_step3():
    assert checkout(f"cd {out}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step4():
    assert checkout(f"cd {tst}; 7z u {out}/arx2.7z", "Everything is Ok"), "test4 FAIL"


def test_step5():
    assert checkout(f"cd {out}; 7z d arx2.7z", "Everything is Ok"), "test5 FAIL"


def test_step6():
    res1 = checkout(f"cd {out}; 7z l arx2.7z", "test1")
    res2 = checkout(f"cd {out}; 7z l arx2.7z", "test2")
    assert res1 and res2, "test6 FAIL"


def test_step7():
    res1 = checkout(f"cd {out}; 7z x arx2.7z -o{folder} -y", "Everything is Ok")
    res2 = checkout(f"ls {folder}", "test1")
    res3 = checkout(f"ls {folder}", "test2")
    assert res1 and res2 and res3, "test2 FAIL"


def test_step8():
    assert checkout(f"cd{tst}; 7z h test1", "Everything is Ok"), "test8 FAIL"

