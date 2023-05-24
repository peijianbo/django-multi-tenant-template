import pymysql

pymysql.install_as_MySQLdb()
try:
    # Werkzeug.Local is a reliable cache（https://blog.csdn.net/bocai_xiaodaidai/article/details/118569734）
    from werkzeug.local import Local as LocalContext
except ImportError:
    from threading import local as LocalContext


thread_local = LocalContext()
