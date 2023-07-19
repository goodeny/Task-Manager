import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='task_manager'
)

def insert_task(title, stats):
    cursor = cnx.cursor()
    query = "INSERT INTO tasks (title, stats) VALUES (%s, %s)"
    values = (title, stats)
    cursor.execute(query, values)
    cnx.commit()

    cursor.close()

def get_all_tasks():
    cursor = cnx.cursor()
    query = "SELECT * FROM tasks"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()

    return results

def delete_task(task_id):
    cursor = cnx.cursor()
    query = "DELETE FROM tasks WHERE ID = %s"
    values = (task_id,)
    cursor.execute(query, values)
    cnx.commit()

    cursor.close()

def update_task_stats(task_id, new_stats):
    cursor = cnx.cursor()
    query = "UPDATE tasks SET stats = %s WHERE ID = %s"
    values = (new_stats, task_id)
    cursor.execute(query, values)
    cnx.commit()

    cursor.close()