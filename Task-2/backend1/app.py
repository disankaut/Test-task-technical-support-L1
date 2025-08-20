from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Запись из Backend1!</h1>"

@app.route('/api/data')
@app.route('/api/data/')
def data():
    try:
        conn = mysql.connector.connect(
            host="mariadb",
            user="user",
            password="userpassword",
            database="app_db"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        conn.close()
        return {"status": "connected", "database": db_name[0]}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
