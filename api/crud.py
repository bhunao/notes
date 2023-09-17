from api.database import db_cursor
from datetime import datetime
from logging import getLogger
from sqlite3 import IntegrityError

path = "../../notes/z_bkp/"
log = getLogger(__name__)


def query(fields, table="notes"):
    named_fields = [
        f"{field_name} = :{field_name}" for field_name in fields.keys()]
    named_fields_clause = ' AND '.join(named_fields)

    with db_cursor() as cursor:
        data = cursor.execute(
            f"SELECT * FROM {table} where {named_fields_clause}", fields)
        log.info(f"data selected from table: {table}")
        return data.fetchall()


def insert_db(fields, table="notes"):
    insert_fields_clause = ", ".join(fields.keys())
    named_fields_clause = f":{', :'.join(fields.keys())}"

    try:
        with db_cursor() as cursor:
            data = cursor.execute(
                f"INSERT INTO {table} ({insert_fields_clause}) "
                f"values ({named_fields_clause})", fields
            )
            log.info(f"data {data.description} inserted into table {table}")
            return data.rowcount > 0
    except IntegrityError as e:
        log.error(e)
        return False


def update_db(field_id_name, field_id_value, fields_to_update, table="notes"):
    set_fields_clause = ", ".join(
        [f"{field_name}= :{field_name}" for field_name in fields_to_update.keys()])
    fields_to_update[field_id_name] = field_id_value

    with db_cursor() as cursor:
        data = cursor.execute(
            f"UPDATE {table} SET {set_fields_clause} "
            f"WHERE {field_id_name}= :{field_id_name}", fields_to_update
        )
        log.info(f"data {data.fetchall()} updated in table {table}")
        return data.rowcount > 0


def delete_db(table, field_name, field_value):
    with db_cursor() as cursor:
        data = cursor.execute(
            f"DELETE FROM {table} where"
            f"{field_name}= :{field_name}", {field_name: field_value}
        )
        return data.rowcount > 0


def create_note(name, path, parent=None):
    data = {
        "name": name,
        "path": path,
        "created_at": datetime.now(),
        "last_edit": datetime.now(),
        "parent": parent if parent else path,
    }
    if query({"name": name, "path": path}):
        return None
    result = insert_db(data)
    return result
