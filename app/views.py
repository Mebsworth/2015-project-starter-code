from flask import request
from flask import render_template
from app import app

@app.route('/', methods=['GET'])
def index():
    coordinates = [{ 
        'lat': 39.955688,
        'lng': -75.202209,
        'notes': 'Corner of 40th & Chestnut'
    }, { 
        'lat': 39.955536, 
        'lng': -75.198481,
        'notes': 'Sitar'
    }]
    return render_template('index.html', title="The Treasure Map", coordinates=coordinates)

@app.route('/health', methods=['GET'])
def get_health():
    return '200 OK'

@app.route('/coordinates', methods=['POST'])
def handle_coordinates():
    # store coordinates
    coordinates = list(request.args.get('coordinates'))
    for c_data in coordinates:
        # format = {'latitude': <float>, 'longitude': <float>, 'notes': <string>}
        coord = Coordinate(latitude=c_data['latitude'], longitude=c_data['longitude'], notes=c_data['notes'])
        db.session.add(coord)
    db.session.commit()
