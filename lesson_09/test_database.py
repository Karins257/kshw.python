from uuid import uuid4


def test_add_row(db_table):
    label = f"SkyPro add {uuid4()}"
    row_id = db_table.add(db_table.build_row(label))

    try:
        created_row = db_table.get(row_id)
        assert created_row is not None
        assert created_row[db_table.editable_column.name] == label
    finally:
        db_table.remove(row_id)


def test_update_row(db_table):
    initial_label = f"SkyPro initial {uuid4()}"
    row_id = db_table.add(db_table.build_row(initial_label))

    try:
        updated_label = f"SkyPro updated {uuid4()}"
        db_table.change_label(row_id, updated_label)

        updated_row = db_table.get(row_id)
        assert updated_row[db_table.editable_column.name] == updated_label
    finally:
        db_table.remove(row_id)


def test_delete_row(db_table):
    label = f"SkyPro delete {uuid4()}"
    row_id = db_table.add(db_table.build_row(label))

    db_table.remove(row_id)

    assert db_table.get(row_id) is None
