from bs4 import BeautifulSoup
from urllib.request import urlopen
import 

response = urlopen('https://dataplatform.cloud.ibm.com/ml/auto-ml/f8411ff7-1c0f-45c0-894d-983a52b4c8be/visualize?projectid=1ff793c1-197b-4739-aa96-4eefc3f6b232&mlInstanceGuid=962d4e59-b1b1-4868-bef0-15a6b1cf1b70&attachment_id=d2296a76-b1bf-42f4-b2d8-043b97b670ee&pipeline_key=P4&context=analytics')
soup = BeautifulSoup(response, 'html.parser')
i = 1
link = browser.find('a')[0]
browser.follow_link(link)
