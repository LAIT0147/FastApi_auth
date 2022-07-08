from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.config import DATABASE_URL


def main():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine.connect())

    session.execute("""create table users(
    id integer not null primary key,
    email varchar(200),
    password varchar(200),
    first_name varchar(200),
    last_name varchar(200),
    nickname varchar(200),
    created_at varchar(200)
    );
    """)

    session.execute("""create table auth_token(
    id integer not null primary key,
    token varchar(256),
    user_id integer references users,
    created_at varchar(200)
    );
    """)

    session.execute("""create table stream(
    id integer not null primary key,
    user_id integer references users,
    title varchar(200),
    topic varchar(200),
    status varchar(200),
    created_at varchar(200)
    );
    """)


    session.close()


if __name__ == '__main__':
    main()
