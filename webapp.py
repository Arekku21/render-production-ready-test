from flask import Flask, jsonify, render_template, send_file,request
from ftplib import FTP
import os

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


# NOTE: The donwloaded route returns a file to be downloaded
@app.route('/ftp/download', methods=['POST'])
def ftp_download():

    #NOTE: Here are using the FTPlib to connect to the FTP server and download the file

    ftp_host = 'ftp.dlptest.com'
    ftp_user = 'dlpuser'
    ftp_password = 'rNrKYTX9g7z3RgJRmxWuGHbeu'
    ftp_directory = ''
    
    #NOTE: using the request.form.get to get the filename from the form data
    file_name = request.form.get('filename')

    # NOTE: Here are using the FTPlib to connect to the FTP server with credentials above

    # Create an FTP object and connect to the server
    ftp = FTP(ftp_host)

    # Login to the server with user and password
    ftp.login(user=ftp_user, passwd=ftp_password)

    # Change the directory to the FTP directory
    ftp.cwd(ftp_directory)

    
    local_file_path = os.path.join('', file_name)
    with open(local_file_path, 'wb') as local_file:
        ftp.retrbinary('RETR ' + file_name, local_file.write)

    ftp.quit()
    return f'File "{file_name}" downloaded to "{local_file_path}"'


# NOTE: The upload route returns a file to be uploaded
@app.route('/ftp/upload', methods=['POST'])
def ftp_upload():

    #NOTE: Here are using the FTPlib to connect to the FTP server and download the file

    ftp_host = 'ftp.dlptest.com'
    ftp_user = 'dlpuser'
    ftp_password = 'rNrKYTX9g7z3RgJRmxWuGHbeu'
    ftp_directory = ''

    file = request.files['file']
    file_name = file.filename

    ftp = FTP(ftp_host)
    ftp.login(user=ftp_user, passwd=ftp_password)
    ftp.cwd(ftp_directory)

    with open(file_name, 'rb') as local_file:
        ftp.storbinary('STOR ' + file_name, local_file)

    ftp.quit()
    return f'File "{file_name}" uploaded to FTP server'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)