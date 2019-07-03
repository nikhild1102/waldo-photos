from app import *
from photoProcessor import resizePhoto
from models import Photos,PhotoThumbnails,Photo_Status
from sqlalchemy import and_

size = 320, 320


@app.route("/")
def index():
  return jsonify(success=True)


@app.route("/photos/pending")
def pendingPhotos():
  snapshot = Photos.query.filter_by(status='pending')
  pendingRecords = []

  if snapshot:
    for p in snapshot:
      pendingRecords.append({
        'uuid':p.uuid,
        'url':p.url,
        'status': p.status.value,
        })
    return jsonify({'data':pendingRecords})
  else:
    return jsonify({'data':[],'message':'No pending records found'})


@app.route("/photos/process", methods=["POST", "GET"])
def processPhotos():
  data = request.get_json()
  uuids = data['uuids']
  photoObjects = Photos.query.filter((Photos.uuid.in_(uuids)) & ((Photos.status=='pending') | (Photos.status=='failed'))).all()
  for photo in photoObjects:
    Photos.query.filter_by(uuid=photo.uuid).update(dict(status='processing'))
    db.session.commit()
    resizePhoto(photo, size)
  return jsonify({'message':'Processing completed'})
