--
-- PostgreSQL database cluster dump
--

-- Started on 2023-08-22 10:26:46

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS;

--
-- User Configurations
--








--
-- Databases
--

--
-- Database "template1" dump
--

\connect template1

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

-- Started on 2023-08-22 10:26:46

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

-- Completed on 2023-08-22 10:26:46

--
-- PostgreSQL database dump complete
--

--
-- Database "BudgetApp" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

-- Started on 2023-08-22 10:26:46

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
-- TOC entry 3364 (class 1262 OID 32768)
-- Name: BudgetApp; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "BudgetApp" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United Kingdom.1252';


ALTER DATABASE "BudgetApp" OWNER TO postgres;

\connect "BudgetApp"

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 217 (class 1259 OID 32777)
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
-- TOC entry 216 (class 1259 OID 32776)
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
-- TOC entry 3365 (class 0 OID 0)
-- Dependencies: 216
-- Name: incomes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.incomes_id_seq OWNED BY public.incomes.id;


--
-- TOC entry 219 (class 1259 OID 32791)
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
-- TOC entry 218 (class 1259 OID 32790)
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
-- TOC entry 3366 (class 0 OID 0)
-- Dependencies: 218
-- Name: outgoings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.outgoings_id_seq OWNED BY public.outgoings.id;


--
-- TOC entry 221 (class 1259 OID 32803)
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
-- TOC entry 220 (class 1259 OID 32802)
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
-- TOC entry 3367 (class 0 OID 0)
-- Dependencies: 220
-- Name: savings_and_investments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.savings_and_investments_id_seq OWNED BY public.savings_and_investments.id;


--
-- TOC entry 215 (class 1259 OID 32770)
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
-- TOC entry 214 (class 1259 OID 32769)
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
-- TOC entry 3368 (class 0 OID 0)
-- Dependencies: 214
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 3189 (class 2604 OID 32780)
-- Name: incomes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.incomes ALTER COLUMN id SET DEFAULT nextval('public.incomes_id_seq'::regclass);


--
-- TOC entry 3193 (class 2604 OID 32794)
-- Name: outgoings id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.outgoings ALTER COLUMN id SET DEFAULT nextval('public.outgoings_id_seq'::regclass);


--
-- TOC entry 3197 (class 2604 OID 32806)
-- Name: savings_and_investments id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.savings_and_investments ALTER COLUMN id SET DEFAULT nextval('public.savings_and_investments_id_seq'::regclass);


--
-- TOC entry 3188 (class 2604 OID 32773)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- TOC entry 3354 (class 0 OID 32777)
-- Dependencies: 217
-- Data for Name: incomes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.incomes (id, userid, name, amount, note, date, repeats_monthly, repeats_annually, repeats_weekly) FROM stdin;
1	0	Salary	£2,300.00	123	2023-08-28	t	f	f
2	0	Pleep Ploop	£78.00	Boglin froglin debit payment	2023-08-20	t	f	f
\.


--
-- TOC entry 3356 (class 0 OID 32791)
-- Dependencies: 219
-- Data for Name: outgoings; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.outgoings (id, userid, name, amount, note, date, repeats_monthly, repeats_annually, repeats_weekly) FROM stdin;
\.


--
-- TOC entry 3358 (class 0 OID 32803)
-- Dependencies: 221
-- Data for Name: savings_and_investments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.savings_and_investments (id, userid, name, amount, note, date, repeats_monthly, repeats_annually, repeats_weekly) FROM stdin;
\.


--
-- TOC entry 3352 (class 0 OID 32770)
-- Dependencies: 215
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, email, password, username, active) FROM stdin;
\.


--
-- TOC entry 3369 (class 0 OID 0)
-- Dependencies: 216
-- Name: incomes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.incomes_id_seq', 2, true);


--
-- TOC entry 3370 (class 0 OID 0)
-- Dependencies: 218
-- Name: outgoings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.outgoings_id_seq', 1, false);


--
-- TOC entry 3371 (class 0 OID 0)
-- Dependencies: 220
-- Name: savings_and_investments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.savings_and_investments_id_seq', 1, false);


--
-- TOC entry 3372 (class 0 OID 0)
-- Dependencies: 214
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- TOC entry 3204 (class 2606 OID 32787)
-- Name: incomes incomes_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.incomes
    ADD CONSTRAINT incomes_pk PRIMARY KEY (id);


--
-- TOC entry 3206 (class 2606 OID 32801)
-- Name: outgoings outgoings_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.outgoings
    ADD CONSTRAINT outgoings_pk PRIMARY KEY (id);


--
-- TOC entry 3208 (class 2606 OID 32813)
-- Name: savings_and_investments savings_and_investments_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.savings_and_investments
    ADD CONSTRAINT savings_and_investments_pk PRIMARY KEY (id);


--
-- TOC entry 3202 (class 2606 OID 32789)
-- Name: users users_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pk PRIMARY KEY (id);


-- Completed on 2023-08-22 10:26:47

--
-- PostgreSQL database dump complete
--

--
-- Database "GroupMeetOrganiser" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

-- Started on 2023-08-22 10:26:47

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
-- TOC entry 3330 (class 1262 OID 24614)
-- Name: GroupMeetOrganiser; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "GroupMeetOrganiser" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United Kingdom.1252';


ALTER DATABASE "GroupMeetOrganiser" OWNER TO postgres;

\connect "GroupMeetOrganiser"

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
-- TOC entry 6 (class 2615 OID 24615)
-- Name: entries; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA entries;


ALTER SCHEMA entries OWNER TO postgres;

--
-- TOC entry 7 (class 2615 OID 24616)
-- Name: users; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA users;


ALTER SCHEMA users OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 216 (class 1259 OID 24617)
-- Name: entries; Type: TABLE; Schema: entries; Owner: postgres
--

CREATE TABLE entries.entries (
    id uuid DEFAULT gen_random_uuid() NOT NULL,
    user_id uuid NOT NULL,
    date date NOT NULL,
    available boolean DEFAULT false NOT NULL
);


ALTER TABLE entries.entries OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 24622)
-- Name: users; Type: TABLE; Schema: users; Owner: postgres
--

CREATE TABLE users.users (
    id uuid DEFAULT gen_random_uuid() NOT NULL,
    name character varying NOT NULL,
    group_code character varying NOT NULL
);


ALTER TABLE users.users OWNER TO postgres;

--
-- TOC entry 3323 (class 0 OID 24617)
-- Dependencies: 216
-- Data for Name: entries; Type: TABLE DATA; Schema: entries; Owner: postgres
--

COPY entries.entries (id, user_id, date, available) FROM stdin;
\.


--
-- TOC entry 3324 (class 0 OID 24622)
-- Dependencies: 217
-- Data for Name: users; Type: TABLE DATA; Schema: users; Owner: postgres
--

COPY users.users (id, name, group_code) FROM stdin;
\.


-- Completed on 2023-08-22 10:26:47

--
-- PostgreSQL database dump complete
--

-- Completed on 2023-08-22 10:26:47

--
-- PostgreSQL database cluster dump complete
--

