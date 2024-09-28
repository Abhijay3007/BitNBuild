from flask import Flask, request, jsonify, redirect, url_for, render_template, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
app = Flask(__name__)

#Database For Users
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# Additional database URIs (binds) for clothes, accessories, personal items
app.config['SQLALCHEMY_BINDS'] = {
    'clothes': 'sqlite:///clothes.db',  # Database for clothes
    'accessories': 'sqlite:///accessories.db',  # Database for accessories
    'personal_items': 'sqlite:///personal_items.db'  # Database for personal items
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Clothes (bound to clothes.db)
class Clothes(db.Model):
    __bind_key__ = 'clothes'  # Bind to clothes.db
    id = db.Column(db.Integer, primary_key=True)
    brandname = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(10), nullable=False)
    colour = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

# Accessories (bound to accessories.db)
class Accessories(db.Model):
    __bind_key__ = 'accessories'  # Bind to accessories.db
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    brandname = db.Column(db.String(100), nullable=False)
    colour = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

# Personal Items (bound to personal_items.db)
class PersonalItems(db.Model):
    __bind_key__ = 'personal_items'  # Bind to personal_items.db
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        # To Check if user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({'message': 'Email address already exists'}), 400

        # Hash the password and store the user
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Redirect to login route after successful signup
        return redirect(url_for('login'))

    return render_template('signup.html')  # Render signup page for GET request


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # Find the user by email
        user = User.query.filter_by(email=email).first()

        # If user doesn't exist, redirect to signup page
        if not user:
            return redirect(url_for('signup'))  # Redirect to signup if user is not found

        # Check if the password is correct
        if not check_password_hash(user.password, password):
            return jsonify({'message': 'Invalid credentials, please try again'}), 401

        # Store user ID in session
        session['user_id'] = user.id

        return jsonify({'message': 'Login successful!', 'user': {'id': user.id, 'name': user.name, 'email': user.email}}), 200

    return render_template('login.html')  # Render login page for GET request
# Dashboard route
@app.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    user = User.query.get(user_id)
    return render_template('dashboard.html', user=user)



# Route to view clothes
@app.route('/clothes')
def clothes():
    clothes_items = Clothes.query.all()  # Query clothes.db
    return render_template('clothes.html', clothes=clothes_items)
     
# Route to add clothes (bound to clothes.db)
@app.route('/add_clothes', methods=['GET', 'POST'])
def add_clothes():
    if request.method == 'POST':
        brandname = request.form.get('brandname')
        size = request.form.get('size')
        colour = request.form.get('colour')
        quantity = request.form.get('quantity')
        price = request.form.get('price')

        new_clothes = Clothes(brandname=brandname, size=size, colour=colour, quantity=quantity, price=price)
        db.session.add(new_clothes)
        db.session.commit()  # This will save to clothes.db

        return redirect(url_for('clothes'))

    return render_template('add_Clothes.html')
@app.route('/accessories')
def accessories():
     accessories_items = Accessories.query.all()
     return render_template('accessories.html', accessories=accessories_items)

# Route to add new accessories
@app.route('/add_accessories', methods=['GET', 'POST'])
def add_accessories():
    if request.method == 'POST':
        brandname = request.form.get('brandname')
        type_of_accessory = request.form.get('type')
        colour = request.form.get('colour')
        quantity = request.form.get('quantity')
        price = request.form.get('price')

        # Create a new Accessories object and add it to the database
        new_accessory = Accessories( brandname=brandname,type=type_of_accessory, colour=colour, quantity=quantity, price=price)
        db.session.add(new_accessory)
        db.session.commit()  # Save to accessories.db

        # Redirect to the accessories list page
        return redirect(url_for('accessories'))

    # Render the add_accessories form
    return render_template('add_accessories.html')

@app.route('/personalitems')
def personalitems():
   
    # Query all personal items from the database
    personal_items_list = PersonalItems.query.all()
    
    # Pass the personal items list to the HTML template
    return render_template('personalitems.html', personalitems=personal_items_list)

# Route to add new personal items
@app.route('/add_personalitem', methods=['GET', 'POST'])
def add_personalitem():
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        description = request.form.get('description')
        quantity = request.form.get('quantity')
        value = request.form.get('value')

        # Create a new PersonalItems object and add it to the database
        new_item = PersonalItems(name=name,category=category,description=description, quantity=quantity, value=value)
        db.session.add(new_item)
        db.session.commit()  # Save to personalitems.db

        # Redirect to the personal items list page
        return redirect(url_for('personal_items'))

    # Render the add_personalitem form
    return render_template('add_personalitem.html')

# Run the Flask appi
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure database is created
    app.run(debug=True)



