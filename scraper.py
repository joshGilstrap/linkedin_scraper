from bs4 import BeautifulSoup
import requests
import pandas as pd

# Uncomment for deployment
next_url = input("LinkedIn URL: ")
response = requests.get(next_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Uncomment for offline testing
# Offline testing to prevent call spamming
# with open('linkedin_python_search.html', "rb") as html_file:
#     soup = BeautifulSoup(html_file, 'html.parser')

# Find every a tag with an href attribute that contains a job posting
tags = soup.find_all('a')
links = []
job_links = []
job_labels = []
for tag in tags:
    links.append(tag.get('href'))
    if tag.get('href') and tag.get('href').startswith('https://www.linkedin.com/jobs/view/'):
        job_links.append(tag.get('href'))
        job_labels.append(tag.text.strip())

# Make multi-column pandas database from links and labels and export to excel
df = pd.DataFrame({'Job Title': job_labels, 'Job Link': job_links})
print(df)
df.to_csv('linkedin_python_search.csv', index=False)
df.to_excel('python_jobs.xlsx', index=False)
