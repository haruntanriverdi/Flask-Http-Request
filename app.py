from flask import Flask, render_template, Blueprint
from views.main import Main, Error
import logging
from flask import current_app
from werkzeug.local import LocalProxy
from flask import Flask

app = Flask(__name__)

app.register_blueprint(Main, url_prefix="/")
app.register_blueprint(Error)

# register root logging
logging.basicConfig(filename='record.log', format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
logging.getLogger('werkzeug').setLevel(logging.INFO)

if __name__ == '__main__':
    app.run(debug=True)
