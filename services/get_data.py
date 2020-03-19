from requests_html import HTML
import re, requests, datetime
from bs4 import BeautifulSoup
from .get_helpline_numbers import helpline_numbers

def get_data():
    r = requests.get('https://www.mohfw.gov.in')

    page = BeautifulSoup(r.text, 'html5lib')
    page = HTML(html=str(page))

    alternate_name = {"Telengana": "Telangana", "Pondicherry": "Puducherry"}
    thead = page.xpath('//thead/tr/th/strong')
    default_headings = ['S. No.', 'Name of State / UT', 'Total Confirmed cases (Indian National)', 'Total Confirmed cases ( Foreign National )', 'Cured/Discharged/Migrated', 'Death']
    found_headings = [element.text.replace("\n", "") for element in thead]

    data = {}

    table_rows = page.xpath('//table/tbody/tr')

    for row in table_rows:
        data_item = {}
        try:
            columns = row.xpath("//td/text()")
            
            state = columns[found_headings.index(default_headings[1])].replace("\n", "")
            
            if state in alternate_name:
                state = alternate_name[state]
            
            if not state:
                continue

            helpline_states = helpline_numbers()

            data_item['helpline'] = helpline_states[state] if state in helpline_states else ""
            data_item['total_confirmed_cases_indian_national'] = columns[found_headings.index(default_headings[2])]
            data_item['total_confirmed_cases_foreign_national'] = columns[found_headings.index(default_headings[3])]
            data_item['cured_or_discharged'] = columns[found_headings.index(default_headings[4])]
            data_item['death'] = columns[found_headings.index(default_headings[5])]
        except Exception as e:
            print(e)
            continue

        data[state] = data_item
    data['fetched'] = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    return data