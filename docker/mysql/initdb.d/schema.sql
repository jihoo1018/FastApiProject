create table blogusers(
    blog_userid varchar(20) primary key ,
    email varchar(20),
    nickname varchar(20),
    password varchar(20)
)

create table posts(
    post_id varchar(20) primary key ,
    title varchar(100),
    content varchar(1000),
    create_at datetime DEFAULT CURRENT_TIMESTAMP,
    updated_at datetime ON UPDATE CURRENT_TIMESTAMP
)