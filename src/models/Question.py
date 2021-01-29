from optparse import Option
from typing import List
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from src.database import Base
from src.models.Answer import Answer


class Question(Base):
    __tablename__ = "question"

    question_id = Column(Integer(), primary_key=True)
    question = Column(String(), nullable=False, unique=True, index=True)
    answer = relationship("Answer", uselist=False, back_populates="question")

    def __init__(self, question: str, answer: Answer, options: List[Option] = None):
        self.question = question
        self.answer = answer
        if options:
            self.options = options
