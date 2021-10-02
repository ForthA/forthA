from src.findHeight import findHeight


def findHeightTest():
    assert (findHeight([-1, 0], 2) == 2)
    assert (findHeight([4, -1, 4, 1, 1], 5) == 3)
    assert (findHeight([-1, 0, 4, 0, 3], 5) == 4)
    assert (findHeight([-1, 0, 0, 0, 2], 5) == 3)
    assert (findHeight([-1, 0, 1, 2, 3, 4, 5, 6, 7], 8) == 8)
    assert (findHeight([3, 3, 3, -1, 3, 3], 6) == 2)

