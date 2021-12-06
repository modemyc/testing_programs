from study.func import funcdivision
import pytest

@pytest.mark.parametrize("x, y, result", [(6, 3, 2),
                                          (15, 3, 5),
                                          (100, 50, 2),
                                          (9, 3, 3),
                                          (5, 2, 2.5)
                                          ])

def test_funcdivision_positive(x, y, result):
    assert funcdivision(x, y) == result

@pytest.mark.parametrize("exem, divider, divisionable",
                         [(ZeroDivisionError, 0, 10),
                         (TypeError, "five", 10)])

def test_funcdivision_error(exem, divider, divisionable):
    with pytest.raises(exem):
        funcdivision(divisionable, divider)
