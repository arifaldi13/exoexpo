import pandas as pd
import psycopg2

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

def load_data_to_db(csv_name="exoplanets.csv"):
    df = pd.read_csv(csv_name)
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO exoplanets (
                planet_name, host_name, discovery_method, orbit_semi_major_axis,
                planet_radius, planet_mass, eccentricity, stellar_mass, distance, v_magnitude
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['planet_name'],
            row['host_name'],
            row['discovery_method'],
            row['orbit_semi_major_axis'],
            row['planet_radius'],
            row['planet_mass'],
            row['eccentricity'],
            row['stellar_mass'],
            row['distance'],
            row['v_magnitude']
        ))
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Data loaded successfully")


if __name__ == "__main__":
    load_data_to_db()