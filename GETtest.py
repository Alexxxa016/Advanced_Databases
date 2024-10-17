import couchdb


url = 'http://T00222705:Admin1234@127.0.0.1:5984'  
db_name = 'drivers'  

try:
    
    couch = couchdb.Server(url)
    
    
    if db_name in couch:
        db = couch[db_name]
        print(f"Connected to CouchDB database: {db_name}")
        
        
        for doc_id in db:
            doc = db[doc_id]
            print(doc)
    else:
        print(f"Database '{db_name}' not found.")
except couchdb.http.Unauthorized as e:
    print(f"Authorization error: {e}")
except Exception as e:
    print(f"Connection error: {e}")
