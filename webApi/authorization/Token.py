import datetime
import psycopg2
import os

from webApi.authorization.Authorization import Authorization


class Token:
    def fetch_access_token(self, clientId):
        token = self.fetch_data(clientId, "short_lived_access_token", "access_token")
        if None or self.is_expired(clientId):
            print('authorization token invalid or missing, start authorization process')
            newToken = self.set_access_token(clientId)
            return newToken
        else:
            return token

    def set_access_token(self, clientId):
        authorization_instance = Authorization()
        token, expiration_timestamp = authorization_instance.getAccessToken(clientId)
        self.insert_data(clientId, "short_lived_access_token", "access_token", token)
        self.insert_data(clientId, "short_lived_access_token", "expiration", expiration_timestamp)
        return token
    def connect_db(self):
        try:
            conn = self._create_connection()
            cur = conn.cursor()
            return conn, cur
        except (Exception, psycopg2.DatabaseError) as error:
            print('Error while connecting to PostgreSQL:', error)
            return None, None

    def _create_connection(self):
        return psycopg2.connect(
            database='strava_App_Db',
            user=self._get_credentials("PSGS_USER"),
            password=self._get_credentials("PSGS_PASS"),
            host='localhost',
            port='5432'
        )

    def _get_credentials(self, credential_type: str):
        return os.getenv(credential_type)

    def fetch_data(self, client_id, table, name):
        conn, cur = self.connect_db()
        if conn is None or cur is None:
            print("Failed to connect to the database.")
            return None

        try:
            cur.execute(f"SELECT value FROM {table} WHERE client_id = %s AND name = %s", (client_id, name))
            data = cur.fetchall()

            if data:
                return data[0][0]
            else:
                return None

        except (Exception, psycopg2.DatabaseError) as e:
            print('Error:', e)
            return None
        finally:
            cur.close()
            conn.close()

    def insert_data(self, client_id, table, name, value):
        conn, cur = self.connect_db()
        if conn is None or cur is None:
            print("Failed to connect to the database.")
            return

        try:
            cur.execute(f'''
                INSERT INTO {table} (client_id, name, value)
                VALUES (%s, %s, %s)
                ON CONFLICT (client_id, name)
                DO UPDATE SET value = EXCLUDED.value
            ''', (client_id, name, value))
            print(f"Upserted {name} in {table} for {client_id}")

            conn.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            cur.close()
            conn.close()

    def is_expired(self, clientId):
        #True is it is expired
        expiration_date_from_db = self.fetch_data(clientId, "short_lived_acces_token", "expire_at")
        if expiration_date_from_db == None: pass #TODO call authorization
        else:
            expiration_date = self.convert_unix_timestamp(expiration_date_from_db)
            expiration_timestamp = self.convert_unix_timestamp(expiration_date)
            current_timestamp = int(datetime.datetime.now().timestamp())
            return current_timestamp > expiration_timestamp

    def convert_unix_timestamp(self, timestamp):
        dt = datetime.datetime.fromtimestamp(timestamp)
        return dt.strftime('%Y-%m-%d %H:%M:%S')
