from flask import Flask, jsonify, render_template, send_file

# NOTE: Create a new Flask app
app = Flask(__name__)

# NOTE: Define the routes

# NOTE: The index route returns the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# NOTE: The api route returns a JSON response with a message
@app.route('/api')
def api():
    data = {'message': 'Hello, API!'}
    return jsonify(data)


# NOTE: The download route returns a file to be downloaded
@app.route('/download')
def download_file():
    file_path = 'download_simple.txt'

    # NOTE: Using the native Flask send_file function to send the file
    return send_file(file_path, mimetype='text/plain', as_attachment=True, download_name='download_simple.txt')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)