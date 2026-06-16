from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route cho trang chủ
@app.route('/')
def home():
    return render_template('index.html')

# Route cho từng tuần
@app.route('/week1')
def week1():
    return render_template('week1.html')

@app.route('/week2')
def week2():
    return render_template('week2.html')

@app.route('/week3')
def week3():
    return render_template('week3.html')

@app.route('/week4')
def week4():
    return render_template('week4.html')

# Health check endpoint cho Cloud Run
@app.route('/health')
def health():
    return {'status': 'healthy', 'message': 'Server is running'}

@app.route('/cicd')
def cicd():
    return jsonify({
        "message": "Hello from CI/CD!",
        "status": "ok"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)