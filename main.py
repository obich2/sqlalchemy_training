from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")

    # colonists = [['Scott', 'Ridley', 21, 'captain', 'research engineer', 'module_1', 'scott_chief@mars.org'],
    # ['Dafoe', "Willem", 25, 'collaborator', 'mechatronics engineer', 'module_2', 'dafoe_collab@mars.org'],
    # ['James', 'Alfredo', 30, 'collaborator', 'mechanical engineer', 'module_2', 'james_collab@mars.org'],
    # ['De Niro', 'Robert', 30, 'collaborator', 'senior research scientist', 'module_3', 'deniro_collab@mars.org']]
    # objects = [ User(*colonists[0]), User(*colonists[1]), User(*colonists[2]), User(*colonists[3]) ]
    # db_sess.bulk_save_objects(objects)
    # db_sess.commit()

    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == 1).first()
    jobs = Jobs(team_leader=user.id, job='deployment of residential modules 1 and 2', work_size=15, collaborators='2, 3',
                is_finished=False)
    db_sess.add(jobs)
    db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()
