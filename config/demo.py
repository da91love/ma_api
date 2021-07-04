import os
import boto3

# Configurate root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create instance
client = boto3.client('s3')

# Read RDS credential from S3
rds_credential = (client.get_object(
    Bucket="aipscm-lambda-rds-credential",
    Key="rds-combined-ca-bundle.pem")
)['Body'].read().decode('utf-8')

config = {
    "name": "production",
    "ROOT": BASE_DIR,
    "DB": {
            "postgre": {
                "db_host": "aipscm-demo-console-tokyo-private-postgre.cwg6zfzmj18q.ap-northeast-1.rds.amazonaws.com",
                "db_database": "aipscm",
                "db_port": "5432",
                "db_user": "core_engine_user",
                "db_password": "core_engine_user",
                "db_sslmode": "require",
                "db_sslrootcert": rds_credential
            }
    },
    "S3": {
        "s3_bucket_name": "aipscm-dev-demo-simulation",
        "aws_access_key_id": "AKIA5PADIN7NAE7BKNSK",
        "aws_secret_access_key": "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",
    },
    "REDIS": {
        "redis_host": "xxxx",
        "redis_port": "xxxx",
        "redis_ssl": True,
        "redis_token": None,
    },
    "LOCK_TIME_LIMIT": 15,
    "LOG_CONFIG": {
        'version': 1,
        'formatters': {
            'general': {
                'format': "[%(asctime)s %(levelname)8s] %(filename)s %(funcName)s at line %(lineno)s - %(message)s"
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'general',
                'level': 'INFO',
            },
        },
        'root': {
            'handlers': ('console',),
            'level': 'INFO'
        }
    },
}
