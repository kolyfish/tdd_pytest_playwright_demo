"""使用 Playwright 查詢 PTT 看板列表並列印"""
from playwright.sync_api import sync_playwright


def get_ptt_boards_with_playwright():
    """使用 Playwright 查詢 PTT 看板列表"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_default_timeout(10_000)

        # 導航到 PTT 看板列表頁面
        page.goto("https://www.ptt.cc/bbs/index.html")
        page.wait_for_load_state("networkidle")

        # 等待看板列表載入
        page.wait_for_selector("div.board-name", state="visible")

        # 查詢所有看板名稱
        board_elements = page.locator("div.board-name")
        board_count = board_elements.count()

        print(f"\n找到 {board_count} 個看板：\n")
        print("=" * 50)

        boards = []
        for i in range(board_count):
            board_name = board_elements.nth(i).inner_text()
            boards.append(board_name)
            print(f"{i + 1:4d}. {board_name}")

        print("=" * 50)
        print(f"\n總共 {len(boards)} 個看板\n")

        browser.close()
        return boards


if __name__ == "__main__":
    get_ptt_boards_with_playwright()

