from context import get_context, register_dataloaders
from dataloaders import CountryLoader, NewsLoader


def test_get_context():
    """
    Тестирование контекста
    """
    context = get_context()

    assert len(context) == 1
    assert context.keys() == {"dataloaders"}
    assert isinstance(context["dataloaders"], dict)
    assert len(context["dataloaders"]) == 2

    dataloaders = context["dataloaders"]
    assert dataloaders.keys() == {"countries", "news"}
    assert isinstance(dataloaders["countries"], CountryLoader)
    assert isinstance(dataloaders["news"], NewsLoader)


def test_register_dataloaders():
    """
    Тестирование содержимого контекста
    """
    dataloaders = register_dataloaders()

    assert len(dataloaders) == 2
    assert isinstance(dataloaders, dict)
    assert dataloaders.keys() == {"countries", "news"}

    assert isinstance(dataloaders["countries"], CountryLoader)
    assert isinstance(dataloaders["news"], NewsLoader)