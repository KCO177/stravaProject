import urllib.request
from datetime import datetime, timedelta
from html_table_parser.parser import HTMLTableParser


class WebScraper:
    def url_get_contents(self, url):
        req = urllib.request.Request(url=url)
        f = urllib.request.urlopen(req)
        return f.read()

    def getFuelPrice(self, date_to_find):
        xhtml = self.url_get_contents('https://www.kurzy.cz/komodity/benzin-nafta-cena/').decode('utf-8')
        p = HTMLTableParser()
        p.feed(xhtml)
        result_list = []
        for sublist in p.tables:
            if sublist and sublist[0][0] == 'Datum':  # Check if the first element of the sublist is 'Datum'
                for entry in sublist[1:]:
                    date = entry[0]
                    benzine_price = entry[1]
                    nafta_price = entry[3]
                    result_list.append([date, benzine_price, nafta_price])

        result = [sublist for sublist in result_list if sublist[0] == date_to_find]
        result = result[0] if result else None

        return result

    def getFormatedDate(self):
        current_date = datetime.now()
        one_day_ago = current_date - timedelta(days=1)
        formatted_date = one_day_ago.strftime('%d.%m.%Y')
        return formatted_date
