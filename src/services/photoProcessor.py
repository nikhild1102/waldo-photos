import requests
from celery import Celery
from PIL import Image
from io import BytesIO

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

queueHandler = Celery("web", broker="http://rabbitmq:1234@localhost:15672")

@queueHandler.task
def resizePhoto(url, size):
  try:
    response = requests.get(url, verify=False, timeout=30)
    img = Image.open(BytesIO(response.content))
    img.thumbnail(size)
    return img
  except Exception as e:
    return None
