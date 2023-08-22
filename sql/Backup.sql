--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

-- Started on 2023-08-22 12:05:33

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 5 (class 2615 OID 16535)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 3364 (class 0 OID 0)
-- Dependencies: 5
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 16536)
-- Name: incomes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.incomes (
    id integer NOT NULL,
    userid integer NOT NULL,
    name character varying NOT NULL,
    amount money NOT NULL,
    note character varying,
    date date NOT NULL,
    repeats_monthly boolean DEFAULT false NOT NULL,
    repeats_annually boolean DEFAULT false NOT NULL,
    repeats_weekly boolean DEFAULT false NOT NULL
);


ALTER TABLE public.incomes OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16544)
-- Name: incomes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.incomes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.incomes_id_seq OWNER TO postgres;

--
-- TOC entry 3366 (class 0 OID 0)
-- Dependencies: 215
-- Name: incomes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.incomes_id_seq OWNED BY public.incomes.id;


--
-- TOC entry 216 (class 1259 OID 16545)
-- Name: outgoings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.outgoings (
    id integer NOT NULL,
    userid integer NOT NULL,
    name character varying NOT NULL,
    amount money NOT NULL,
    note character varying,
    date date NOT NULL,
    repeats_monthly boolean DEFAULT false NOT NULL,
    repeats_annually boolean DEFAULT false NOT NULL,
    repeats_weekly boolean DEFAULT false NOT NULL
);


ALTER TABLE public.outgoings OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16553)
-- Name: outgoings_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.outgoings_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.outgoings_id_seq OWNER TO postgres;

--
-- TOC entry 3367 (class 0 OID 0)
-- Dependencies: 217
-- Name: outgoings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.outgoings_id_seq OWNED BY public.outgoings.id;


--
-- TOC entry 218 (class 1259 OID 16554)
-- Name: savings_and_investments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.savings_and_investments (
    id integer NOT NULL,
    userid integer NOT NULL,
    name character varying NOT NULL,
    amount money NOT NULL,
    note character varying,
    date date NOT NULL,
    repeats_monthly boolean DEFAULT false NOT NULL,
    repeats_annually boolean DEFAULT false NOT NULL,
    repeats_weekly boolean DEFAULT false NOT NULL
);


ALTER TABLE public.savings_and_investments OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16562)
-- Name: savings_and_investments_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.savings_and_investments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.savings_and_investments_id_seq OWNER TO postgres;

--
-- TOC entry 3368 (class 0 OID 0)
-- Dependencies: 219
-- Name: savings_and_investments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.savings_and_investments_id_seq OWNED BY public.savings_and_investments.id;


--
-- TOC entry 220 (class 1259 OID 16563)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying NOT NULL,
    password character varying NOT NULL,
    username character varying NOT NULL,
    active boolean NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16568)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- TOC entry 3369 (class 0 OID 0)
-- Dependencies: 221
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 3188 (class 2604 OID 16569)
-- Name: incomes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.incomes ALTER COLUMN id SET DEFAULT nextval('public.incomes_id_seq'::regclass);


--
-- TOC entry 3192 (class 2604 OID 16570)
-- Name: outgoings id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.outgoings ALTER COLUMN id SET DEFAULT nextval('public.outgoings_id_seq'::regclass);


--
-- TOC entry 3196 (class 2604 OID 16571)
-- Name: savings_and_investments id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.savings_and_investments ALTER COLUMN id SET DEFAULT nextval('public.savings_and_investments_id_seq'::regclass);


--
-- TOC entry 3200 (class 2604 OID 16572)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- TOC entry 3351 (class 0 OID 16536)
-- Dependencies: 214
-- Data for Name: incomes; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.incomes VALUES (4, 0, 'Salary', '£2,306.00', '', '2023-08-28', true, false, false);


--
-- TOC entry 3353 (class 0 OID 16545)
-- Dependencies: 216
-- Data for Name: outgoings; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.outgoings VALUES (1, 0, 'Mortgage', '£400.00', '', '2023-09-16', true, false, false);
INSERT INTO public.outgoings VALUES (2, 0, 'Gas and Electric', '£150.00', '', '2023-08-31', true, false, false);
INSERT INTO public.outgoings VALUES (3, 0, 'Council Tax', '£98.00', '', '2023-08-31', true, false, false);
INSERT INTO public.outgoings VALUES (4, 0, 'Internet', '£37.00', '', '2023-09-18', true, false, false);
INSERT INTO public.outgoings VALUES (5, 0, 'Pet Health Club', '£16.00', '', '2023-08-28', true, false, false);
INSERT INTO public.outgoings VALUES (6, 0, 'Smarty', '£6.00', '', '2023-09-14', true, false, false);
INSERT INTO public.outgoings VALUES (7, 0, 'Spotify', '£11.00', '', '2023-08-14', true, false, false);
INSERT INTO public.outgoings VALUES (8, 0, 'NabuCasa', '£65.00', '', '2023-02-15', false, true, false);
INSERT INTO public.outgoings VALUES (9, 0, 'Food and Household', '£150.00', '', '2023-08-29', true, false, false);
INSERT INTO public.outgoings VALUES (10, 0, 'Petrol', '£100.00', '', '2023-08-28', true, false, false);
INSERT INTO public.outgoings VALUES (11, 0, 'Car MOT', '£42.00', '', '2023-04-01', false, true, false);
INSERT INTO public.outgoings VALUES (12, 0, 'Car Service', '£380.00', '', '2023-04-01', false, true, false);
INSERT INTO public.outgoings VALUES (13, 0, 'Car Tax', '£130.00', '', '2023-04-01', false, true, false);
INSERT INTO public.outgoings VALUES (14, 0, 'Car Insurance', '£400.00', '', '2023-04-01', false, true, false);
INSERT INTO public.outgoings VALUES (15, 0, 'Mothers Day', '£10.00', '', '2023-03-27', false, true, false);
INSERT INTO public.outgoings VALUES (16, 0, 'Dad Birthday Present', '£20.00', '', '2023-05-29', false, true, false);
INSERT INTO public.outgoings VALUES (17, 0, 'Fathers Day', '£10.00', '', '2023-06-19', false, true, false);
INSERT INTO public.outgoings VALUES (18, 0, 'Georges Birthday', '£20.00', '', '2023-07-29', false, true, false);
INSERT INTO public.outgoings VALUES (19, 0, 'Home Insurance', '£200.00', '', '2023-08-06', false, true, false);
INSERT INTO public.outgoings VALUES (20, 0, 'Mums Birthday Present', '£20.00', '', '2023-08-19', false, true, false);
INSERT INTO public.outgoings VALUES (21, 0, 'RAC', '£40.00', '', '2023-07-29', false, true, false);
INSERT INTO public.outgoings VALUES (22, 0, 'Alistair Birthday Present', '£20.00', '', '2023-09-03', false, true, false);
INSERT INTO public.outgoings VALUES (23, 0, 'Google Drive', '£16.00', '', '2023-09-07', false, true, false);
INSERT INTO public.outgoings VALUES (24, 0, 'Emily Birthday Present', '£20.00', '', '2023-10-03', false, true, false);
INSERT INTO public.outgoings VALUES (25, 0, 'Alex Birthday Present', '£20.00', '', '2023-10-13', false, true, false);
INSERT INTO public.outgoings VALUES (26, 0, 'Ellie Birthday Present', '£50.00', '', '2023-12-22', false, true, false);
INSERT INTO public.outgoings VALUES (27, 0, 'Emily Birthday Present', '£20.00', '', '2023-12-25', false, true, false);
INSERT INTO public.outgoings VALUES (28, 0, 'Mum Christmas Present', '£20.00', '', '2023-12-25', false, true, false);
INSERT INTO public.outgoings VALUES (29, 0, 'Dad Christmas Present', '£20.00', '', '2023-12-25', false, true, false);
INSERT INTO public.outgoings VALUES (30, 0, 'Ellie Christmas Present', '£50.00', '', '2023-12-25', false, true, false);
INSERT INTO public.outgoings VALUES (31, 0, 'George Christmas Present', '£20.00', '', '2023-12-25', false, true, false);
INSERT INTO public.outgoings VALUES (32, 0, 'Alistair Christmas Present', '£20.00', '', '2023-12-25', false, true, false);
INSERT INTO public.outgoings VALUES (33, 0, 'Alex Christmas Present', '£20.00', '', '2023-12-25', false, true, false);


--
-- TOC entry 3355 (class 0 OID 16554)
-- Dependencies: 218
-- Data for Name: savings_and_investments; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.savings_and_investments VALUES (1, 0, 'General', '£100.00', '', '2023-08-29', true, false, false);
INSERT INTO public.savings_and_investments VALUES (2, 0, 'Emergencies', '£250.00', '', '2023-08-29', true, false, false);
INSERT INTO public.savings_and_investments VALUES (3, 0, 'Holiday', '£100.00', '', '2023-08-29', true, false, false);
INSERT INTO public.savings_and_investments VALUES (4, 0, 'Vanguard', '£350.00', '', '2023-09-18', true, false, false);


--
-- TOC entry 3357 (class 0 OID 16563)
-- Dependencies: 220
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3370 (class 0 OID 0)
-- Dependencies: 215
-- Name: incomes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.incomes_id_seq', 14, true);


--
-- TOC entry 3371 (class 0 OID 0)
-- Dependencies: 217
-- Name: outgoings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.outgoings_id_seq', 33, true);


--
-- TOC entry 3372 (class 0 OID 0)
-- Dependencies: 219
-- Name: savings_and_investments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.savings_and_investments_id_seq', 4, true);


--
-- TOC entry 3373 (class 0 OID 0)
-- Dependencies: 221
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- TOC entry 3202 (class 2606 OID 16574)
-- Name: incomes incomes_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.incomes
    ADD CONSTRAINT incomes_pk PRIMARY KEY (id);


--
-- TOC entry 3204 (class 2606 OID 16576)
-- Name: outgoings outgoings_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.outgoings
    ADD CONSTRAINT outgoings_pk PRIMARY KEY (id);


--
-- TOC entry 3206 (class 2606 OID 16578)
-- Name: savings_and_investments savings_and_investments_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.savings_and_investments
    ADD CONSTRAINT savings_and_investments_pk PRIMARY KEY (id);


--
-- TOC entry 3208 (class 2606 OID 16580)
-- Name: users users_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pk PRIMARY KEY (id);


--
-- TOC entry 3365 (class 0 OID 0)
-- Dependencies: 5
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pg_database_owner
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;


-- Completed on 2023-08-22 12:05:33

--
-- PostgreSQL database dump complete
--

