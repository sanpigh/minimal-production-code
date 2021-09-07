from minimal_production_code.simple_request import get_sum


def test_get_sum():
    status, sumation = get_sum(3,4)
    assert status == 200
    assert sumation == 7
    return