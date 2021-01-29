from sqlalchemy import Sequence, Column, Integer

Column(Integer, Sequence('user_id_seq'), primary_key=True)
