import time
import urllib
from flask import Flask, request

app = Flask(__name__)


@app.route('/sleep/<seq>')
def sleep(seq):
    time.sleep(int(request.args.get('time', 10)))
    return seq

@app.route('/work/<seq>')
def work(seq):
    # Busily move electrons for `time` seconds
    t = time.time()
    while time.time() - t < int(request.args.get('time', 10)):
        pass
    return seq

@app.route('/req/<seq>')
def req(seq):
    url = 'http://localhost:6000/sleep/{}?time={}'.format(
        seq, int(request.args.get('time', 10)))
    return urllib.urlopen(url).read()
