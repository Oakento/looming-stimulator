import os
import sys
import sqlite3


def resource_path(db_file):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, db_file)


def execute(sql, params):
    resource = resource_path("config.db")
    with sqlite3.connect(resource) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        try:
            result = cursor.execute(sql, params)
            conn.commit()
        except Exception as e:
            raise e
        return result




def get_config_by_config_id(config_id=1):
    sql = "SELECT * FROM config WHERE config_id = ?"
    params = (config_id,)
    result = execute(sql, params).fetchone()
    return dict(result) if result else None


def update_config_by_config_id(min_degree, max_degree, chamber_height, time_expand, time_hold, time_pause, repeat, config_id=1):
    sql = '''UPDATE config 
             SET min_degree = ?, max_degree = ?, chamber_height = ?, time_expand = ?, time_hold = ?, time_pause = ?, repeat = ? 
             WHERE config_id = ?
          '''
    params = (min_degree, max_degree, chamber_height, time_expand, time_hold, time_pause, repeat, config_id)
    execute(sql, params)
