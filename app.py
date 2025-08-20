# -*- coding: utf-8 -*-
"""
ギターECサイトのFlaskアプリ本体
"""
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # セッション管理用

 # サンプルギターデータ
GUITARS = [
    {'id': 1, 'name': 'Fender Stratocaster', 'price': 120000, 'image': 'strat.jpg'},
    {'id': 2, 'name': 'Gibson Les Paul', 'price': 150000, 'image': 'lespaul.jpg'},
    {'id': 3, 'name': 'Ibanez RG', 'price': 90000, 'image': 'ibanez.jpg'},
]

# インメモリでユーザー情報を保持
USERS = []
@app.route('/users', methods=['GET', 'POST'])
def users():
    """マイページ（ユーザー情報登録ページ）"""
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        phone = request.form['phone']
        USERS.append({'name': name, 'address': address, 'phone': phone})
    return render_template('mypage.html', users=USERS)

@app.route('/')
def index():
    """トップページ：ギター一覧表示"""
    return render_template('index.html', guitars=GUITARS)

@app.route('/add_to_cart/<int:guitar_id>')
def add_to_cart(guitar_id):
    """カートにギターを追加"""
    cart = session.get('cart', [])
    cart.append(guitar_id)
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    """カートページ"""
    cart = session.get('cart', [])
    items = [g for g in GUITARS if g['id'] in cart]
    total = sum(g['price'] for g in items)
    return render_template('cart.html', items=items, total=total)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    """購入ページ：ユーザー情報選択または入力"""
    cart = session.get('cart', [])
    items = [g for g in GUITARS if g['id'] in cart]
    total = sum(g['price'] for g in items)
    selected_user = None
    if request.method == 'POST':
        if 'select_user' in request.form:
            idx = int(request.form['select_user'])
            selected_user = USERS[idx]
            name = selected_user['name']
            address = selected_user['address']
            phone = selected_user['phone']
        else:
            name = request.form['name']
            address = request.form['address']
            phone = request.form['phone']
        # ...ここで注文処理...
        session.pop('cart', None)
        return render_template('checkout.html', items=items, total=total, name=name, address=address, phone=phone, success=True, users=USERS)
    return render_template('checkout.html', items=items, total=total, users=USERS)

if __name__ == '__main__':
    app.run(debug=True)
