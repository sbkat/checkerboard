from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def play():
    return render_template('index1.html')

@app.route('/4')
def playHalf():
    return render_template('index2.html')

@app.route('/<int:x>')
def playRows(x):
    return render_template('index3.html', row=x)

@app.route('/<int:x>/<int:y>')
def playRowsColumns(x,y):
    return render_template('index4.html', row=x, column=y)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def playRowsColumnsColors(x,y,color1,color2):
    return render_template('index5.html', row=x, column=y, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)