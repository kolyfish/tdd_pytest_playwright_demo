import requests
from bs4 import BeautifulSoup
from datetime import datetime
from sqlalchemy.orm import Session
from .models import Board


def get_ptt_boards():
    url = "https://www.ptt.cc/bbs/index.html"

    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")

    board_names = soup.find_all(name="div", attrs={"class": "board-name"})
    return [board.get_text() for board in board_names]


def insert_ptt_board(name: str, session: Session):
    board = Board(
        name=name,
        created_time=datetime.now()
    )
    session.add(board)
    session.commit()