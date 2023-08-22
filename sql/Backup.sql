-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION pg_database_owner;

-- DROP SEQUENCE public.incomes_id_seq;

CREATE SEQUENCE public.incomes_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.outgoings_id_seq;

CREATE SEQUENCE public.outgoings_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.savings_and_investments_id_seq;

CREATE SEQUENCE public.savings_and_investments_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.users_id_seq;

CREATE SEQUENCE public.users_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;-- public.incomes definition

-- Drop table

-- DROP TABLE public.incomes;

CREATE TABLE public.incomes (
	id serial4 NOT NULL,
	user_id int4 NOT NULL,
	"name" varchar NOT NULL,
	amount int4 NOT NULL,
	note varchar NULL,
	start_date date NOT NULL,
	repeats_monthly bool NOT NULL DEFAULT false,
	repeats_annually bool NOT NULL DEFAULT false,
	repeats_weekly bool NOT NULL DEFAULT false,
	end_date date NULL,
	CONSTRAINT incomes_pk PRIMARY KEY (id)
);


-- public.outgoings definition

-- Drop table

-- DROP TABLE public.outgoings;

CREATE TABLE public.outgoings (
	id serial4 NOT NULL,
	user_id int4 NOT NULL,
	"name" varchar NOT NULL,
	amount int4 NOT NULL,
	note varchar NULL,
	start_date date NOT NULL,
	repeats_monthly bool NOT NULL DEFAULT false,
	repeats_annually bool NOT NULL DEFAULT false,
	repeats_weekly bool NOT NULL DEFAULT false,
	end_date date NULL,
	CONSTRAINT outgoings_pk PRIMARY KEY (id)
);


-- public.savings_and_investments definition

-- Drop table

-- DROP TABLE public.savings_and_investments;

CREATE TABLE public.savings_and_investments (
	id serial4 NOT NULL,
	user_id int4 NOT NULL,
	"name" varchar NOT NULL,
	amount int4 NOT NULL,
	note varchar NULL,
	start_date date NOT NULL,
	repeats_monthly bool NOT NULL DEFAULT false,
	repeats_annually bool NOT NULL DEFAULT false,
	repeats_weekly bool NOT NULL DEFAULT false,
	end_date date NULL,
	CONSTRAINT savings_and_investments_pk PRIMARY KEY (id)
);


-- public.users definition

-- Drop table

-- DROP TABLE public.users;

CREATE TABLE public.users (
	id serial4 NOT NULL,
	email varchar NOT NULL,
	"password" varchar NOT NULL,
	username varchar NOT NULL,
	active bool NOT NULL,
	CONSTRAINT users_pk PRIMARY KEY (id)
);
