from .. import models
from sqlmodel import SQLModel, create_engine, Session, select


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)
SQLModel.metadata.create_all(engine)
valid_note = models.Note(name="test_file01", path="/teste_folder")


class TestDatabase:
    def setup_class(self):
        self.engine = engine
        self.valid_note = models.Note(name="test_file01", path="/teste_folder")

    def teardown(self):
        with Session(self.engine) as session:
            session.rollback()
            session.close()

    def test_valid_note(self):
        with Session(self.engine) as session:
            session.add(self.valid_note)
            session.commit()

            statement = select(models.Note).where(
                models.Note.name == self.valid_note.name,
                models.Note.path == self.valid_note.path,
                models.Note.type == self.valid_note.type,
                models.Note.parent == self.valid_note.parent,
            )
            result = session.exec(statement).first()
            assert result is not None
            assert result.name == self.valid_note.name


def test_valid_note():
    with Session(engine) as session:
        session.add(valid_note)
        session.commit()

        statement = select(models.Note).where(
            models.Note.name == valid_note.name,
            models.Note.path == valid_note.path,
            models.Note.type == valid_note.type,
            models.Note.parent == valid_note.parent,
        )
        result = session.exec(statement).first()
        assert result is not None
        assert result.name == valid_note.name

        session.rollback()
        session.close()
