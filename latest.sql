--
-- PostgreSQL database dump
--

-- Dumped from database version 12.5 (Ubuntu 12.5-1.pgdg16.04+1)
-- Dumped by pg_dump version 12.1

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
-- Name: users; Type: TABLE; Schema: public; Owner: wmfjnbbwgxwzyn
--

CREATE TABLE "public"."users" (
    "id" integer NOT NULL,
    "username" character varying(25) NOT NULL,
    "hashed_pswd" "text" NOT NULL
);


ALTER TABLE public.users OWNER TO wmfjnbbwgxwzyn;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: wmfjnbbwgxwzyn
--

CREATE SEQUENCE "public"."users_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO wmfjnbbwgxwzyn;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wmfjnbbwgxwzyn
--

ALTER SEQUENCE "public"."users_id_seq" OWNED BY "public"."users"."id";


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: wmfjnbbwgxwzyn
--

ALTER TABLE ONLY "public"."users" ALTER COLUMN "id" SET DEFAULT "nextval"('"public"."users_id_seq"'::"regclass");


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: wmfjnbbwgxwzyn
--

COPY "public"."users" ("id", "username", "hashed_pswd") FROM stdin;
1	Dimas	$pbkdf2-sha256$29000$QmgNIWRMqVXqXSvFWEvp3Q$LiRfyCo9fbvznv1BMUzuYSZo8KOVvbna.ZXcjcKLBFI
2	Refa	$pbkdf2-sha256$29000$bE2J8T4H4NzbG.N8L.Xc.w$0sZ/sbBL/CmD8dZ0If1liB0NhrBCNWCaiRi2w2zH8xM
\.


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wmfjnbbwgxwzyn
--

SELECT pg_catalog.setval('"public"."users_id_seq"', 2, true);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: wmfjnbbwgxwzyn
--

ALTER TABLE ONLY "public"."users"
    ADD CONSTRAINT "users_pkey" PRIMARY KEY ("id");


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: wmfjnbbwgxwzyn
--

ALTER TABLE ONLY "public"."users"
    ADD CONSTRAINT "users_username_key" UNIQUE ("username");


--
-- PostgreSQL database dump complete
--

