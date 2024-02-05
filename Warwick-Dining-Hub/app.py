# Import dependencies -- reuse code others have given us.
import sqlite3
import os
from markupsafe import escape
import datetime
import sys
import logging
from flask import Flask, render_template, request, url_for, redirect, abort, g
from feedback import add_feedback

from add_inventory import get_db_connection, init_db

from werkzeug.utils import secure_filename  # Import secure_filename

app = Flask("app", static_url_path="/static")


app.config['UPLOAD_FOLDER'] = 'static/images'
app.logger.setLevel(logging.DEBUG)
# The database configuration
DATABASE = 'Dining_Hub.db'

# Functions to help connect to the database
# And clean up when this application ends.
def get_db_connection():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  # 设置 row_factory 属性为 sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

# Home page
@app.route("/")
@app.route("/index")
def home():
    dining_facilities = [
        {'name': 'Cafe Library', 'overview': 'Coffee and snacks'},
        {'name': 'University House', 'overview': 'Buffet and meals'}
    ]
    return render_template('index.html', active_page='dashboard')

# Search page
@app.route('/search')
def search():
    query = request.args.get('q', '')
    conn = get_db_connection()
    
    products = conn.execute("SELECT * FROM product WHERE name LIKE ? OR category LIKE ?", ('%' + query + '%', '%' + query + '%')).fetchall()
    conn.close()
    return render_template('search.html', query=query, products=products)

# User Profile page
@app.route("/profile")
def profile():
    user_info = {'name': 'John Doe'}
    return render_template('profile.html', user_info=user_info)

# Product page
@app.route('/products')
def products():
    conn = get_db_connection()
    products = conn.execute('SELECT name, category, price, size, image FROM product').fetchall()
    conn.close()
    return render_template('products.html', products=products, active_page='products')

# facilities info
facilities_details = {
    'StarBucks Cafe': {
        'open_hours': 'Mon-Sat: 10:00 AM - 5:00 PM, Sun: Closed',
        'address': 'The Library',
        'map_image': 'starbucks_map.png' 
    },
    'The Beautiful Duck Restaurant': {
        'open_hours': 'Mon-Sat: 11:30 AM - 10:00 PM, Sun: 11:30 AM - 6:00 PM',
        'address': 'Roots Building',
        'map_image': 'beautiful_duck_map.png' 
    },
    'Terrace Bar': {
        'open_hours': 'Mon-Sat: 11:00 AM - 4:00 AM, Sun: 4:00 PM - 4:00 AM',
        'address': 'Underground Plaza',
        'map_image': 'terrace_bar_map.png'  
    }
}
# facilities page
@app.route('/facilities')
def facilities():
    facility_query = request.args.get('facility')
    conn = get_db_connection()
    
    if facility_query:
        # 当有特定facility参数时，仅获取该设施的产品
        products = conn.execute('SELECT * FROM product WHERE facility = ?', (facility_query,)).fetchall()
        facilities_info = {facility_query: products}
    else:
        # 没有特定facility参数时，获取所有商家的产品
        facilities_info = {}
        for facility_name in ['The Beautiful Duck Restaurant', 'StarBucks Cafe', 'Terrace Bar']:
            products = conn.execute('SELECT * FROM product WHERE facility = ?', (facility_name,)).fetchall()
            facilities_info[facility_name] = products
    
    conn.close()
    return render_template('facilities.html', facilities_info=facilities_info, active_page='facilities', facilities_details=facilities_details)

# feedback page
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        restaurant = request.form['restaurant']
        rating = request.form['rating']
        message = request.form['message']
        add_feedback(name, email, restaurant, rating, message)  
        return redirect(url_for('feedback_submitted'))  
    # If it's a GET request, display the form
    return render_template('feedback.html', active_page='feedback')

@app.route('/feedback_submitted')
def feedback_submitted():
    # Displays a message that the submission was successful
    return render_template('feedback_result.html', active_page='feedback')


# booking page
@app.route("/booking")
def booking():
    return render_template('booking.html', active_page='booking')

@app.route('/submit-booking', methods=['POST'])
def submit_booking():
    name = request.form['name']
    email = request.form['email']
    date = request.form['date']
    time = request.form['time']
    guests = request.form['guests']
    facility = request.form['facility']


    conn = get_db_connection()
    cur = conn.cursor()

    # Insert booking information into the database
    cur.execute('INSERT INTO booking (name, email, date, time, guests, facility) VALUES (?, ?, ?, ?, ?, ?)',
                (name, email, date, time, guests, facility))
    conn.commit()  
    conn.close()  

    print(request.form)

    return render_template('booking_result.html')



# add product page
@app.route('/add_product', methods=['POST'])
def add_product():
    # 获取表单数据
    name = request.form['name']
    category = request.form['category']
    price = request.form['price']
    size = request.form['size']
    facility = request.form['facility']
    image = request.files['image']
        # Check if the file is selected
    if image:
        # Save the uploaded file to the specified directory
        image_filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))
    else:
        image_filename = None  # Set to None if no file is selected
    print(f"Name: {name}, Category: {category}, Price: {price}, Size: {size}, Facility: {facility}, Image: {image_filename}")
    app.logger.debug(f"Name: {name}, Category: {category}, Price: {price}, Size: {size}, Facility: {facility}, Image: {image_filename}")
    sys.stdout.flush()
    return redirect(url_for('products'))



### YOUR CODE GOES HERE ###
if __name__ == "__main__":
    with app.app_context():
        init_db()
    app.run(debug=True)
