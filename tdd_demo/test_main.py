import os
import pytest
from .main import get_ptt_boards, insert_ptt_board
from .models import Board
from playwright.sync_api import expect


@pytest.mark.skipif(
    os.getenv("CI") == "true",
    reason="在 CI 環境中跳過，使用 Playwright 測試替代（test_verify_stock_board_exists）"
)
def test_get_ptt_boards():
    """使用 requests 取得 PTT 看板列表（本地測試用）"""
    expected = "Stock"

    result = get_ptt_boards()
    print(result)

    assert expected in result


def test_verify_stock_board_exists(page_with_timeout):
    """驗證 PTT 網站上是否存在 Stock 看板"""
    page = page_with_timeout
    page.goto("https://www.ptt.cc/bbs/index.html")
    page.wait_for_load_state("networkidle")

    stock_board = page.locator("div.board-name", has_text="Stock")
    stock_board.wait_for(state="visible")

    expect(stock_board).to_contain_text("Stock")


# 寫入 board 資料庫的功能
def test_insert_ptt_board(sqlite_session_fixture):
    """寫入 board 資料庫"""
    expected = "test"

    insert_ptt_board(name=expected, session=sqlite_session_fixture)

    board = sqlite_session_fixture.query(Board).filter(Board.name == expected).first()
    assert board is not None
    assert board.name == expected
