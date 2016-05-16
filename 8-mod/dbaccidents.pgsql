--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: accidents; Type: TABLE; Schema: public; Owner: zemoso; Tablespace: 
--

CREATE TABLE accidents (
    state character varying,
    eqto8 numeric,
    eqto10 numeric,
    mrthn10 numeric,
    ntknwn numeric,
    total numeric
);


ALTER TABLE public.accidents OWNER TO zemoso;

--
-- Data for Name: accidents; Type: TABLE DATA; Schema: public; Owner: zemoso
--

COPY accidents (state, eqto8, eqto10, mrthn10, ntknwn, total) FROM stdin;
Andhra Pradesh	6425	8657	8144	19298	42524
Arunachal Pradesh	88	76	87	0	251
Assam	0	0	0	6535	6535
Bihar	2660	3938	3722	0	10320
Chhattisgarh	2888	7052	3571	0	13511
Goa	616	1512	2184	0	4312
Gujarat	4864	7864	7132	8089	27949
Haryana	3365	2588	4112	0	10065
Himachal Pradesh	276	626	977	1020	2899
Jammu and Kashmir	1557	618	434	4100	6709
Jharkhand	1128	701	1037	2845	5711
Karnataka	11167	14715	18566	0	44448
Kerala	5580	13271	17323	0	36174
Madhya Pradesh	15630	16226	19354	0	51210
Maharashtra	4117	5350	10538	46311	66316
Manipur	147	453	171	0	771
Meghalaya	210	154	119	0	483
Mizoram	27	58	25	0	110
Nagaland	11	13	18	0	42
Odisha	1881	3120	4284	0	9285
Punjab	1378	2231	1825	907	6341
Rajasthan	5534	5895	5475	6065	22969
Sikkim	6	144	8	0	158
Tamil Nadu	8424	18826	29871	10636	67757
Tripura	290	376	222	0	888
Uttarakhand	318	305	456	393	1472
Uttar Pradesh	8520	10457	10995	0	29972
West Bengal	1494	1311	974	8511	12290
Andaman and Nicobar Islands	18	104	114	0	236
Chandigarh	112	39	210	58	419
Dadra and Nagar Haveli	40	20	17	8	85
Daman and Diu	11	6	8	25	50
Delhi	0	0	0	6937	6937
Lakshadweep	0	0	0	3	3
Puducherry	154	668	359	0	1181
All India	88936	127374	152332	121741	490383
\.


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

