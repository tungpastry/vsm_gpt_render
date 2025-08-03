from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

# Route mặc định để tránh lỗi 404
@app.route("/")
def index():
    return "✅ VSM GPT API is running", 200

@app.route("/query", methods=["POST"])
def handle_query():
    data = request.get_json()
    sql = data.get("query")

    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        cursor.close()
        conn.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
