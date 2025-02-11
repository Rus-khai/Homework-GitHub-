import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def number():
    return 7000792289606361


def test_get_mask_card_number(number):
    assert get_mask_card_number(number) == "7000 79** **** 6361"

    with pytest.raises(TypeError, match="Не правильный тип номера карты"):
        get_mask_card_number([])

    with pytest.raises(ValueError, match="Не правильный номер карты"):
        get_mask_card_number("")


@pytest.fixture
def account():
    return 73654108430135874305


def test_get_mask_account(account):
    assert get_mask_account(account) == "**4305"

    with pytest.raises(ValueError, match="Не правильный номер счёта"):
        assert get_mask_account(736541084301358743051)

    with pytest.raises(ValueError, match="Не правильный номер счёта"):
        get_mask_account("")

    with pytest.raises(TypeError, match="Не правильный тип счёта"):
        get_mask_account([])
