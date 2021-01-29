from sqlalchemy import Column, Integer, ForeignKey, String, Sequence
from sqlalchemy.orm import relationship
from src.database import Base


class Answer(Base):
    __tablename__ = "answer"

    #id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    answer_id = Column(Integer(), primary_key=True)
    answer = Column(String(), nullable=False, index=True)
    question_id = Column(Integer(), ForeignKey("question.question_id"))

    question = relationship("Question", back_populates="answer")

    def __init__(self, answer: str, question_id: int = None):
        self.answer = answer
        self.question_id = question_id
