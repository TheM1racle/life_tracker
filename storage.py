import sqlite3
from core import Day
from datetime import date

DB_NAME = "storage_life.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

class Storage:
    def __init__(self):
        self._create_table_if_not_exists()
    
    def _create_table_if_not_exists(self):
        with get_db_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS days (
                    date TEXT PRIMARY KEY,
                    d3 INTEGER,
                    magnesium INTEGER,
                    creatine INTEGER,
                    omega3 INTEGER,
                    nofap INTEGER,
                    hours REAL CHECK(hours >= 0 AND hours <= 24),
                    streak INTEGER DEFAULT 0)
                """)
            conn.execute("CREATE INDEX IF NOT EXISTS idx_date ON days(date)")
    
    def save_day(self, day_obj):
        with get_db_connection() as conn:
            conn.execute("""
                INSERT INTO days VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(date) DO UPDATE SET
                    d3=excluded.d3,
                    magnesium=excluded.magnesium,
                    creatine=excluded.creatine,
                    omega3=excluded.omega3,
                    nofap=excluded.nofap,
                    hours=excluded.hours,
                    streak=excluded.streak
                """, (day_obj.date,
                        day_obj.d3,
                        day_obj.magnesium,
                        day_obj.creatine,
                        day_obj.omega3,
                        day_obj.nofap,
                        day_obj.hours,
                        day_obj.streak
                        ))
            conn.commit()
    
    def get_last_day_data(self):
        with get_db_connection() as conn:
            cursor = conn.execute("""
                SELECT * FROM days
                ORDER BY date DESC
                LIMIT 1
            """)
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def get_all_history(self):
        all_days = []
        with get_db_connection() as conn:
            cursor = conn.execute("""
                SELECT * FROM days
                ORDER BY date ASC
            """)
            for row in cursor:
                day_obj = Day(
                    date=row['date'],
                    d3=row['d3'],
                    magnesium=row['magnesium'],
                    creatine=row['creatine'],
                    omega3=row['omega3'],
                    nofap=row['nofap'],
                    hours=row['hours'],
                    streak=row['streak']
                )
                all_days.append(day_obj)
        return all_days



