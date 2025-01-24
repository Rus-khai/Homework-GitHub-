import pytest


from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(70007922896063611)
    assert str(exc_info.value) == "Не правильный номер карты"

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number('')
    assert str(exc_info.value) == "Не правильный номер карты"


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"

    with pytest.raises(ValueError) as exc_info:
        get_mask_account(736541084301358743051)
    assert str(exc_info.value) == "Не правильный номер карты"

    with pytest.raises(ValueError) as exc_info:
        get_mask_account('')
    assert str(exc_info.value) == "Не правильный номер карты"
