from app import miles_to_kilometers


def test_miles_to_kilometers():
    assert miles_to_kilometers(1) == 1.60934
    assert miles_to_kilometers(5) == 8.04672
