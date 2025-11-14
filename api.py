from flask import Flask, jsonify
from flask_cors import CORS
import json

# Create the Flask app
app = Flask(__name__)
CORS(app)  # Allow frontend to access this API

# Load the JSON data files
def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

pets = load_json('pets.json')
shelters = load_json('shelters.json')
adoptions = load_json('adoptions.json')

# HOME ROUTE - Just to check if API is working
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Pet Adoption Platform API",
        "endpoints": [
            "/api/pets - Get all pets",
            "/api/pets/<id> - Get one pet",
            "/api/shelters - Get all shelters",
            "/api/adoptions - Get all adoptions"
        ]
    })

# GET ALL PETS
@app.route('/api/pets', methods=['GET'])
def get_all_pets():
    return jsonify(pets)

# GET ONE PET BY ID
@app.route('/api/pets/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    pet = next((p for p in pets if p['id'] == pet_id), None)
    if pet:
        return jsonify(pet)
    else:
        return jsonify({"error": "Pet not found"}), 404

# GET ALL SHELTERS
@app.route('/api/shelters', methods=['GET'])
def get_all_shelters():
    return jsonify(shelters)

# GET ONE SHELTER BY ID
@app.route('/api/shelters/<int:shelter_id>', methods=['GET'])
def get_shelter(shelter_id):
    shelter = next((s for s in shelters if s['id'] == shelter_id), None)
    if shelter:
        return jsonify(shelter)
    else:
        return jsonify({"error": "Shelter not found"}), 404

# GET ALL ADOPTIONS
@app.route('/api/adoptions', methods=['GET'])
def get_all_adoptions():
    return jsonify(adoptions)

# FILTER PETS BY SPECIES (dogs or cats)
@app.route('/api/pets/species/<species>', methods=['GET'])
def get_pets_by_species(species):
    filtered = [p for p in pets if p['species'].lower() == species.lower()]
    return jsonify(filtered)

# FILTER PETS BY STATUS (Available, Adopted, Pending)
@app.route('/api/pets/status/<status>', methods=['GET'])
def get_pets_by_status(status):
    filtered = [p for p in pets if p['status'].lower() == status.lower()]
    return jsonify(filtered)

# Run the API
if __name__ == '__main__':
    print("🚀 API is starting...")
    print("📍 Go to: http://localhost:5000")
    print("📍 Try: http://localhost:5000/api/pets")
    app.run(debug=True, port=5000)