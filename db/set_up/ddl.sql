CREATE TABLE IF NOT EXISTS paper_types
(
    id   serial PRIMARY KEY,
    name varchar(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS paper_formats
(
    id   serial PRIMARY KEY,
    name varchar(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS binding_types
(
    id   serial PRIMARY KEY,
    name varchar(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS countries
(
    id   serial PRIMARY KEY,
    name varchar(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS brands
(
    id         serial PRIMARY KEY,
    name       varchar(60) NOT NULL,
    country_id integer references countries
);

CREATE TABLE IF NOT EXISTS papers
(
    id              serial PRIMARY KEY,
    name            varchar(60) NOT NULL,
    description     text        NOT NULL,
    pieces          integer     NOT NULL,
    paper_type_id   integer references paper_types,
    density         float4      NOT NULL,
    paper_format_id integer references paper_formats,
    brand_id        integer references brands,
    binding_type_id integer references binding_types,
    country_id      integer references countries
);
