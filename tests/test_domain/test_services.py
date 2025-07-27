import logging

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import clear_mappers, sessionmaker

from domain.services import WarehouseService
from infrastructure.orm import Base, ProductORM
from infrastructure.repositories import (
    SqlAlchemyOrderRepository,
    SqlAlchemyProductRepository,
)

# Настройка логгера
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@pytest.fixture
def session():
    logger.info("Создание in-memory базы данных")
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        yield session
    clear_mappers()
    logger.info("Очистка мапперов SQLAlchemy")


@pytest.fixture
def warehouse_service(session):
    logger.info("Инициализация WarehouseService с SQLAlchemy репозиториями")
    product_repo = SqlAlchemyProductRepository(session)
    order_repo = SqlAlchemyOrderRepository(session)
    return WarehouseService(product_repo, order_repo)


def test_create_product(session, warehouse_service):
    logger.info("Тест: создание продукта")
    warehouse_service.create_product(name="TestProduct", quantity=5, price=99.99)
    session.commit()

    logger.info("Проверка продукта в базе данных")
    result = session.query(ProductORM).filter_by(name="TestProduct").first()

    assert result is not None, "Продукт не найден в базе"
    assert result.name == "TestProduct"
    assert result.quantity == 5
    assert result.price == 99.99
    logger.info(f"Продукт успешно создан и найден: {result.name}")
