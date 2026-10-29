from cutils import CUtils


def test_create_var_sets_once():
    c = CUtils()
    c.create_var("speed", 1)
    c.create_var("speed", 99)
    assert c.speed == 1
