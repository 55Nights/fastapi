-- insert new posts
USE fastapi;
ALTER TABLE post MODIFY id INT AUTO_INCREMENT;

INSERT INTO post (title, content, publish)
VALUES ('First Post', 'This is my first post', true);

INSERT INTO post (title, content, publish)
VALUES ('Second Post', 'This is my second post', true);