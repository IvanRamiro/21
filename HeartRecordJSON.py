from flask import Flask, jsonify, request

app = Flask(__name__)

heart_rate_data = []

@app.route('/heart_rate', methods=['POST'])
def insert_heart_rate():
    heart_rate_data = request.get_json()
    heart_id = heart_rate_data['heart_id']
    date = heart_rate_data['date']
    heart_rate = heart_rate_data['heart_rate']

    for record in heart_rate_data:
        if record['heart_id'] == heart_id:
            return jsonify({'message': 'Heart rate record with the same ID already exists'})

    heart_rate_data.append({
        'heart_id': heart_id,
        'date': date,
        'heart_rate': heart_rate
    })

    return jsonify({'message': 'Heart rate record inserted successfully'})


@app.route('/heart_rate', methods=['GET'])
def get_all_heart_rates():
    return jsonify(heart_rate_data)


@app.route('/heart_rate/<heart_id>', methods=['GET'])
def get_heart_rate_by_id(heart_id):
    heart_rate_record = None
    for record in heart_rate_data:
        if record['heart_id'] == heart_id:
            heart_rate_record = record
            break

    if heart_rate_record:
        return jsonify(heart_rate_record)
    else:
        return jsonify({'message': 'Heart rate record not found'})


@app.route('/heart_rate/<heart_id>', methods=['PUT'])
def update_heart_rate(heart_id):
    heart_rate_data = request.get_json()
    date = heart_rate_data['date']
    heart_rate = heart_rate_data['heart_rate']

    modified = False
    for index, record in enumerate(heart_rate_data):
        if record['heart_id'] == heart_id:
            record['date'] = date
            record['heart_rate'] = heart_rate
            modified = True
            break

    if modified:
        return jsonify({'message': 'Heart rate record updated successfully'})
    else:
        return jsonify({'message': 'Heart rate record not found'})


@app.route('/heart_rate/<heart_id>', methods=['DELETE'])
def delete_heart_rate(heart_id):
    deleted = False
    for index, record in enumerate(heart_rate_data):
        if record['heart_id'] == heart_id:
            heart_rate_data.pop(index)
            deleted = True
            break

    if deleted:
        return jsonify({'message': 'Heart rate record deleted successfully'})
    else:
        return jsonify({'message': 'Heart rate record not found'})


if __name__ == '__main__':
    app.run(debug=True)
