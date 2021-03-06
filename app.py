from flask import Flask,render_template,session,request,redirect,url_for
import os
import scriping


#インスタンスを作成
app = Flask(__name__)

key = os.urandom(21)
app.secret_key = key

id_pwd ={'mememori8888@gmail.com':'mm19830831'}

#メイン
@app.route('/')
def index():
    if not session.get('login'):
        return redirect(url_for('login'))
    else:
        return render_template('Flaskindex.html')

@app.route('/login')
def login():
    return render_template('login.html')

#ログイン認証
@app.route('/logincheck',methods=['post'])
def logincheck():
    user_id = request.form['user_id']
    password = request.form['password']

    if user_id in id_pwd:
        if password == id_pwd[user_id]:
            session['login'] = True
        else:
            session['login'] = False
    
    else: 
        session['login'] = False

    if session['login']:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

#スクレイピングプログラム
@app.route('/scriping')

def get():
    scriping.scriping()
    return render_template('result.html')


#logout
@app.route('/logout')
def logout():
    session.pop('login',None)
    return redirect(url_for('index'))

#アプリケーションの起動
if __name__ == '__main__':
    app.run(debug=True)