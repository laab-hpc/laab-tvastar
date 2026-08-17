import os

app_host = os.getenv('TVST_HOST', '127.0.0.1')
app_port = int(os.getenv('TVST_PORT', '8000'))
app_mount = os.getenv('TVST_MOUNT', '')