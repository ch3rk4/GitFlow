from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    Product("Купить огурцы", "Купить огурцы для салата", 300.0, 10)
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "Product('Купить огурцы', 'Купить огурцы для салата', 300.0, 10)"
    )

    Smartphone("Iphone", "Glade", 300.0, 10, 1200, "XR", 128, "Black")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone('Iphone', 'Glade', 300.0, 10)"

    LawnGrass("Green grass", "Green grass", 1500, 10000, "England", 6, "black")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass('Green grass', 'Green grass', 1500, 10000)"
