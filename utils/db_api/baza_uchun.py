import sqlite3

class Database:
    def __init__(self, baza_manzili):
        self.path_to_db = baza_manzili

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)
    def execute(self, sql: str, parameters: tuple = None, fetchone=False, commit=False, fetchall=None):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data
    def create_table_users(self):
        sql = """
        CREATE TABLE myfiles_teacher (
            id int NOT NULL,
            NAME varchar(255) NOT NULL,
            email varchar(255),
            language varchar(3),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)
    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email:str = None, language: str = 'uz'):
        sql = """
        INSERT INTO myfiles_teacher(id, Name, email, ) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM myfiles_teacher
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM users;", commit=True)

    def delete_user(self):
        self.execute("DELETE FROM users WHERE TRUE", commit=True)

    def user_qoshish(self,  ism: str, tg_id: int, fam: str = None, username: str=None):
        sql = """
               INSERT INTO users(ism, fam, username, tg_id) VALUES(?, ?, ?, ?)
               """
        self.execute(sql, parameters=(ism, fam, username, tg_id), commit=True)

    def user_sanash(self):
        return self.execute("SELECT COUNT(*) FROM users;", fetchone=True)

    def barcha_foydalanuvchilarni_tanlash(self):
        sql = """
        SELECT * FROM users
        """
        return self.execute(sql, fetchall=True)
    def select_all_menu(self):
        sql = """
        SELECT * FROM menu
        """
        return self.execute(sql, fetchall=True)


    def select_taom(self, **kwargs):
        sql = "SELECT * FROM taom_mahsulotlar WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)
    def select_pitsa(self, **kwargs):
        sql = "SELECT * FROM pitsa_mahsulotlar WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)
    def select_nonushta(self, **kwargs):
        sql = "SELECT * FROM nonushta_uchun WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)
    def select_maxsulotlar(self, **kwargs):
        sql = "SELECT * FROM maxsulotlar WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)
    def select_bolalar(self, **kwargs):
        sql = "SELECT * FROM bolalar_uchun WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)
    def select_ichimliklar(self, **kwargs):
        sql = "SELECT * FROM ichimliklar WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)

def logger(statement):
    print(f"""
    __________________________________________________________
    Executing:
    {statement}
    __________________________________________________________
""")
# user sanovchi baza


