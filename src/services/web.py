from app import *
from models import Photos,PhotoThumbnails,Photo_Status

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
