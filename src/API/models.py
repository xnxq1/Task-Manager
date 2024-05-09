from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column()

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()