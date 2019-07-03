import requests
from celery import Celery
from PIL import Image
from io import BytesIO
from app import *
from models.models import Photos,PhotoThumbnails

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

queueHandler = Celery("web", broker="http://rabbitmq:1234@localhost:15672")

@queueHandler.task
def resizePhoto(photo, size):
  try:
    response = requests.get(photo.url, verify=False, timeout=30)
    img = Image.open(BytesIO(response.content))
    img.thumbnail(size)
    img.save("/app/waldo-app-thumbs/"+str(photo.uuid)+".JPEG")
    thumbnail = PhotoThumbnails(photo_uuid=photo.uuid, width=size[0], height=size[1], url="/app/waldo-app-thumbs/"+str(photo.uuid)+".JPEG" )
    db.session.add(thumbnail)
    Photos.query.filter_by(uuid=photo.uuid).update(dict(status='completed'))
    db.session.commit()

  except:
    Photos.query.filter_by(uuid=photo.uuid).update(dict(status='failed'))
    db.session.commit()
    

