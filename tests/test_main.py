import pytest


@pytest.fixture
def tst_tuple():
    a = (1, 2, 3, 1, 4)
    return a


@pytest.fixture
def tst_dict():
    a = {
        1: "a",
        2: "b"
    }
    return a


class Test_tuple:
    @pytest.mark.parametrize(
        "i, res",
        [
            (0, 1),
            (1, 2),
            (-1, 4),
        ]
    )
    def test_index(self, i, res, tst_tuple):
        assert tst_tuple[i] == res

    def test_change(self, tst_tuple):
        with pytest.raises(TypeError):
            tst_tuple[0] = 0

    def test_count(self, tst_tuple):
        assert tst_tuple.count(1) == 2


class Test_dict:
    def test_get(self, tst_dict):
        assert tst_dict.get(1) == "a"

    def test_rewrite(self, tst_dict):
        tst_dict[2] = "c"
        assert tst_dict[2] == "c"

    def test_update(self, tst_dict):
        tst_dict.update({3: "c", 4: "d"})
        assert tst_dict == {1: "a", 2: "b", 3: "c", 4: "d"}
