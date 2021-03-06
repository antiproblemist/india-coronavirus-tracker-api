from requests_html import HTML
import re, requests, datetime
from bs4 import BeautifulSoup
from .get_helpline_numbers import helpline_numbers

def get_data():
    r = requests.get('https://www.mohfw.gov.in')

    page = BeautifulSoup(r.text, 'html5lib')
    page = HTML(html=str(page))

    thead = page.xpath("//div[@id='cases']/div/div/table/thead/tr/th/strong")
    default_headings = ["S. No.","Name of State / UT","Total Confirmed cases *","Cured/Discharged/Migrated","Death"]
    found_headings = [element.text.replace("\n", "") for element in thead]

    data = {}

    table_rows = page.xpath("//div[@id='cases']/div/div/table/tbody/tr")

    for row in table_rows:
        data_item = {}
        try:
            columns = row.xpath("//td/text()")
            state = columns[found_headings.index(default_headings[1])].replace("\n", "")
          
            if not state:
                continue

            helpline_states = helpline_numbers()

            data_item['helpline'] = helpline_states[state] if state in helpline_states else ""
            data_item['total_confirmed_cases'] = columns[found_headings.index(default_headings[2])]
            data_item['cured_or_discharged_or_migrated'] = columns[found_headings.index(default_headings[3])]
            data_item['death'] = columns[found_headings.index(default_headings[4])]
        except Exception as e:
            print(e)
            continue

        data[state] = data_item
    data['fetched'] = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    return data