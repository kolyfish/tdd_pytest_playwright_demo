import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from tdd_demo.models import Base
from playwright.sync_api import Page


@pytest.fixture(scope="function")
def sqlite_session_fixture() -> Session:
    engine_url = "sqlite:///"
    engine = create_engine(engine_url)

    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def page_with_timeout(page: Page) -> Page:
    """設置 Playwright page 的預設等待時間"""
    page.set_default_timeout(10_000)
    return page

