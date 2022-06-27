
from flask import Flask,make_response,request,jsonify
from flask_mongoengine import MongoEngine
import smtplib, ssl
from flask_cors import CORS
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "******@gmail.com"
password = "*******"



app = Flask(__name__)
CORS(app)
db = MongoEngine()
db.init_app(app)
db.disconnect()
database_name = "Cineminimum"
DB_URI = "mongodb+srv://*******:******cinemacluster.bi53e0o.mongodb.net/{}?retryWrites=true&w=majority".format(database_name)
app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine()
db.init_app(app)

@app.route('/api/form')
def form():
    return render_template('movie.js')

###### MOVIES #########################################################################################################

class movie(db.Document):
    _id = db.ObjectIdField()
    c_id = db.StringField()
    m_name = db.StringField()
    duration = db.IntField()
    description = db.StringField()
    age_group = db.StringField()
    release_date = db.IntField()
    img_path = db.StringField()
    on_air = db.StringField()

    def to_json(self):

        return {
            "_id":self.pk,
            "c_id":self.c_id,
            "m_name":self.m_name,
            "duration":self.duration,
            "description":self.description,
            "age_group":self.age_group,
            "release_date":self.release_date,
            "img_path":self.img_path,
            "on_air":self.on_air

        }

@app.route("/api/createMovie", methods=['POST'])
def createMovie():
    movie1 = movie(c_id="1",m_name="test",duration=1234,
                   description="test",age_group="test",release_date=1234,img_path="/images/")
    movie1.save()
    a=make_response("",201)
    a.headers['Access-Control-Allow-Origin'] = '*'
    return a

@app.route("/api/movies", methods=['GET','POST'])
def api_movies():
    if request.method == "GET":
        movies = []
        for mov in movie.objects:
            movies.append(mov)
        a = make_response(jsonify(movies), 200)
        a.headers['Access-Control-Allow-Origin'] = '*'
        return a

@app.route("/api/movies/<_id>", methods=['GET','POST'])
def selectMovie(_id):
    if request.method == "GET":
        movie_obj = movie.objects(_id=_id).first()
        if movie_obj:
            abc = []
            for x in session_id.objects(m_id=_id):
                abc.append(x)
            a = make_response(jsonify(movie_obj.to_json(),abc),200)
            a.headers['Access-Control-Allow-Origin'] = '*'
            return a



###### BOOKS  #########################################################################################################

class books(db.Document):
    cust_id = db.StringField()
    session_id = db.StringField()

    def to_json(self):

        return {
            "cust_id":self.cust_id,
            "session_id":self.session_id
        }
@app.route("/api/books", methods=['POST'])
def api_books():
    content = request.get_json(silent=True)
    cart = []
    for key in content.keys():
        cart.append(content[key])
    b = books(cust_id=cart[0],session_id=cart[1])
    b.save()


    a = make_response("This page is for Admin", 200)
    a.headers['Access-Control-Allow-Origin'] = '*'
    return a

@app.route("/api/mailto",methods=['POST'])
def mailto():



    content = request.get_json(silent=True)
    cart = []
    for key in content.keys():
        cart.append(content[key])
    receiver_email = cart[0]
    message = str(cart[1])+" " + str(cart[2])+" " + str(cart[3])+" " + str(cart[4])+" " + str(cart[5])+" " + str(cart[6])+" " + str(cart[7])
    # Create a secure SSL context

    # Try to log in to server and send email
    try:
        a= make_response("Success",200)
        a.headers['Access-Control-Allow-Origin'] = '*'
        return a
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()



    ###### CINEMAS  #########################################################################################################

class cinema(db.Document):
    c_name = db.StringField()
    location = db.StringField()


    def to_json(self):

        return {
            "c_name":self.c_name,
            "location":self.location
        }

@app.route("/api/cinema", methods=['GET'])
def api_cinema():
    if request.method == "GET":
        cinemas = []
        for cnm in cinema.objects:
            cinemas.append(cnm)
        a=make_response(jsonify(cinemas), 200)
        a.headers['Access-Control-Allow-Origin'] = '*'
        return a

###### CUSTOMERS  ######################################################################################################

class customer(db.Document):
    email= db.StringField()
    age = db.IntField()
    phone_no = db.IntField()
    f_name = db.StringField()
    l_name = db.StringField()

    def to_json(self):

        return {
            "email":self.email,
            "age":self.age,
            "phone_no":self.phone_no,
            "f_name":self.f_name,
            "l_name":self.l_name
        }
@app.route("/api/newcustomer", methods=['POST'])
def newCustomer():
    content = request.get_json(silent=True)
    cart = []
    for key in content.keys():
        cart.append(content[key])
    cere = customer(email=cart[0],age=cart[1],phone_no=cart[2],f_name=cart[3],l_name=cart[4])

    cere.save()

    a = make_response(jsonify(content),200)
    a.headers['Access-Control-Allow-Origin'] = '*'
    return a


#### DISCOUNTS  ########################################################################################################

class discount(db.Document):
    m_id = db.StringField()
    d_amount = db.StringField()


    def to_json(self):

        return {
            "m_id":self.m_id,
            "d_amount":self.d_amount,
        }

@app.route("/api/discount", methods=['GET'])
def getDiscount():
    pass

###### MOVIE THEATER  ##################################################################################################

class movie_theater(db.Document):
    _id = db.ObjectIdField()
    c_id = db.StringField()
    th_type = db.StringField()
    th_no = db.IntField()
    capacity = db.IntField()

    def to_json(self):

        return {
            "_id":self.pk,
            "c_id":self.c_id,
            "th_type":self.th_type,
            "th_no":self.th_no,
            "capacity":self.capacity

        }


@app.route("/api/theaters", methods=["POST"])
def api_theater():
    if request.method == "POST":
            theaterList = []
            for a in movie_theater.objects():
                theaterList.append(a)
            a=make_response(jsonify(theaterList), 200)
            a.headers['Access-Control-Allow-Origin'] = '*'
            return a


###### SEATS  ##########################################################################################################

class seats(db.Document):
    th_no = db.IntField()
    s_number = db.IntField()
    seated = db.BooleanField()
    session_id = db.StringField()
    m_id = db.StringField()


    def to_json(self):

        return {
            "th_no":self.th_no,
            "s_number":self.s_number,
            "seated":self.seated,
            "session_id":self.session_id,
            "m_id":self.m_id
        }

@app.route("/api/check_seats/<s_id>", methods=['POST'])
def api_checkseat(s_id):
    abc =[]
    full = []
    for x in seats.objects(session_id=s_id):
        abc.append(x)
    i=0
    for y in abc:
        if y['seated'] == True:
            full.append(y['s_number'])
            i+=1
    a=make_response(jsonify(full),200)
    a.headers['Access-Control-Allow-Origin'] = '*'
    return a




@app.route("/api/seats/<s_id>", methods=['POST'])
def api_seats(s_id):
    if request.method == 'POST':
            all_Seats = []
            for ass in seats.objects(session_id=s_id):
                all_Seats.append(ass)
            a=make_response(jsonify(all_Seats),200)
            a.headers['Access-Control-Allow-Origin'] = '*'
            return a






##### SESSION_ID  ######################################################################################################


class session_id(db.Document):

    _id = db.ObjectIdField()
    th_no = db.IntField()
    session = db.StringField()
    m_id = db.StringField()
    price = db.IntField()

    def to_json(self):
        return {
            "_id":self.pk,
            "th_no":self.th_no,
            "session":self.session,
            "m_id":self.m_id,
            "price":self.price

        }

@app.route("/api/sessions", methods=['GET'])
def check_ses():
    a = make_response(jsonify(session_id.objects),200)
    a.headers['Access-Control-Allow-Origin'] = '*'
    return a






if __name__ == "__main__":
    app.run()



