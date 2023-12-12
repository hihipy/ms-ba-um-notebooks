-- DROP DATABASE cosmetics;
CREATE DATABASE cosmetics;
USE cosmetics;


-- CREATE TABLES AND INSERT CLEANED VALUES INTO TABLES

-- company
CREATE TABLE company
(
    id           INT PRIMARY KEY,
    company_name VARCHAR(255)
);


-- brand
CREATE TABLE brand
(
    id         INT PRIMARY KEY AUTO_INCREMENT,
    brand_name VARCHAR(255),
    company_id INT,
    CONSTRAINT fk1 FOREIGN KEY (company_id) REFERENCES company (id)
);


-- category
CREATE TABLE category
(
    id            INT PRIMARY KEY,
    category_name VARCHAR(255)
);

-- chemical
CREATE TABLE chemical
(
    id            INT PRIMARY KEY AUTO_INCREMENT,
    chemical_name VARCHAR(255)
);


-- product
CREATE TABLE product
(
    id           INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(255),
    brand_id     INT,
    company_id   INT,
    category_id  INT,
    CONSTRAINT fk2 FOREIGN KEY (brand_id) REFERENCES brand (id),
    CONSTRAINT fk6 FOREIGN KEY (company_id) REFERENCES brand (company_id),
    CONSTRAINT fk3 FOREIGN KEY (category_id) REFERENCES category (id)
);


-- productchemicals
CREATE TABLE productchemicals
(
    id          INT PRIMARY KEY AUTO_INCREMENT,
    chemical_id INT,
    product_id  INT,
    brand_id    INT,
    CONSTRAINT fk4 FOREIGN KEY (chemical_id) REFERENCES chemical (id)
);

-- insert data from orginal csv document
INSERT INTO company(id, company_name)
SELECT DISTINCT CompanyId, CompanyName
FROM Planilha_sem_ttulo;

INSERT INTO brand(brand_name, company_id)
SELECT DISTINCT BrandName, CompanyId
FROM Planilha_sem_ttulo;

INSERT INTO category(id, category_name)
SELECT DISTINCT PrimaryCategoryId, PrimaryCategory
FROM Planilha_sem_ttulo;

INSERT INTO chemical(chemical_name)
SELECT DISTINCT ChemicalName
FROM Planilha_sem_ttulo;

INSERT INTO product(product_name, brand_id, company_id, category_id)
SELECT DISTINCT ProductName, b.id AS BrandId, CompanyId, PrimaryCategoryId
FROM Planilha_sem_ttulo p
         LEFT JOIN brand b ON p.BrandName = b.brand_name AND p.CompanyId = b.company_id;

INSERT INTO productchemicals(chemical_id, product_id, brand_id)
SELECT c.id, a.product_id, b.id AS brand_id
FROM (SELECT DISTINCT p.ChemicalName,
                      p.ProductName,
                      pd.id AS product_id,
                      p.BrandName,
                      p.CompanyId
      FROM Planilha_sem_ttulo p
               LEFT JOIN product pd ON p.ProductName = pd.product_name AND p.CompanyId = pd.company_id) a
         LEFT JOIN chemical c ON a.ChemicalName = c.chemical_name
         LEFT JOIN brand b ON a.BrandName = b.brand_name AND a.CompanyId = b.company_id;


-- VIEW
-- view details of chemical in products
CREATE OR REPLACE VIEW productchemicals_detail AS
SELECT p.id,
       p.chemical_id,
       c.chemical_name,
       p.product_id,
       pd.product_name,
       b.brand_name
FROM productchemicals p
         LEFT JOIN chemical c ON p.chemical_id = c.id
         LEFT JOIN product pd ON p.product_id = pd.id
         LEFT JOIN brand b ON p.brand_id = b.id;

-- view product info
CREATE OR REPLACE VIEW product_detail AS
SELECT p.id,
       p.product_name,
       b.brand_name,
       c.company_name,
       cg.category_name
FROM product p
         LEFT JOIN brand b ON p.brand_id = b.id
         LEFT JOIN company c ON p.company_id = c.id
         LEFT JOIN category cg ON p.category_id = cg.id;

-- PROCEDURE
DELIMITER $$

-- create chemical of product
CREATE PROCEDURE CreateProductChemical(
    IN chemical_id INT,
    IN product_id INT,
    IN brand_id INT
)
BEGIN
    INSERT INTO productchemicals(chemical_id, product_id, brand_id) VALUES (chemical_id, product_id, brand_id);
END $$

call CreateProductChemical(14, 2, 2);

-- create product
DELIMITER $$
CREATE PROCEDURE CreateProduct(
    IN productName VARCHAR(255),
    IN brandId INT,
    IN companyId INT,
    IN categoryId INT
)
BEGIN
    INSERT INTO product(product_name, brand_id, company_id, category_id)
    VALUES (productName, brandId, companyId, categoryId);
END $$

call CreateProduct('XXYYZZ', 1, 4, 111);

-- create category
DELIMITER $$
CREATE PROCEDURE CreateCategory(
    IN categoryId INT,
    IN categoryName VARCHAR(255)
)
BEGIN
    INSERT INTO category(id, category_name) VALUES (categoryId, categoryName);
END $$

call CreateCategory(2, 'Cleaning');


-- update product
DELIMITER $$
CREATE PROCEDURE UpdateProduct(
    IN p_product_id INT,
    IN p_product_name VARCHAR(255),
    IN p_brand_id INT,
    IN p_company_id INT,
    IN p_category_id INT
)
BEGIN
    UPDATE product
    SET product_name = p_product_name,
        brand_id     = p_brand_id,
        company_id   = p_company_id,
        category_id  = p_category_id
    WHERE id = p_product_id;
END $$

CALL UpdateProduct(1, 'ULTRA COLOR RICH EXTRA PLUMP LIPSTICK-ALL SHADES', 2, 338, 18);

--  delete product id
DELIMITER $$
CREATE PROCEDURE DeleteProduct(
    IN p_product_id INT
)
BEGIN
    DELETE
    FROM product
    WHERE id = p_product_id;
END $$

CALL DeleteProduct(1);

-- create company
DELIMITER $$
CREATE PROCEDURE CreateCompanyProcedure(
    IN p_company_name VARCHAR(255),
    OUT p_message VARCHAR(255)
)
BEGIN
    DECLARE v_company_id INT;
    SELECT MAX(id) INTO v_company_id FROM company;

    IF v_company_id IS NULL THEN
        SET v_company_id = 1;
    ELSE
        SET v_company_id = v_company_id + 1;
    END IF;

    INSERT INTO company(id, company_name) VALUES (v_company_id, p_company_name);

    -- Set the success message
    SET p_message = 'Company created successfully!';
END $$

CALL CreateCompanyProcedure('NewCompany', @message);
SELECT @message;

-- Create a new brand and link it to a company
DELIMITER $$
CREATE PROCEDURE CreateBrandProcedure(
    IN p_brand_name VARCHAR(255),
    IN p_company_name VARCHAR(255),
    OUT p_message VARCHAR(255)
)
BEGIN
    DECLARE v_company_id INT;
    DECLARE v_brand_id INT;

    -- Get or create company ID
    SELECT id INTO v_company_id FROM company WHERE company_name = p_company_name LIMIT 1;
    IF v_company_id IS NULL THEN
        SELECT MAX(id) INTO v_company_id FROM company;
        IF v_company_id IS NULL THEN
            SET v_company_id = 1;
        ELSE
            SET v_company_id = v_company_id + 1;
        END IF;

        INSERT INTO company(id, company_name) VALUES (v_company_id, p_company_name);
    END IF;

    -- Get or create brand ID
    SELECT id INTO v_brand_id FROM brand WHERE brand_name = p_brand_name AND company_id = v_company_id LIMIT 1;
    IF v_brand_id IS NULL THEN
        INSERT INTO brand(brand_name, company_id) VALUES (p_brand_name, v_company_id);
        SET v_brand_id = LAST_INSERT_ID();
    END IF;

    SET p_message = 'Brand created successfully!';
END $$

CALL CreateBrandProcedure('NewBrand', 'ExistingCompany', @message);
SELECT @message;


