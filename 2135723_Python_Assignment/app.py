from flask import Flask, abort,render_template,request,redirect
from models import db,StudentModel
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()
    db.session.commit()
 
@app.route('/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':

        # hobby = request.form.getlist('hobbies')
        # #hobbies = ','.join(map(str, hobby))
        # hobbies=",".join(map(str, hobby))


        first_name = request.form['first_name']
        last_name = request.form['last_name']
        address = request.form['address']  
        pincode = request.form['pincode']  
        country = request.form['country']
        # email = request.form['email']
        # password = request.form['password']
        # gender = request.form['gender']
        # hobbies = hobbies 
        
        custaddress = StudentModel(
            first_name=first_name,
            last_name=last_name,
            address=address,
            pincode=pincode,
            country = country,
            # email=email,
            # password=password,
            # gender=gender, 
            # hobbies=hobbies,
            
        )
        db.session.add(custaddress)
        db.session.commit()
        return redirect('/')
 
 
@app.route('/') 
def RetrieveList():
    custaddress = StudentModel.query.all()
    return render_template('datalist.html',custaddress = custaddress)
 
 
@app.route('/<int:id>')
def RetrieveStudent(id):
    custaddress = StudentModel.query.filter_by(id=id).first()
    if custaddress:
        return render_template('data.html', custaddress = custaddress)
    return f"Employee with id ={id} Doenst exist"
 
 
@app.route('/<int:id>/edit',methods = ['GET','POST'])
def update(id):
    student = StudentModel.query.filter_by(id=id).first()

    #hobbies = student.hobbies.split(' ')
    # print(hobbies)
    if request.method == 'POST':
        if student:
            db.session.delete(student)
            db.session.commit()
    #     tv = request.form['tv']    
    #     if tv is None:
    #               pass

    #    # print('Form:' + str(request.form))    
      
    #     cricket = request.form['cricket']
    #     movies = request.form['movies']
    #     hobbies = tv + ' ' +  cricket + ' ' + movies
    #     print('H' + hobbies)
        # hobby = request.form.getlist('hobbies')
        # #hobbies = ','.join(map(str, hobby))
        # hobbies =  ",".join(map(str, hobby)) 
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        address = request.form['address']
        pincode = request.form['pincode']
        country = request.form['country']
        # email = request.form['email']
        # password = request.form['password']
        # gender = request.form['gender']
        # hobbies = hobbies  
        

        student = StudentModel(
            first_name=first_name,
            last_name=last_name,
            address=address,
            pincode=pincode,
            country = country,
            # email=email,
            # password=password,
            # gender=gender, 
            # hobbies=hobbies,
            
        )
        db.session.add(student)
        db.session.commit()
        return redirect('/')
        return f"Student with id = {id} Does nit exist"
 
    return render_template('update.html', student = student)
 
 
@app.route('/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    custaddress = StudentModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if custaddress:
            db.session.delete(custaddress)
            db.session.commit()
            return redirect('/') 
        abort(404)
     #return redirect('/')
    return render_template('delete.html')
 

if __name__ == "__main__":
    app.run(debug=True) 