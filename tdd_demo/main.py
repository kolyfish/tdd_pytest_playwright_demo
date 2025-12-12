from datetime import datetime
from sqlalchemy.orm import Session
from .models import Board


def insert_ptt_board(name: str, session: Session):
    board = Board(
        name=name,
        created_time=datetime.now()
    )
    session.add(board)
    session.commit()
