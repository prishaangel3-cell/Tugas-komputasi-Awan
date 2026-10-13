import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer

# Inisialisasi Database SQLite
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT)')
    cursor.execute('INSERT INTO logs (message) VALUES ("App connected to SQLite Database successfully!")')
    conn.commit()
    conn.close()

init_db()

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT message FROM logs ORDER BY id DESC LIMIT 1')
        db_message = cursor.fetchone()[0]
        conn.close()

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response_html = f"<h1>Halo dari Jenkins CI/CD!</h1><p><b>Status Database:</b> {db_message}</p>"
        self.wfile.write(response_html.encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), SimpleHandler)
    print("Server running on port 8000...")
    server.serve_forever()
