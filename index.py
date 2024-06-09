from flask import Flask, render_template, url_for, Response

app = Flask(__name__)

def read_file_content(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()

@app.route('/')
def index():
    content = read_file_content(f'templates/render.html')
    return Response(content, mimetype='text/plain')

@app.route('/example')
def example():
    return render_template('rendered.html')

if __name__ == '__main__':
    app.run(debug=True)