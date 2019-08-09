#from app import app
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, User, Properties, Photos
from forms import NewUsersForm, SignInForm, PhotoUploadForm
from flask_login import current_user, login_user, logout_user, LoginManager
from helpers import closestMatches, backToArr
from werkzeug.security import generate_password_hash, check_password_hash

# configure Flask
app = Flask(__name__)

# project configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:JhuSli0d38oNNfAauam9@cnn-project3.cetsu4jwuaoc.us-east-1.rds.amazonaws.com:5432/fulldata'
db.init_app(app)
app.secret_key = 'cnn_project_3'

# LoginManager configuration
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


# the routes
# home route: this will get changed!! we just used this route for debugging purposes to compare to /search below
@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    if (current_user.is_authenticated):
        return render_template('welcome.html')
    else:
        return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')
# **** this will be used for 'bookmarked' properties, if we include
# **** this feature, otherwise we'll delete this route
# @app.route('/home')
# #@login_required
# def home():
#   if (current_user.is_anonymous):
#       return redirect(url_for('login'))
#   # get user's bookmarked pages if they have any
#   properties = current_user.get_properties()
#   return render_template('home.html', properties=properties)

# login page to validate user:
@app.route('/login', methods=['GET', 'POST'])
def login():
    if (current_user.is_authenticated):
        return redirect(url_for('index'))

    form = SignInForm()
    
    if (form.validate_on_submit()):
        user = User.query.filter_by(username=form.username.data).first()
        if (user is None or not check_password_hash(user.hashed_password, form.password.data)):
            flash("Invalid credentials", "error-message")
            return redirect(url_for('login'))
        
        login_user(user)
        flash("You have been successfully logged in", "success-message")
        return redirect(url_for('index'))
    
    return render_template('login.html', form=form)


# log current user out:
@app.route('/logout')
#@login_required
def logout():
    if (current_user.is_anonymous):
        return redirect(url_for('login'))
    
    logout_user()
    
    return redirect(url_for('index'))


# register a new user and create and store a hashed password:
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = NewUsersForm()
    if (request.method == 'GET'):
        # check that the user isn't already logged in
        if (current_user.is_authenticated):
            return redirect(url_for('index'))   
    else:   
        # create a new user with a hashed password, and save to database
        if (form.validate_on_submit()):
            username = User.query.filter_by(username=form.username.data).first()
            if (username is not None):
                flash("The username you have chosen is not valid, please try another.", "error-message")
                redirect(url_for('register'))
            else:
                user = User(first_name=form.first_name.data, last_name=form.last_name.data,
                    username=form.username.data, hashed_password=(generate_password_hash(form.password.data)))
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('index'))

    return render_template('register.html', form=form)


# pull out the matching database properties for the given user input
#### this is a dummy routine so far, will be updated once VGG16 is finished ####
@app.route('/results', methods=['GET', 'POST'])
def results():
    if (current_user.is_anonymous):
        return redirect(url_for('login'))

    form = PhotoUploadForm()

    # photo upload works, but doesn't save the file yet, this is being worked on
    if (request.method == 'POST'):
        photo = request.files['photo']

        mlsnums = closestMatches(photo)

        properties = {}
        top = {}
        count = 0;

        for mlsnum in mlsnums:
            prop = Properties.query.filter_by(mlsnum=mlsnum).first()

            price = str(prop.listprice)
            p = str(prop.beds) + " beds | " + str(prop.baths) + " baths | " + str(int(prop.sqft)) + " sqft"

            # reformat the price string so it removes decimals and adds the price sign
            if (price is not None):
                sub = str(price).split(".")[0]
                price = "${:,}".format(int(sub))

            if count == 0:

                # separate out the 'top' hit to be displayed separately
                top[prop.mlsnum] = {
                    "string" : p,
                    "photo" : prop.photourl,
                    "mlsnum" : mlsnum
                }

                if (price is not None):
                    top[prop.mlsnum].update({"price": price})
            else:
                properties[prop.mlsnum] = {
                "string" : p,
                "photo" : prop.photourl,
                "mlsnum" : mlsnum
            }

                if (price is not None):
                    properties[prop.mlsnum].update({"price": price})
            count = count + 1

        print(str(top))
        return render_template('results.html', properties=properties, top=top)
    else:
        return render_template('search.html', form=form)


# this page will hold our visualizations
@app.route('/stats', methods=['GET'])
def stats():
    # make sure the user is logged in
    if (current_user.is_anonymous):
        return redirect(url_for('login'))

    else:
        mlsnum = request.args.get('mlsnum')
        stats = {}
        prop = Properties.query.filter_by(mlsnum=mlsnum).first()

        price = str(prop.listprice)

        if (price is not None):
            sub = str(price).split(".")[0]
            price = "${:,}".format(int(sub))
            stats["price"] = price

        if (prop.soldprice is not None):
            stats["sold"] = True

        if (prop.garage is not None and prop.garage != 0):
            stats["garage"] = prop.garage

        stats["address"] = str(prop.address) + "\n" + str(prop.city) + ", " + str(prop.state) + " " + str(prop.zipcode)
        stats["string"] = str(prop.beds) + " beds | " + str(prop.baths) + " baths | " + str(int(prop.sqft)) + " sqft"
        stats["listdate"] = prop.listdate
        stats["lotsize"] = prop.lotsize
        stats["remarks"] = prop.remarks
        stats["photo"] = prop.photourl

        return render_template('stats.html', stats=stats)


if __name__ == "__main__":
    app.run()