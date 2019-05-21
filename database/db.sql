--
-- PostgreSQL database dump
--

-- Dumped from database version 10.4
-- Dumped by pg_dump version 11.3

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

SET default_with_oids = false;

--
-- Name: orders; Type: TABLE; Schema: public; Owner: ialmoqre_ibrahim
--

CREATE TABLE public.orders (
    id bigint NOT NULL,
    fullname character varying(60),
    email character varying(60),
    phone character varying(20),
    details character varying(2000),
    "timestamp" character varying(30)
);


ALTER TABLE public.orders OWNER TO ialmoqre_ibrahim;

--
-- Name: orders_id_seq; Type: SEQUENCE; Schema: public; Owner: ialmoqre_ibrahim
--

CREATE SEQUENCE public.orders_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orders_id_seq OWNER TO ialmoqre_ibrahim;

--
-- Name: orders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ialmoqre_ibrahim
--

ALTER SEQUENCE public.orders_id_seq OWNED BY public.orders.id;


--
-- Name: photographers; Type: TABLE; Schema: public; Owner: ialmoqre_ibrahim
--

CREATE TABLE public.photographers (
    id bigint NOT NULL,
    fullname character varying(60),
    email character varying(60),
    phone character varying(20),
    "timestamp" character varying(30)
);


ALTER TABLE public.photographers OWNER TO ialmoqre_ibrahim;

--
-- Name: photographers_id_seq; Type: SEQUENCE; Schema: public; Owner: ialmoqre_ibrahim
--

CREATE SEQUENCE public.photographers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.photographers_id_seq OWNER TO ialmoqre_ibrahim;

--
-- Name: photographers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ialmoqre_ibrahim
--

ALTER SEQUENCE public.photographers_id_seq OWNED BY public.photographers.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: ialmoqre_ibrahim
--

CREATE TABLE public.users (
    id bigint NOT NULL,
    username character varying(30) NOT NULL,
    password character varying(30) NOT NULL
);


ALTER TABLE public.users OWNER TO ialmoqre_ibrahim;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: ialmoqre_ibrahim
--

CREATE SEQUENCE public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO ialmoqre_ibrahim;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ialmoqre_ibrahim
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: orders id; Type: DEFAULT; Schema: public; Owner: ialmoqre_ibrahim
--

ALTER TABLE ONLY public.orders ALTER COLUMN id SET DEFAULT nextval('public.orders_id_seq'::regclass);


--
-- Name: photographers id; Type: DEFAULT; Schema: public; Owner: ialmoqre_ibrahim
--

ALTER TABLE ONLY public.photographers ALTER COLUMN id SET DEFAULT nextval('public.photographers_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: ialmoqre_ibrahim
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: ialmoqre_ibrahim
--

COPY public.orders (id, fullname, email, phone, details, "timestamp") FROM stdin;
\.


--
-- Data for Name: photographers; Type: TABLE DATA; Schema: public; Owner: ialmoqre_ibrahim
--

COPY public.photographers (id, fullname, email, phone, "timestamp") FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: ialmoqre_ibrahim
--

COPY public.users (id, username, password) FROM stdin;
\.


--
-- Name: orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ialmoqre_ibrahim
--

SELECT pg_catalog.setval('public.orders_id_seq', 1, false);


--
-- Name: photographers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ialmoqre_ibrahim
--

SELECT pg_catalog.setval('public.photographers_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ialmoqre_ibrahim
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: orders idx_17318_primary; Type: CONSTRAINT; Schema: public; Owner: ialmoqre_ibrahim
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT idx_17318_primary PRIMARY KEY (id);


--
-- Name: photographers idx_17327_primary; Type: CONSTRAINT; Schema: public; Owner: ialmoqre_ibrahim
--

ALTER TABLE ONLY public.photographers
    ADD CONSTRAINT idx_17327_primary PRIMARY KEY (id);


--
-- Name: users idx_17333_primary; Type: CONSTRAINT; Schema: public; Owner: ialmoqre_ibrahim
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT idx_17333_primary PRIMARY KEY (id);


--
-- Name: idx_17318_id; Type: INDEX; Schema: public; Owner: ialmoqre_ibrahim
--

CREATE UNIQUE INDEX idx_17318_id ON public.orders USING btree (id);


--
-- Name: idx_17327_id; Type: INDEX; Schema: public; Owner: ialmoqre_ibrahim
--

CREATE UNIQUE INDEX idx_17327_id ON public.photographers USING btree (id);


--
-- Name: idx_17333_id; Type: INDEX; Schema: public; Owner: ialmoqre_ibrahim
--

CREATE UNIQUE INDEX idx_17333_id ON public.users USING btree (id);


--
-- Name: idx_17333_username; Type: INDEX; Schema: public; Owner: ialmoqre_ibrahim
--

CREATE UNIQUE INDEX idx_17333_username ON public.users USING btree (username);


--
-- PostgreSQL database dump complete
--

