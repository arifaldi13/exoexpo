from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route('/planets', methods=['GET'])
def get_planets():
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    SELECT
        planet_name,
        host_name,
        discovery_method,
        orbit_semi_major_axis,
        planet_radius,
        planet_mass,
        eccentricity,
        stellar_mass,
        distance,
        v_magnitude
    FROM exoplanets;
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    planets = []
    for row in rows:
        planets.append({
            'planet_name': row[0],
            'host_name': row[1],
            'discovery_method': row[2],
            'orbit_semi_major_axis': row[3],
            'planet_radius': row[4],
            'planet_mass': row[5],
            'eccentricity': row[6],
            'stellar_mass': row[7],
            'distance': row[8],
            'v_magnitude': row[9]
        })

    cursor.close()
    conn.close()

    return jsonify(planets)

if __name__ == '__main__':
    app.run(debug=True)
