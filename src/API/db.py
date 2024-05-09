from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


from config import db_url


class DB:
    def __init__(self, url: str, echo: bool = False):

        self.engine = create_async_engine(
            url,
            echo=echo
        )

        self.async_session = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def get_async_session(self) -> AsyncSession:
        async with self.async_session() as session:
            yield session
