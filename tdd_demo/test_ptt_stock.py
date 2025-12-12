from playwright.sync_api import expect


def test_verify_stock_board_exists(page_with_timeout):
    """驗證 PTT 網站上是否存在 Stock 看板"""
    page = page_with_timeout
    page.goto("https://www.ptt.cc/bbs/index.html")
    page.wait_for_load_state("networkidle")

    stock_board = page.locator("div.board-name", has_text="Stock")
    stock_board.wait_for(state="visible")

    expect(stock_board).to_contain_text("Stock")


