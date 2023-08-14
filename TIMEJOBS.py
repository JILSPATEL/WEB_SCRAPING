print("put some skill that you are not familiar with")
print("NOTE:enter word in small case")
unfamiliar_skill=input('>')
print(f'filtering out {unfamiliar_skill}')
#def find_jobs():
html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
#print(html_text)
soup = BeautifulSoup(html_text,'lxml')
jobs1=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
#print(jobs)
for index,jobs in enumerate(jobs1):
    job_pub = jobs.find('span', class_='sim-posted').span.text
    if 'few days ago' in job_pub:
        company_name=jobs.find('h3',class_='joblist-comp-name').text.replace(' ','')
        skills=jobs.find('span',class_='srp-skills').text.replace(' ','').lower()
        more_info=jobs.header.h2.a['href']
        if unfamiliar_skill not in skills:
            with open(f'posts/{index}.txt','w') as f:
                f.write(f"company name : {company_name.strip()} \n")
                f.write(f"Required skills : {skills.strip()} \n")
                f.write(f"More INFO : {more_info} \n")
            print(f'file saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        # time_wait=1
        # print(f"waiting {time_wait} minutes....")
        #time.sleep(time_wait*60)
