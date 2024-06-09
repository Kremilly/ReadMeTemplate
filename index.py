from flask import Flask, render_template, url_for, Response

app = Flask(__name__)

def read_file_content(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()

@app.route('/raw/<file_path>')
def read_file(file_path):
    content = read_file_content(f'templates/{file_path}.html')
    return Response(content, mimetype='text/plain')

@app.route('/')
def index():
    return render_template('render.html')

if __name__ == '__main__':
    app.run(debug=True)