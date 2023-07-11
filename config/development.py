import os
# import boto3

# Configurate root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Create instance
# client = boto3.client('s3')
#
# # Read RDS credential from S3
# rds_credential = (client.get_object(
#     Bucket="aipscm-lambda-rds-credential",
#     Key="rds-combined-ca-bundle.pem")
# )['Body'].read().decode('utf-8')

config = {
    "name": "development",
    "ROOT": BASE_DIR,
    "DB": {
            "mysql": {
                "db_host": "localhost",
                "db_database": "market_analysis",
                "db_port": "3306",
                "db_user": "ma_user01",
                "db_password": "kk5dd0ss2",
                # "db_sslmode": "require",
                # "db_sslrootcert": rds_credential
            }
    },
    "S3": {
        "s3_bucket_name": "aipscm-simulation",
        "aws_access_key_id": "AKIA5PADIN7NAE7BKNSK",
        "aws_secret_access_key": "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",
    },
    "REDIS": {
        "redis_host": "xxxx",
        "redis_port": "xxxx",
        "redis_ssl": True,
        "redis_token": None,
    },
    "AUTH": {
        "FSC_OPEN_API": "mXwh51CbHVJpZ4ACqYwC6VKezfgfLNg1O+MibCmClldeC0NmQ97VQYE+ZbLtzseE2Pj1LUFvZCtXAdjVjSXMDw==",
        "FRX_OPEN_API": "53A86B442EC041DF94C8CE9268074D8617CF87B7",
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
