from flask import Flask, request
from flask import send_file
from flask_cors import CORS
import logging
from psycopg2 import connect
import boto3
import yaml
import os
import uuid
from sqlalchemy import text
from flask import g
from prometheus_flask_exporter import PrometheusMetrics

from helpers.service_helpers import get_settings, generate_file_uuid, make_hash_from_cred
from modules.s3 import S3
from modules.postgres import Postgres


# initializing app instance and metrics collector
app = Flask(__name__)
metrics = PrometheusMetrics(app)
app.config['CORS_HEADERS'] = 'Content-Type'
logging.getLogger('flask_cors').level = logging.DEBUG
CORS(app)
SETTINGS = get_settings()
s3 = S3()
postgres = Postgres()


@app.before_request
def before_request():
    g.db_session = postgres.get_connection()


@app.teardown_request
def teardown_request(exception):
    db_session = g.pop('db_session', None)
    if db_session is not None:
        db_session.close()


@app.route('/get_video/1', methods=['GET'])
def get_video():
    src_path = 'src/'
    file_path = 'src/small_video.mp4'

    if not os.path.isfile(file_path):
        return {'error': 'Video file not found'}, 404

    return send_file(file_path, mimetype='video/mp4')

#--------------------------------------------------------------------------------------------------


@app.route('/reg_user', methods=['POST'])
def reg_user():
    data = request.get_json()
    pass_hash = make_hash_from_cred(data['password'])
    private_token = generate_file_uuid()
    db_session = g.db_session

    query_users = "INSERT INTO main.users (uuid) VALUES (:private_token);"
    query_users_creds = f"insert into main.user_creds (user_id, login, password) values(" \
                        f":private_token, :login, :hash_pass);"

    postgres.execute_custom_query(query_users, db_session, private_token=private_token)
    postgres.execute_custom_query(query_users_creds, db_session,
                                  private_token=private_token,
                                  login=data['login'],
                                  hash_pass=pass_hash)

    return {'status_code': 200}


@app.route('/reg_company', methods=['POST'])
def reg_company():
    data = request.get_json()
    pass_hash = make_hash_from_cred(data['password'])
    private_token = generate_file_uuid()
    db_session = g.db_session

    query_companies = "INSERT INTO main.companies (uuid) VALUES (:private_token);"
    query_companies_creds = f"insert into main.company_creds (company_id, login, password) values(" \
                            f":private_token, :login, :hash_pass);"

    postgres.execute_custom_query(query_companies, db_session, private_token=private_token)
    postgres.execute_custom_query(query_companies_creds, db_session,
                                  private_token=private_token,
                                  login=data['login'],
                                  hash_pass=pass_hash)

    return {'status_code': 200}

@app.route('/reg_sub_company_user', methods=['POST'])
def reg_sub_company_user():
    pass


@app.route('/company_auth', methods=['POST'])
def company_auth():
    data = request.get_json()
    pass_hash = make_hash_from_cred(data['password'])
    db_session = g.db_session

    query_auth = "SELECT * FROM main.company_creds WHERE login = :login and password = :pass_hash;"
    result = postgres.execute_custom_query(query_auth, db_session, login=data['login'], pass_hash=pass_hash).fetchone()

    if result:
        return {'status_code': 200}
    else:
        return {'status_code': 400}

@app.route('/user_auth', methods=['POST'])
def user_auth():
    data = request.get_json()
    pass_hash = make_hash_from_cred(data['password'])
    db_session = g.db_session

    query_auth = "SELECT * FROM main.user_creds WHERE login = :login and password = :pass_hash;"
    result = postgres.execute_custom_query(query_auth, db_session, login=data['login'], pass_hash=pass_hash).fetchone()

    if result:
        return {'status_code': 200}
    else:
        return {'status_code': 400}

@app.route('/show_preview_courses', methods=['GET'])
def show_preview_courses():
    pass


@app.route('/show_preview_companies', methods=['GET'])
def show_preview_companies():
    pass


@app.route('/user_courses', methods=['GET'])
def user_courses():
    pass


@app.route('/play_video', methods=['POST', 'GET'])
def play_video():
    pass


@app.route('/upload_video', methods=['POST'])
def upload_video():
    data = request.get_json()
    s3.upload_file(data['video'])
    print()


@app.route('/edit_video', methods=['POST'])
def edit_video():
    pass


@app.route('/delete_video', methods=['POST'])
def delete_video():
    pass


@app.route('/make_course', methods=['POST'])
def make_course():
    pass


@app.route('/edit_course', methods=['POST'])
def edit_course():
    pass


@app.route('/delete_course', methods=['POST'])
def delete_course():
    pass


@app.route('/view_course', methods=['GET'])
def view_course():
    pass


@app.route('/make_module', methods=['POST'])
def make_module():
    pass


@app.route('/delete_module', methods=['POST'])
def delete_module():
    pass


@app.route('/edit_module', methods=['POST'])
def edit_module():
    pass


@app.route('/view_module', methods=['GET'])
def view_module():
    pass


@app.route('/search_course', methods=['GET'])
def search_course():
    pass


@app.route('/search_video', methods=['GET'])
def search_video():
    pass


@app.route('/search_company', methods=['GET'])
def search_company():
    pass


@app.route('/show_company_page', methods=['GET'])
def show_company_page():
    pass


@app.route('/show_user_page', methods=['GET'])
def show_user_page():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
