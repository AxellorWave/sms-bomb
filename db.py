import mysql.connector
from mysql.connector import Error
import os

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'db'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME', 'bomb_db'),
    'connection_timeout': 10
}

def get_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f"Ошибка подключения к БД: {e}")
        return None

def put(message, level, mes_id, data=''):
    if isinstance(message, str):
        chat_id = message
    else:
        chat_id = message.chat.id

    conn = get_connection()
    if not conn:
        return False

    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO user_state (chat_id, level, data, mes_id, updated_at) 
            VALUES (%s, %s, %s, %s, NOW())
            ON DUPLICATE KEY UPDATE 
                level = VALUES(level),
                data = VALUES(data),
                mes_id = VALUES(mes_id),
                updated_at = NOW()
        """
        values = (str(chat_id), level, data, str(mes_id))
        
        cursor.execute(query, values)
        conn.commit()
        return True
    except Error as e:
        print(f"Ошибка при записи в БД: {e}")
        conn.rollback()
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def give(message):
    chat_id = message.chat.id
    conn = get_connection()
    
    if not conn:
        return None, None, None

    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT level, data, mes_id FROM user_state WHERE chat_id = %s"
        cursor.execute(query, (str(chat_id),))
        
        result = cursor.fetchone()
        
        if result:
            return result['level'], result['data'], result['mes_id']
        else:
            return None, None, None
    except Error as e:
        print(f"Ошибка при чтении из БД: {e}")
        return None, None, None
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()