from flask import Flask, url_for, render_template, redirect
from data import db_session
from data.users import User
from forms.user import RegisterForm
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def main():
    db_session.global_init("db/blogs.db")

    # colonists = [['Scott', 'Ridley', 21, 'captain', 'research engineer', 'module_1', 'scott_chief@mars.org'],
    # ['Dafoe', "Willem", 25, 'collaborator', 'mechatronics engineer', 'module_2', 'dafoe_collab@mars.org'],
    # ['James', 'Alfredo', 30, 'collaborator', 'mechanical engineer', 'module_2', 'james_collab@mars.org'],
    # ['De Niro', 'Robert', 30, 'collaborator', 'senior research scientist', 'module_3', 'deniro_collab@mars.org']]
    # objects = [ User(*colonists[0]), User(*colonists[1]), User(*colonists[2]), User(*colonists[3]) ]
    # db_sess.bulk_save_objects(objects)
    # db_sess.commit()

    # db_sess = db_session.create_session()
    # user = db_sess.query(User).filter(User.id == 1).first()
    # jobs = Jobs(team_leader=user.id, job='deployment of residential modules 1 and 2', work_size=15,
    #             collaborators='2, 3',
    #             is_finished=False)
    # db_sess.add(jobs)
    # db_sess.commit()
    # db_sess = db_session.create_session()
    # jobs = db_sess.query(Jobs).all()
    # print(jobs)
    # return render_template('index.html', jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
