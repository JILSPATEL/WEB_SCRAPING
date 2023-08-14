html_text = requests.get("https://www.flipkart.com/mobiles/smartphones~type/pr?sid=tyy,4io").text
soup = BeautifulSoup(html_text, 'lxml')
price_tags = soup.find_all('div', class_='_30jeq3 _1_WHN1')
mo_name = soup.find_all('div', class_='_4rR01T')
offers = soup.find_all('div', class_='_2Tpdn3 _18hQoS')
off = soup.find_all('div', class_='_3Ay6Sb')

for i, price_tag in enumerate(price_tags):
    price_text = price_tag.text.strip()
    price_text = price_text.replace(',', '')
    price_text = price_text.replace('₹', '')
    price = int(price_text)

    discount_text = off[i].text.replace('% off', '').strip()
    discount_percentage = int(discount_text)

    if price > 10000 and 'Bank Offer' in offers[i].text:
        if discount_percentage>25:
         print(f"mobile : {mo_name[i].text.strip()}")
         print(f"discount given is :{discount_percentage}")
         print(f"price :{price}")
