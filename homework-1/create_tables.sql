-- SQL-команды для создания таблиц
--
-- Name: mployeese; Type: TABLE; Schema: public; Owner: -; Tablespace:
--
CREATE TABLE mployeese(
    employee_id int PRIMARY KEY,
    first_name text,
    last_name text,
    title text,
    birth_date date,
    notes text,
);


--
-- Name: customers; Type: TABLE; Schema: public; Owner: -; Tablespace:
--
CREATE TABLE customers(
    customer_id int PRIMARY KEY,
    company_name text
    contact_name text
);


--
-- Name: orders; Type: TABLE; Schema: public; Owner: -; Tablespace:
--
CREATE TABLE orders(
    order_id int PRIMARY KEY,
    customer_id text,
    employee_id text,
    order_date date,
    ship_city text
)


