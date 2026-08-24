import pytest

from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


@pytest.mark.parametrize(
    "source, expected",
    [
        ("skypro", "Skypro"),
        ("Skypro", "Skypro"),
        ("123 test", "123 test"),
        ("04 апреля 2023", "04 апреля 2023"),
        ("", ""),
        (" ", " "),
    ],
)
def test_capitalize(utils, source, expected):
    assert utils.capitalize(source) == expected


@pytest.mark.xfail(
    strict=True,
    reason="capitalize изменяет регистр остальных символов",
)
def test_capitalize_preserves_other_characters(utils):
    assert utils.capitalize("sKYPRO") == "SKYPRO"


def test_capitalize_none(utils):
    with pytest.raises(AttributeError):
        utils.capitalize(None)


@pytest.mark.parametrize(
    "source, expected",
    [
        ("   skypro", "skypro"),
        ("skypro", "skypro"),
        ("sky pro", "sky pro"),
        ("skypro   ", "skypro   "),
        ("   ", ""),
        ("", ""),
    ],
)
def test_trim(utils, source, expected):
    assert utils.trim(source) == expected


def test_trim_none(utils):
    with pytest.raises(AttributeError):
        utils.trim(None)


@pytest.mark.parametrize(
    "source, symbol, expected",
    [
        ("SkyPro", "S", True),
        ("SkyPro", "Pro", True),
        ("SkyPro", "U", False),
        ("SkyPro", "s", False),
        ("123", "2", True),
        ("04 апреля 2023", " ", True),
        ("", "S", False),
        (" ", " ", True),
    ],
)
def test_contains(utils, source, symbol, expected):
    assert utils.contains(source, symbol) is expected


def test_contains_none_source(utils):
    with pytest.raises(AttributeError):
        utils.contains(None, "S")


def test_contains_none_symbol(utils):
    with pytest.raises(TypeError):
        utils.contains("SkyPro", None)


@pytest.mark.parametrize(
    "source, symbol, expected",
    [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("SkyProSky", "Sky", "Pro"),
        ("SkyPro", "U", "SkyPro"),
        ("123123", "12", "33"),
        ("04 апреля 2023", " ", "04апреля2023"),
        ("", "S", ""),
        (" ", " ", ""),
    ],
)
def test_delete_symbol(utils, source, symbol, expected):
    assert utils.delete_symbol(source, symbol) == expected


def test_delete_symbol_none_source(utils):
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "S")


def test_delete_symbol_none_symbol(utils):
    with pytest.raises(TypeError):
        utils.delete_symbol("SkyPro", None)
