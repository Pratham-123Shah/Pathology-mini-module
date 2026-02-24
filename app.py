from flask import Flask,render_template,request,redirect

from models import get_tests,create_order

from controllers import change_order_status,create_result

from db import get_db


app=Flask(__name__)


@app.route("/")

def home():

    db=get_db()

    cursor=db.cursor(dictionary=True)

    cursor.execute(

        """SELECT lab_test_order.*,
        pathology_test.test_name

        FROM lab_test_order

        JOIN pathology_test

        ON pathology_test.id=
        lab_test_order.pathology_test_id

        """
    )

    orders=cursor.fetchall()

    return render_template(

        "order_list.html",

        orders=orders

    )



@app.route("/create_order")

def create_order_page():

    tests=get_tests()

    return render_template(

        "order_form.html",

        tests=tests

    )



@app.route("/save_order",methods=["POST"])

def save_order():

    create_order(request.form)

    return redirect("/")



@app.route("/change_status",methods=["POST"])

def change():

    change_order_status(

        request.form["id"],

        request.form["status"]

    )

    return redirect("/")



@app.route("/result/<id>")

def result_page(id):

    return render_template(

        "result_form.html",

        id=id

    )



@app.route("/save_result",methods=["POST"])

def save_result():

    create_result(

        request.form["id"],

        request.form["result"]

    )

    return redirect("/")



if __name__=="__main__":

    app.run()