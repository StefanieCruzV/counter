from crypt import methods
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'times in page'
# our index route will handle rendering our form


@app.route('/', methods=['get'])
def index():
    # print("index")
    # print(request.form)
    if 'times' in session:
        session['times'] = session['times']+1
    else:
        session['times'] = 1

    return render_template("index.html")

@app.route('/increase', methods=['post'])
def counttwo():
    # print("enelpost")
    if 'times' in session:
        session['times'] = session['times']+1
    else:
        session['times'] = 1
    return redirect("/")

@app.route('/increaseby', methods=['post'])
def countby():
    print(request.form['increaseby'])
    if 'times' in session:
        session['times'] = session['times']+ (int(request.form['increaseby'])-1)
    else:
        session['times'] = 1
    return redirect("/")



@app.route('/destroy_session')
def destroy():
    print("destroy")
    # del session["times"]
    session.clear() 
    # delete all keys in session
    return redirect("/")


# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     # print(request.form)
#     # Never render a template on a POST request.
#     # Instead we will redirect to our index route.
#     # return redirect('/')
#     session['username'] = request.form['name']
#     session['useremail'] = request.form['email']
#     return redirect('/show')

# @app.route('/destroy_session')
# def index():
#     return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
