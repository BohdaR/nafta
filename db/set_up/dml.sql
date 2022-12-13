INSERT INTO countries (name)
VALUES ('China'),
       ('Ukraine'),
       ('Poland'),
       ('Canada'),
       ('Spain'),
       ('Germany');

INSERT INTO brands (name, country_id)
VALUES ('Buromax', 9),
       ('Kite', 13),
       ('Cool For School', 13),
       ('Galeria Papieru', 10);

INSERT INTO binding_types (name)
VALUES ('Glue block'),
       ('bracket'),
       ('Thread-glue');

INSERT INTO paper_formats (name)
VALUES ('A5'),
       ('A4'),
       ('A3'),
       ('A2'),
       ('A1'),
       ('A0');

INSERT INTO paper_types (name)
VALUES ('Corrugated board'),
       ('Design paper'),
       ('Design paper'),
       ('Colored cardboard'),
       ('Colored paper');

INSERT INTO papers (name, description, pieces, paper_type_id, density, paper_format_id, brand_id, binding_type_id,
                    country_id)
VALUES ('A4 color paper, 80g/m2, PASTEL, yellow, 50 sheets', 'Yellow paper. 50 pieces. Can be used at school.', '50',
        '7', '80', '8', '16', '5', '9'),
       ('Set of colored cardboard A4, 80g/m2, DARK+PASTEL', 'Set of colored cardboard A4, 80g/m2, DARK+PASTEL', '80',
        '6', '80', '8', '16', '7', '9'),
       ('Corrugated cardboard colored metallized Hot Wheels HW14-258K',
        'Corrugated cardboard colored metallized Hot Wheels HW14-258K', '5', '3', '200', '8', '17', '6', '10'),
       ('Colored cardboard double-sided Cool For School 230',
        'There are 10 pieces of colored cardboard in the Cool For School set.' ||
        ' The child will look at the package with pleasure and interest.' ||
        ' From colored cardboard, the kid will be able to create various applications,' ||
        ' paper crafts, origami.  Cool For School products have passed all stages of testing ' ||
        'and certification in accordance with the quality and safety standards provided in the European Union.',
        '10', '6', '230', '8', '18', '6', '13'),
       ('Colored cardboard one-sided',
        'There are 10 pieces of colored cardboard in the Cool For School set.' ||
        '  The child will look at the package with pleasure and interest.' ||
        ' From colored cardboard, the kid will be able to create various applications, paper crafts, origami.' ||
        '  Cool For School products have passed all stages of testing and certification in accordance with the' ||
        ' quality and safety standards provided in the European Union.',
        '10', '7', '230', '7', '18', '5', '13')
