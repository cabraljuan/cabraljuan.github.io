from flask import Flask, render_template, request

app = Flask(__name__)

def cobb_douglas(alpha, beta, p1, p2, w):
    alpha = float(alpha)
    beta = float(beta)
    p1 = float(p1)
    p2 = float(p2)
    w = float(w)
    
    marshall_x1 = (w / p1) * (alpha / (alpha + beta))
    marshall_x2 = (w / p2) * (beta / (alpha + beta))
    utility = (marshall_x1 ** alpha) * (marshall_x2 ** beta)
    
    return marshall_x1, marshall_x2, utility

@app.route('/', methods=['GET', 'POST'])
def index2():
    if request.method == 'POST':
        alpha = request.form['alpha']
        beta = request.form['beta']
        p1 = request.form['p1']
        p2 = request.form['p2']
        w = request.form['w']
        
        marshall_x1, marshall_x2, utility = cobb_douglas(alpha, beta, p1, p2, w)
        return render_template('result.html', marshall_x1=marshall_x1, marshall_x2=marshall_x2, utility=utility)

    return render_template('index2.html')

if __name__ == "__main__":
    app.run(debug=True)
