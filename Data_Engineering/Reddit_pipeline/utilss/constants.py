import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__),'../config/config.conf'))

SECRET_APP = parser.get('api_keys','reddit_secret_key')
CLIENT_ID = parser.get('api_keys','reddit_client_id')
USER_AGENT = parser.get('api_keys','reddit_user_agent')


DATABASE_HOST = parser.get('database','database_host')
DATABASE_name = parser.get('database','database_name')
DATABASE_port = parser.get('database','database_port')
DATABASE_username = parser.get('database','database_username')
DATABASE_password = parser.get('database','database_password')

AWS_ACCESS_KEY_ID = parser.get('aws', 'aws_access_key_id')
AWS_ACCESS_KEY = parser.get('aws', 'aws_secret_access_key')
AWS_REGION = parser.get('aws', 'aws_region')
AWS_BUCKET_NAME = parser.get('aws', 'aws_bucket_name')

INPUT_PATH = parser.get('file_paths','input_path')
OUTPUT_PATH: str = parser.get('file_paths','output_path')


POST_FIELDS = (
    'id',
    'title',
    'selftextscore',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)