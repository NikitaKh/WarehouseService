import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from domain.services import WarehouseService
from infrastructure.database import DATABASE_URL
from infrastructure.orm import Base
from infrastructure.repositories import (
    SqlAlchemyOrderRepository,
    SqlAlchemyProductRepository,
)
from infrastructure.unit_of_work import SqlAlchemyUnitOfWork

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

engine = create_engine(DATABASE_URL)
SessionFactory = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def main():
    logger.info("Запуск приложения WarehouseService")

    with SessionFactory() as session:
        logger.debug("Создана новая сессия SQLAlchemy")

        product_repo = SqlAlchemyProductRepository(session)
        order_repo = SqlAlchemyOrderRepository(session)

        with SqlAlchemyUnitOfWork(session) as uow:
            logger.info("Начало транзакции UnitOfWork")

            warehouse_service = WarehouseService(product_repo, order_repo)

            try:
                new_product = warehouse_service.create_product(name="test1", quantity=1, price=500)
                uow.commit()
                logger.info(f"Создан новый продукт: {new_product}")
            except Exception as e:
                uow.rollback()
                logger.exception("Ошибка при создании продукта. Отмена транзакции", e)


if __name__ == "__main__":
    main()
