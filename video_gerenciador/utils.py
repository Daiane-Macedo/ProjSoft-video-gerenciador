from boto.s3.connection import S3Connection, Bucket, Key

import videoGerenciador.settings as settings


def delete_from_S3(filename):
    conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
    bucket = Bucket(conn, settings.AWS_STORAGE_BUCKET_NAME)
    k = Key(bucket)
    k.key = settings.MEDIA_URL + filename
    bucket.delete_key(k)
