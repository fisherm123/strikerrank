PGDMP                  
    {            worldsoccer    16.1    16.1     W           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            X           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            Y           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            Z           1262    16398    worldsoccer    DATABASE     m   CREATE DATABASE worldsoccer WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';
    DROP DATABASE worldsoccer;
                postgres    false            �            1259    16570    leagues    TABLE     u   CREATE TABLE public.leagues (
    league character varying NOT NULL,
    international character varying NOT NULL
);
    DROP TABLE public.leagues;
       public         heap    postgres    false            T          0    16570    leagues 
   TABLE DATA           8   COPY public.leagues (league, international) FROM stdin;
    public          postgres    false    216   I       �           2606    16576    leagues leagues_raw_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.leagues
    ADD CONSTRAINT leagues_raw_pkey PRIMARY KEY (league);
 B   ALTER TABLE ONLY public.leagues DROP CONSTRAINT leagues_raw_pkey;
       public            postgres    false    216            T   x   x�U�M
�0���)��G��PȢP�7S3ԁ��$��ٔ��}��G	���u6zNYvX�ˈkTgq*g'!��90��f�T�^�^X�0զ�7�0�|��3��:������[ �:�     