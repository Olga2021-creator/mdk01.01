from sql_base import base_worker
from settings import BASE_PATH


base_worker.set_base_path(BASE_PATH)

if not base_worker.check_base():
    base_worker.create_base("../sql/tables.sql")
