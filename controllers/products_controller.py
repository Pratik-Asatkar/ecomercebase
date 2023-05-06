from flask import Blueprint, render_template, request, redirect


import models.products as product_db
import tools.image as image_db


product =  Blueprint('product', __name__, template_folder="templates")


@product.route('/<productid>')
def product_info(productid):
    product = product_db.get_product(productid)
    return render_template('product.html', product=product)


@product.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'GET':
        return "Product Add Endpoint!"
    elif request.method == 'POST':
        img_file = request.files['img']

        name = request.form.get('name')
        short_desc = request.form.get('short_desc')
        description = request.form.get('description')
        category = request.form.get('category')
        price = request.form.get('price')
        img = image_db.upload(img_file, ''.join(name.lower().split()), 'Products')['secure_url']

        product_data = {
            "_id": ''.join(name.lower().split()),
            "name": name,
            "short_desc": short_desc,
            "desc": description,
            "category": category,
            "price": int(price),
            "img": img
        }

        if product_db.add_product(product_data):
            return redirect('/')
        else:
            print("Something went wrong!")
            return redirect('/')
