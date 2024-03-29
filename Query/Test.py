from unittest import TestCase

from Query import Query


class Test(TestCase):
    """Test with coverage

    `coverage run -m unittest Test.py && coverage html`
    """

    def testCreate(self):
        self.assertEqual(
            str(Query().insert("table").values({"id": 0, "name": "'name'"})),
            "INSERT INTO table (id, name) VALUES (0, 'name')",
        )

    def testCreateShort(self):
        self.assertEqual(
            str(Query().insert("table", {"id": 0, "name": "'name'"})),
            "INSERT INTO table (id, name) VALUES (0, 'name')",
        )

    def testRead(self):
        self.assertEqual(
            str(
                Query()
                .select(["id", "name"])
                .from_table("table")
                .where("id = 0")
                .and_("deleted = 0")
                .order("main DESC")
                .limit(0, 10)
            ),
            "SELECT id, name FROM table WHERE id = 0 AND deleted = 0 ORDER BY"
            " main DESC LIMIT 0, 10",
        )
        self.assertEqual(
            str(
                Query()
                .select("id, name")
                .from_table("table")
                .where("id = 0")
                .and_("deleted = 0")
                .order("main DESC")
                .limit(0, 10)
            ),
            "SELECT id, name FROM table WHERE id = 0 AND deleted = 0 ORDER BY"
            " main DESC LIMIT 0, 10",
        )

    def testReadShort(self):
        self.assertEqual(
            str(
                Query()
                .select(["id", "name"], "table", ["id = 0", "deleted = 0"])
                .order("main DESC")
                .limit(10)
            ),
            "SELECT id, name FROM table WHERE id = 0 AND deleted = 0 ORDER BY"
            " main DESC LIMIT 10",
        )

    def testJoin(self):
        self.assertEqual(
            str(
                Query()
                .select(["t.id", "t.name"])
                .from_table("table t")
                .join("other o", "o.tableId = t.id")
                .where("t.id = 0")
                .and_("t.deleted = 0")
            ),
            "SELECT t.id, t.name FROM table t INNER JOIN other o ON o.tableId"
            " = t.id WHERE t.id = 0 AND t.deleted = 0",
        )

    def testJoinShort(self):
        self.assertEqual(
            str(
                Query()
                .select(
                    ["t.id", "t.name"],
                    "table t",
                    ["t.id = 0", "t.deleted = 0"]
                )
                .join("other o", "o.tableId = t.id")
            ),
            "SELECT t.id, t.name FROM table t INNER JOIN other o ON o.tableId"
            " = t.id WHERE t.id = 0 AND t.deleted = 0",
        )

    def testLeftJoin(self):
        self.assertEqual(
            str(
                Query()
                .select(["t.id", "t.name"])
                .from_table("table t")
                .left("other o", "o.tableId = t.id")
                .where("t.id = 0")
                .and_("t.deleted = 0")
            ),
            "SELECT t.id, t.name FROM table t LEFT JOIN other o ON o.tableId"
            " = t.id WHERE t.id = 0 AND t.deleted = 0",
        )

    def testLeftJoinShort(self):
        self.assertEqual(
            str(
                Query()
                .select(
                    ["t.id", "t.name"],
                    "table t",
                    ["t.id = 0", "t.deleted = 0"]
                )
                .left("other o", "o.tableId = t.id")
            ),
            "SELECT t.id, t.name FROM table t LEFT JOIN other o ON o.tableId"
            " = t.id WHERE t.id = 0 AND t.deleted = 0",
        )

    def testUpdate(self):
        self.assertEqual(
            str(
                Query()
                .update("table")
                .set({"name": "'new name'", "number": 1, "string": "'str'"})
                .where("id = 0")
                .and_("deleted = 0")
            ),
            "UPDATE table SET name = 'new name', number = 1, string = 'str'"
            " WHERE id = 0 AND deleted = 0",
        )

    def testUpdateShort(self):
        self.assertEqual(
            str(
                Query().update(
                    "table",
                    {"name": "'new name'", "number": 1, "string": "'str'"},
                    ["id = 0", "deleted = 0"],
                )
            ),
            "UPDATE table SET name = 'new name', number = 1, string = 'str'"
            " WHERE id = 0 AND deleted = 0",
        )

    def testDelete(self):
        self.assertEqual(
            str(Query().delete().from_table("table").where("id = 0")),
            "DELETE FROM table WHERE id = 0",
        )

    def testDeleteShort(self):
        self.assertEqual(
            str(Query().delete("table", "id = 0")
                ), "DELETE FROM table WHERE id = 0"
        )

    def testAnd(self):
        self.assertEqual(
            str(
                Query()
                .delete()
                .from_table("table")
                .where("id = 0")
                .and_(["user_id = 1", "is_public = 1"])
            ),
            "DELETE FROM table WHERE id = 0 AND user_id = 1 AND is_public = 1",
        )

    def testOr(self):
        self.assertEqual(
            str(
                Query()
                .select(["id", "name"], "table", "id = 0")
                .or_("user_id = 1")
            ),
            "SELECT id, name FROM table WHERE id = 0 OR user_id = 1",
        )
        self.assertEqual(
            str(
                Query()
                .select(["id", "name"], "table", "id = 0")
                .or_(["user_id = 1", "is_public = 1"])
            ),
            "SELECT id, name FROM table WHERE id = 0 OR user_id = 1 "
            "OR is_public = 1",
        )
