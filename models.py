from db import get_db


def get_tests():

    db = get_db()

    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM pathology_test")

    return cursor.fetchall()



def create_order(data):

    db = get_db()

    cursor = db.cursor()

    cursor.execute(

        "SELECT COUNT(*) FROM lab_test_order"

    )

    count = cursor.fetchone()[0] + 1

    order_id = "LAB-" + str(count).zfill(4)


    cursor.execute(

        """INSERT INTO lab_test_order
        (order_id,patient_name,patient_phone,
        pathology_test_id,order_date)

        VALUES (%s,%s,%s,%s,%s)
        """,

        (

            order_id,

            data['patient_name'],

            data['patient_phone'],

            data['test_id'],

            data['order_date']

        )

    )

    db.commit()