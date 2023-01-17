from flask import Flask, render_template
# from jinja_cli import *
import json


app = Flask(__name__)


@app.route('/')
def index():
    with open("media/data.json", "r") as f:
        data = json.load(f)
    # print(json.dumps(data, indent = 5, sort_keys= True))
    # print(data['sku_table'])
    for x in data['crate_table']:
        x_values = x.keys()
    context = {
        'hub':data['hub'],
        'supplier_name':data['supplier_name'],
        'grn':data['grn'],
        'supplier':data['supplier'],
        'sku_table':data['sku_table'],
        'crate_table':data['crate_table'],
        'x_values':x_values
    }

    return render_template('index.html',context=context)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
 