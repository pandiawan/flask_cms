import os
from datetime import datetime
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def create_directory(fullpath):
    if os.path.exists(fullpath):
        return True
    os.makedirs(fullpath, exist_ok=True)
    return True


def get_upload_dir(folder):
    full_dir = '{}/{}/{:02d}/{:02d}'.format(folder, datetime.now().year, datetime.now().month, datetime.now().day)
    mkdir = create_directory(full_dir)
    if mkdir:
        return full_dir


def upload(file, folder):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_dir = get_upload_dir(folder)
        if not upload_dir:
            return None, True
        file_path = os.path.join(upload_dir, filename)
        file.save(os.path.join(os.getcwd(), file_path))
        return file_path, False
    else:
        return None, True
