"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        male_count = 0
        female_count = 0
        data = []
        tags = soup.find_all('tbody', {'tr': ''})
        for tag in tags:
            data = tag.text
            data = data.split()
        for i in range(1000):
            if i % 5 == 2:
                number = ''
                for s in data[i]:
                    if s != ',':
                        number += s
                male_count += int(number)
            if i % 5 == 4:
                number = ''
                for s in data[i]:
                    if s != ',':
                        number += s
                female_count += int(number)
        print(f"Male number: {male_count}")
        print(f"Female number: {female_count}")


if __name__ == '__main__':
    main()
