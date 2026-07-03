import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(0, 0, [0, 0]),
        pytest.param(14, 14, [0, 0]),
        pytest.param(15, 15, [1, 1]),
        pytest.param(23, 23, [1, 1]),
        pytest.param(24, 24, [2, 2]),
        pytest.param(27, 27, [2, 2]),
        pytest.param(28, 28, [3, 2]),
        pytest.param(100, 100, [21, 17]),
    ]
)
def test_should_return_correct_age(cat_age: int,
                                   dog_age: int,
                                   expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_exception",
    [
        pytest.param(-1, 14, ValueError, id="negative cat age"),
        pytest.param(14, -1, ValueError, id="negative dog age"),
        pytest.param(-1, -1, ValueError, id="negative ages"),
        pytest.param("14", 14, TypeError, id="string cat age"),
        pytest.param(14, "14", TypeError, id="string dog age"),
    ]
)
def test_should_raise_valid_exception(cat_age: int,
                                      dog_age: int,
                                      expected_exception: Exception) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
