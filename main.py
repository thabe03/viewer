from flask import Flask, render_template, request, redirect, url_for
import visitors

app = Flask(__name__)

@app.route('/')
def index():
    visitors.insert_ip_addr(request.remote_addr) #void
    count = visitors.get_visitor_count() #int
    return render_template('viewer.html', count=count)

if __name__ == '__main__':
    visitors.init_db()
    app.run(host='0.0.0.0', port=81)

# sqlite3 mydatabase.db "select * from visitors;"
