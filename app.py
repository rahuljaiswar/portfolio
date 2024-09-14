from flask import Flask, render_template
from flask_caching import Cache

app = Flask(__name__)

# Configuring Cache
cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

@app.route('/')
@cache.cached(timeout=60*60)  # Cache for 1 hour
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
