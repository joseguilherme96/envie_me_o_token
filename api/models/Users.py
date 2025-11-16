from db import db
from sqlalchemy import Integer, String, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Users(db.model):

    login : Mapped[str] = mapped_column(unique=True,primary_key=True)
    senha : Mapped[str] = mapped_column(String(30))
    tipo_usuario_id : Mapped[int] = mapped_column(Integer,ForeignKey("cod_tipo_user"),name="tipo_usuario_id")