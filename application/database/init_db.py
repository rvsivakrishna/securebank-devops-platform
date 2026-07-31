import os
import sys
import time
import pymysql
import bcrypt

DB_HOST = os.getenv("DB_HOST", "mysql-service")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("DB_NAME", "bankdb")
DB_USER = os.getenv("DB_USER", "bankuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "Bank@123")

conn = None

for i in range(60):
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            autocommit=True
        )

        print("✅ Connected to MySQL")
        break

    except Exception as e:
        print(f"[{i+1}/60] Waiting for MySQL: {e}")
        time.sleep(2)

if conn is None:
    print("❌ Could not connect to MySQL")
    sys.exit(1)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE,
    password VARCHAR(255)
)
""")

cursor.execute("SELECT COUNT(*) FROM users WHERE username=%s", ("admin",))

exists = cursor.fetchone()[0]

if exists == 0:
    password_hash = bcrypt.hashpw(
        b"Admin@123",
        bcrypt.gensalt()
    ).decode()

    cursor.execute(
        "INSERT INTO users(username,password) VALUES(%s,%s)",
        ("admin", password_hash)
    )

print("✅ Database initialized successfully")

conn.close()
