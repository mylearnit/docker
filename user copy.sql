ALTER SESSION SET "_ORACLE_SCRIPT"=true;
CREATE USER csbdev IDENTIFIED BY TestUser123;
GRANT CONNECT, RESOURCE TO csbdev;
GRANT CREATE TABLE TO csbdev;
GRANT CREATE SESSION TO csbdev;
ALTER USER csbdev QUOTA UNLIMITED ON USERS;
exit;