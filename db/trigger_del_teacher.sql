CREATE TRIGGER delete_teacher
AFTER DELETE ON users
FOR EACH ROW
WHEN OLD.role = 'teacher'
BEGIN
    DELETE FROM teachers WHERE user_id = OLD.user_id;
END;
