import mysql.connector

class Database:

  db_connection = ""
  query = ""
  result_set = ""
  params = ""

  # Constructor to set the database connection
  def __init__(self):

    self.mysql = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="pmanager"
    )

  def get_owner(self, c_table, c_table_column, request_parameter, c_table_fkey, owner_table, owner_fk):

    # c = stands for current, which is related to the current request

    db_connection = self.mysql.cursor(dictionary=True)
    query = "select * from {} where {}=%s".format(c_table, c_table_column)
    params = (request_parameter, )
    db_connection.execute(query, params )
    c_request_record = db_connection.fetchone()

    owner_query_value = c_request_record[c_table_fkey]

    query2 = "select * from {} where {}=%s".format(owner_table, owner_fk)
    params2 = (owner_query_value, )
    db_connection.execute(query2, params2)
    owner_record = db_connection.fetchone()

    if 'password' in owner_record:
      owner_record.pop("password")

    return owner_record


  def get_query_relation(self, table_name):
    db_connection = self.mysql.cursor(dictionary=True)
    query = "select * from {} where {}=%s".format(table_name, self.get_relation_where)
    params = (self.get_relation_value,)
    db_connection.execute("select * from users where id=1")
    result = db_connection.fetchone()

    print(result)

    return self


  # this is a general method used to retrieve all the records from a table
  def all(self, table_name):

    self.db_connection = self.mysql.cursor(dictionary=True)
    self.query = "SELECT * from {} order by id desc".format(table_name)
    self.db_connection.execute(self.query)
    self.result_set = self.db_connection.fetchall()

    return self.result_set

  # this method accepts a table name and sets single_query variable to the result set
  # the method return self so that users can keep chaining
  # Example: you can call variable_name.single(table_name).single_query
  def select_where(self, table_name, where, where_value):

    self.db_connection = self.mysql.cursor(dictionary=True)
    self.query = "SELECT * from {} where {}=%s".format(table_name, where)
    self.params = (where_value, )
    self.db_connection.execute(self.query, self.params)

    return self.db_connection.fetchone()

  # when calling this method, it is assumed that your single_query variable has already been set
  # the method accepts the name of the table which you the records from and takes a where clause
  # the value from the where clause comes from single_query variable
  def with_relation(self, table_name):
    self.db_connection = self.mysql.cursor(dictionary=True)
    self.query = "SELECT * from {} where {}=%s".format(table_name, self.single_query)
    self.params = (self.single_query, )
    self.db_connection.execute(self.query, self.params )
    self.result_set = self.db_connection.fetchall()

    return self.result_set

  def delete_where(self, table_name, where, where_value):

    self.db_connection = self.mysql.cursor()
    self.query = "DELETE FROM {} where {}=%s".format(table_name, where)
    self.params = (where_value, )
    self.db_connection.execute(self.query, self.params)
    self.mysql.commit()

    return self

  def empty_table(self, table_name ):

    db_connection = self.mysql.cursor()
    query = "DELETE FROM {}".format(table_name)
    db_connection.execute(query)
    self.mysql.commit()

    return self

  def create(self):
    self.db_connection = self.mysql.cursor()
    self.query = "insert into posts (title, postContent) values (%s, %s)"
    self.params = ('Post title', 'Post content')
    self.db_connection.execute(self.query, self.params)
    self.mysql.commit()

    return self


  # accepts the table name and the form data
  def insert(self, table_name, form):

    form_data = dict(form)
    form_data.pop("csrf_token")
    form_data.pop("action")

    table_values = ""                                                 # stores the placeholders
    i = 0
    j = 0
    table_attributes = ""                                             # represents the attribute names to insert data on

    db_query_attributes = list(form_data.keys())                      # creates a list with all form data keys
    form_fields = list(form_data.values());                           # creates a list with all form field values

    form_fields_len = len(form_fields)

    for l in form_fields:
      i += 1

      if i < form_fields_len:
        table_values += "%s, "
      else:
        table_values += "%s"

    for m in db_query_attributes:
      j += 1
      if j < len(db_query_attributes):
        table_attributes += m + ","
      else:
        table_attributes += m

    self.db_connection = self.mysql.cursor()
    self.query = "insert into {} ({}) values ({})".format(table_name, table_attributes, table_values)
    self.params = form_fields
    self.db_connection.execute(self.query, self.params)
    self.mysql.commit()

    return


  def register_user(self, table_name, form_data):
    table_values = ""  # stores the placeholders
    i = 0
    j = 0
    table_attributes = ""  # represents the attribute names to insert data on

    db_query_attributes = list(form_data.keys())  # creates a list with all form data keys
    form_fields = list(form_data.values());  # creates a list with all form field values

    form_fields_len = len(form_fields)

    for l in form_fields:
      i += 1

      if i < form_fields_len:
        table_values += "%s, "
      else:
        table_values += "%s"

    for m in db_query_attributes:
      j += 1
      if j < len(db_query_attributes):
        table_attributes += m + ","
      else:
        table_attributes += m

    self.db_connection = self.mysql.cursor()
    self.query = "insert into {} ({}) values ({})".format(table_name, table_attributes, table_values)
    self.params = form_fields
    self.db_connection.execute(self.query, self.params)
    self.mysql.commit()

    return


  ####### UPDATE METHOD - SIMPLE

  def  update_where(self, table_name, where, where_value, form_data):

    form_keys = list(form_data.keys())
    form_values = list(form_data.values())
    form_values.pop(0)
    form_values.pop(-1)
    form_keys.pop(0)
    form_keys.pop(-1)

    print("Form values")
    print(form_values)

    print("Form Keys")
    print(form_keys)

    i = 0;
    for x in form_values:
      print("Key")
      print(form_keys[i]);
      print(x)


      db_connection = self.mysql.cursor()
      query = "update {} set {}=%s where {}=%s".format(table_name, form_keys[i], where)
      params = (x, where_value)
      db_connection.execute(query, params)
      self.mysql.commit()

      i += 1

    return self

