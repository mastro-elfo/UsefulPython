class Query(object):
    def __init__(self):
        (
            self._method,
            self._table,
            self._from,
            self._where,
            self._order,
            self._limit,
            self._select_cols,
            self._columns,
            self._values,
            self._set,
            self._joins,
            self._lefts,
        ) = (
            "",
            "",
            "",
            "",
            list(),
            "",
            list(),
            list(),
            list(),
            list(),
            dict(),
            dict(),
        )

    def __str__(self):
        query = ""

        query += self._method

        if self._select_cols:
            if isinstance(self._select_cols, list):
                query += f" {', '.join(self._select_cols)}"
            else:
                query += f" {self._select_cols}"

        if self._from:
            query += f" FROM {self._from}"

        if self._table:
            query += f" {self._table}"

        if self._columns:
            query += f" ({', '.join(self._columns)})"

        if self._values:
            query += f" VALUES ({', '.join(str(val) for val in self._values)})"

        if self._set:
            query += f" SET {', '.join(self._set)}"

        if self._joins:
            for join, on in self._joins.items():
                query += f" INNER JOIN {join} ON {on}"

        if self._lefts:
            for join, on in self._lefts.items():
                query += f" LEFT JOIN {join} ON {on}"

        if self._where:
            query += f" WHERE {self._where}"

        if self._order:
            query += f" ORDER BY {', '.join(self._order)}"

        if self._limit:
            query += f" LIMIT {self._limit}"

        return query

    def method(self, method):
        self._method = method
        return self

    def select(self, cols="*", from_table="", where=""):
        self._select_cols = cols
        self.method("SELECT")
        if from_table:
            self.from_table(from_table)
        if where:
            self.where(where)
        return self

    def insert(self, table, values=None):
        self._table = table
        self.method("INSERT INTO")
        if values:
            self.values(values)
        return self

    def update(self, table, set_values=None, where=""):
        self._table = table
        self.method("UPDATE")
        if set_values:
            self.set(set_values)
        if where:
            self.where(where)
        return self

    def delete(self, from_table="", where=""):
        self.method("DELETE")
        if from_table:
            self.from_table(from_table)
        if where:
            self.where(where)
        return self

    def set(self, cols=None):
        if cols:
            self._set = [f"{key} = {value}" for key, value in cols.items()]
        return self

    def values(self, cols=None):
        if cols:
            self._columns = cols.keys()
            self._values = cols.values()
        return self

    def from_table(self, table):
        self._from = table
        return self

    def join(self, join, on):
        self._joins[join] = on
        return self

    def left(self, join, on):
        self._lefts[join] = on
        return self

    def order(self, *conditions):
        self._order.extend(conditions)
        return self

    def limit(self, offset, limit=None):
        if limit is None:
            self._limit = f" {offset}"
        else:
            self._limit = f" {offset}, {limit}"
        return self

    def where(self, condition):
        if isinstance(condition, str):
            self._where = condition
        else:
            self._where = " AND ".join(condition)
        return self

    def and_(self, condition):
        if isinstance(condition, str):
            self._where += f" AND {condition}"
        else:
            self._where += f" AND {' AND '.join(condition)}"
        return self

    def or_(self, condition):
        if isinstance(condition, str):
            self._where += f" OR {condition}"
        else:
            self._where += f" OR {' OR '.join(condition)}"
        return self
