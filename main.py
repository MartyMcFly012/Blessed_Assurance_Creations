from flask import Flask, render_template
from data_access import get_all_products, get_product_by_id

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to the Self-Care Goods Store!"


@app.route('/products')
def products():
    products_list = get_all_products()
    return render_template('products.html', products=products_list)


@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = get_product_by_id(product_id)
    if product:
        return render_template('product_detail.html', product=product)
    else:
        return "Product not found"


if __name__ == '__main__':
    app.run(debug=True)
