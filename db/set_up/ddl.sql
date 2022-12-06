CREATE TABLE paper_types
(
    id   serial PRIMARY KEY,
    name varchar(60) NOT NULL
);

CREATE TABLE paper_formats
(
    id   serial PRIMARY KEY,
    name varchar(60) NOT NULL
);

CREATE TABLE binding_types
(
    id   serial PRIMARY KEY,
    name varchar(60) NOT NULL
);

CREATE TABLE countries
(
    id   serial PRIMARY KEY,
    name varchar(30) NOT NULL
);

CREATE TABLE brands
(
    id         serial PRIMARY KEY,
    name       varchar(60) NOT NULL,
    country_id integer references countries
);

CREATE TABLE papers
(
    id                  serial PRIMARY KEY,
    name                varchar(60) NOT NULL,
    description         text        NOT NULL,
    pieces              integer     NOT NULL,
    paper_type_id       integer references paper_types,
    density             float4      NOT NULL,
    paper_format_id     integer references paper_formats,
    brand_id            integer references brands,
    binding_type_id     integer references binding_types,
    manufacture_country_id integer references countries,
    status              varchar(30) default 'new'
);

CREATE TABLE colors
(
    id   serial PRIMARY KEY,
    name varchar(20) NOT NULL
);

CREATE TABLE papers_colors
(
    paper_id integer references papers,
    color_id integer references colors
);
