from app.main import app
# let app be base package

@app.route('/')
def home():
    return 'Flask API started on Pythonanywhere. Hi there!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True) # `127.0.0.1` only allowed local pc can visit
