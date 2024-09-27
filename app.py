from flask import Flask,render_template
app=Flask(__name__)
@app.route('/helloo')
def Hello():
    name="Haseena"
    return render_template('index.html',name=name)

@app.route('/fruit')
def fruit():
    fruits=['Mango','Grapes','Custard Apple']
    return render_template('index1.html',fruits=fruits)
@app.route('/age')
def age():
    age=19
    return render_template('index2.html',age=age)
    
if __name__=="__main__":
    app.run(debug=True)