from ... import models
from sqlmodel import SQLModel, create_engine, Session, select


Note = models.Note
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)
SQLModel.metadata.create_all(engine)
valid_note = Note(name="test_file01", path="/teste_folder")


class TestDatabase:
    def setup_class(self):
        self.engine = engine
        self.valid_note = Note(name="test_file01", path="/teste_folder")

    def teardown(self):
        with Session(self.engine) as session:
            session.rollback()
            session.close()

    def test_valid_note(self):
        with Session(self.engine) as session:
            session.add(self.valid_note)
            session.commit()

            statement = select(Note).where(
                Note.name == self.valid_note.name,
                Note.path == self.valid_note.path,
                Note.type == self.valid_note.type,
                Note.parent == self.valid_note.parent,
            )
            result = session.exec(statement).first()
            assert result is not None
            assert result.name == self.valid_note.name


def test_valid_note():
    with Session(engine) as session:
        session.add(valid_note)
        session.commit()

        statement = select(Note).where(
            Note.name == valid_note.name,
            Note.path == valid_note.path,
            Note.type == valid_note.type,
            Note.parent == valid_note.parent,
        )
        result = session.exec(statement).first()
        assert result is not None
        assert result.name == valid_note.name

        session.rollback()
        session.close()
