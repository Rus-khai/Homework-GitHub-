import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "info_card, expected_result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ],
)
def test_mask_account_card(info_card, expected_result):
    assert mask_account_card(info_card) == expected_result

    with pytest.raises(ValueError, match="Не правильный номер карты"):
        assert mask_account_card("")

    with pytest.raises(ValueError, match="Не правильный номер карты"):
        assert mask_account_card("vhbhfhvjsv13121")


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

    with pytest.raises(TypeError, match="Не правильный тип даты"):
        assert get_date([12121221])
