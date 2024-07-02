import pytest

pytestmark = pytest.mark.django_db

class TestCategory:
    def test__str__method(self, category_factory):
        # Arrange
        # Act
        obj = category_factory(name="test_category")

        # Assert
        assert obj.__str__() == "test_category"

class TestBrand:
    def test__str__method(self, brand_factory):
        # Arrange
        # Act
        obj = brand_factory(name="test_brand")
        # Assert
        assert obj.__str__() == "test_brand"

class TestProduct:
    # Arrange
    # Act
    def test__str__method(self, product_factory):
        obj = product_factory(name="test_product")
    # Assert
        assert obj.__str__() == "test_product"
        
