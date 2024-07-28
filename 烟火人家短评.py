import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15'
}

total_comments = 2656
comments_per_page = 20
total_pages = (total_comments + comments_per_page - 1) // comments_per_page

with open('all_comments3.txt', 'w', encoding='utf-8') as file:
    for page in range(total_pages):
        start = page * comments_per_page
        url = f'https://movie.douban.com/subject/35370850/comments?start={start}&limit=20&status=P&sort=new_score'
        
        response = requests.get(url, headers=headers)
        
        if response.ok:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            pingluns = soup.findAll('span', attrs={'class': 'short'})
            
            for pinglun in pingluns:
                content = pinglun.get_text(strip=True)
                content = re.sub(r'\s+', '', content)
                file.write(content + '\n')

        else:
            print(f'请求失败：{url}')

print('处理完成，已保存到 all_comments3.txt')
