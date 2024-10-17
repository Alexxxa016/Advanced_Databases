from flask import Flask, jsonify, request, render_template
import couchdb

app = Flask(__name__)

class CouchDBClient:
    def __init__(self, url='http://T00222705:Admin1234@127.0.0.1:5984', db_name='drivers'):
        
        try:
            self.couch = couchdb.Server(url)
            #Get the database
            if db_name in self.couch:
                self.db = self.couch[db_name]
                print(f"Connected to CouchDB database: {db_name}")
            else:
                print(f"Database '{db_name}' not found.")
        except couchdb.http.Unauthorized as e:
            print(f"Authorization error: {e}")
        except Exception as e:
            print(f"Connection error: {e}")

client = CouchDBClient(url='http://T00222705:Admin1234@127.0.0.1:5984')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mango_query', methods=['POST'])
def mango_query():
    query = request.json
    try:
        result = list(client.db.find(query))
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/mapreduce_query', methods=['POST'])
def mapreduce_query():
    view_name = request.json.get('view_name')  
    use_reduce = request.json.get('use_reduce', False)  

    try:
        
        result = client.db.view(f'allDocs/{view_name}', reduce=use_reduce)
        return jsonify(list(result))
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
