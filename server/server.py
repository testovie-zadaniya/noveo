from __future__ import print_function
from flask import Flask, request
import sys
import numexpr
import logging

app = Flask(__name__)
logging.getLogger("werkzeug").setLevel(logging.WARNING)

@app.route("/")
def one_minute_nobrainer():
    try:
        expr = request.args.get('expr')
#	out = expr
#	out = str(numexpr.evaluate(expr))
        print(numexpr.evaluate(expr), file=sys.stdout)
        return '', 204
    except:
        return 'bad expression', 400

@app.errorhandler(404)
def page_not_found(e):
    return '', 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082)
