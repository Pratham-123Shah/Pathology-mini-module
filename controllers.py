from db import get_db


def change_order_status(order_id,new_status):

    db=get_db()

    cursor=db.cursor()

    cursor.execute(

        "SELECT status FROM lab_test_order WHERE id=%s",

        (order_id,)

    )

    current=cursor.fetchone()[0]


    valid={

        "Draft":["Ordered","Cancelled"],

        "Ordered":["Completed"],

        "Completed":[],

        "Cancelled":[]

    }


    if new_status not in valid[current]:

        raise Exception("Invalid Status")


    cursor.execute(

        "UPDATE lab_test_order SET status=%s WHERE id=%s",

        (new_status,order_id)

    )

    db.commit()



def create_result(order_id,result):

    db=get_db()

    cursor=db.cursor()


    cursor.execute(

        "SELECT status FROM lab_test_order WHERE id=%s",

        (order_id,)

    )


    status=cursor.fetchone()[0]


    if status!="Ordered":

        raise Exception("Result not allowed")


    cursor.execute(

        """INSERT INTO lab_test_result
        (test_order_id,result_value)

        VALUES(%s,%s)
        """,

        (order_id,result)

    )


    cursor.execute(

        """UPDATE lab_test_order
        SET status='Completed'
        WHERE id=%s
        """,

        (order_id,)

    )


    db.commit()