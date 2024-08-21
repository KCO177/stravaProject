from datetime import datetime
from webApi.authorization.Token import Token
from webApi.dataFetcher.WebScraper import WebScraper


class PriceHandler:
    def date_diff(self, date_str1, date_str2):
        date_format = '%d.%m.%Y'
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        delta = date1 - date2
        return delta.days

    def fetchPrices(self):
        db = Token()
        conn, cur = db.connect_db()
        if conn is None or cur is None:
            print("Failed to connect to the database.")
            return None

        try:
            cur.execute("SELECT * FROM fuel_price ORDER BY id DESC LIMIT 1")
            result = cur.fetchone()  # Fetch the single last row
            return result

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

        finally:
            cur.close()
            conn.close()

    def setPrices(self, date, benzin, nafta):
        db = Token()
        conn, cur = db.connect_db()
        if conn is None or cur is None:
            print("Failed to connect to the database.")
            return
        try:
            cur.execute(f'''INSERT INTO fuel_price (date, benzin, nafta) VALUES (%s, %s, %s)''', (date, benzin, nafta))
            print(f"inserted price values for date {date}")
            conn.commit()
        except Exception as e:
            print('Error:', e)

        finally:
            cur.close()
            conn.close()

    # Example usage
    def getValidPrices(self):
        scraper = WebScraper()
        prices = self.fetchPrices()

        if prices:
            date1 = scraper.getFormatedDate()
            date2 = prices[1]
            day_delta = self.date_diff(date1, date2)
            if day_delta < 7:
                return prices  # Assuming you want to return or use the prices
            else:
                new_values = scraper.getFuelPrice(date1)
                if new_values:
                    self.setPrices(new_values[0], new_values[1], new_values[2])
                    return new_values
        else:
            print("No prices found.")
