from flask import Flask, jsonify, request,g
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # To return rows as dictionaries
    return conn

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Endpoint to handle login
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    name=data.get('name')
    email = data.get('email')
    password = data.get('pass')
    print('Received login data:', password)
    return jsonify({"message": "Login successful"}), 200


# Endpoint to handle signup
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    name=data.get('name')
    email = data.get('mail')
    password = data.get('pass')
    print('Received signup data:', password)
        
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()
    # Create SQL insert statement
    sql = '''
    INSERT INTO users (username, email, pass)
    VALUES (?, ?, ?)
    '''
    # Execute the SQL statement
    cursor.execute(sql, (name, email, password))
    # Commit the transaction
    conn.commit()
    # Close the connection
    conn.close()
    return jsonify({"message": "Signup successful"}), 200

@app.route('/api/create', methods=['POST'])
def create():
    data = request.json
    name=data.get('name')
    describtion = data.get('describtion')
    userid=1

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = '''
    INSERT INTO projects (pname, describtion,user_id)
    VALUES (?, ?, ?)
    '''
    cursor.execute(sql, (name, describtion,userid))
    conn.commit()
    conn.close()
    return jsonify({"message": "project created successfully"}), 200

@app.route('/api/createTag', methods=['POST'])
def create_tag():
    data = request.json
    name = data.get('name')
    color = data.get('color')

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = '''
    INSERT INTO tags (Tname, color)
    VALUES (?, ?)
    '''
    cursor.execute(sql, (name, color))
    conn.commit()
    conn.close()
    return jsonify({"message": "Tag created successfully"}), 200

@app.route('/api/tags', methods=['GET'])
def Show_tag():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = '''
    SELECT id, Tname, color FROM tags
    '''
    cursor.execute(sql)
    tags = cursor.fetchall()
    conn.close()
    tags_list = []
    for tag in tags:
        tags_list.append({
            "id": tag[0],
            "name": tag[1],
            "color": tag[2]
        })

    return jsonify(tags_list), 200
    
@app.route('/api/getprojects', methods=['GET'])
def Show_proj():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = '''
    SELECT id, pname, describtion FROM projects
    '''
    cursor.execute(sql)
    pros = cursor.fetchall()
    conn.close()
    pros_list = []
    for pro in pros:
        pros_list.append({
            "id": pro[0],
            "name": pro[1],
            "describtion": pro[2]
        })

    return jsonify(pros_list), 200

if __name__ == '__main__':
    app.run(debug=True)
