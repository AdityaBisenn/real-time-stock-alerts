from app.core.db import get_db
from app.core.logger import logger

def get_target_list():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT DISTINCT stock_symbol FROM stock_alerts WHERE is_active = 1"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return [row[0] for row in result]