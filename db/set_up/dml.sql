INSERT INTO paper_types (name)
VALUES ('Кольоровий папір');
INSERT INTO paper_formats (name)
VALUES ('A4');
INSERT INTO countries (name)
VALUES ('Ukraine');
INSERT INTO binding_types (name)
VALUES ('На скобі');
INSERT INTO brands (name, country_id)
VALUES ('Buromax', 1);
INSERT INTO papers (name, description, pieces, paper_type_id, density, paper_format_id, brand_id, binding_type_id,
                    manufacture_country_id)
VALUES ('Кольоровий папів двохсторонній', 'Some paper', 4, 1, 45, 1, 1, 1, 1);
