CREATE DATABASE IF NOT EXISTS vsc_erp;
USE vsc_erp;

--
-- Master Data Tables (Lookup Tables)
--

CREATE TABLE masters_master_role (
    id bigint NOT NULL AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY name (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE masters_master_pay_grade_level (
    id bigint NOT NULL AUTO_INCREMENT,
    level varchar(10) NOT NULL,
    base_salary decimal(10,2) NOT NULL,
    description longtext,
    role_id bigint NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY Masters_master_pay_grade_level_role_id_level_3194a9d6_uniq (role_id, level),
    CONSTRAINT Masters_master_pay_g_role_id_691cc7b2_fk_Masters_m FOREIGN KEY (role_id)
        REFERENCES masters_master_role (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE masters_master_expertise_area (
    id bigint NOT NULL AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    description longtext,
    role_id bigint NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY name (name),
    KEY Masters_master_exper_role_id_82dc56c3_fk_Masters_m (role_id),
    CONSTRAINT Masters_master_exper_role_id_82dc56c3_fk_Masters_m FOREIGN KEY (role_id)
        REFERENCES masters_master_role (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE masters_master_vehicle_brand (
    id bigint NOT NULL AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY name (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE masters_master_vehicle_category (
    id bigint NOT NULL AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    licence_type varchar(20) NOT NULL,
    wheels smallint unsigned NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY name (name),
    CONSTRAINT masters_master_vehicle_category_chk_1 CHECK ((wheels >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE masters_master_vehicle_model (
    id bigint NOT NULL AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    engine varchar(50) NOT NULL,
    weight int unsigned DEFAULT NULL,
    description longtext NOT NULL,
    brand_id bigint NOT NULL,
    category_id bigint NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY Masters_master_vehicle_model_brand_id_name_c8eaf8de_uniq (brand_id, name),
    KEY Masters_master_vehic_category_id_46c005b1_fk_Masters_m (category_id),
    CONSTRAINT Masters_master_vehic_brand_id_2c81c645_fk_Masters_m FOREIGN KEY (brand_id)
        REFERENCES masters_master_vehicle_brand (id),
    CONSTRAINT Masters_master_vehic_category_id_46c005b1_fk_Masters_m FOREIGN KEY (category_id)
        REFERENCES masters_master_vehicle_category (id),
    CONSTRAINT masters_master_vehicle_model_chk_1 CHECK ((weight >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE masters_master_spare_part_type (
    id bigint NOT NULL AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    description longtext,
    PRIMARY KEY (id),
    UNIQUE KEY name (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- User and Actor Tables (Users, Customers, Employees)
--

CREATE TABLE auth_user (
    id int NOT NULL AUTO_INCREMENT,
    password varchar(128) NOT NULL,
    last_login datetime(6) DEFAULT NULL,
    is_superuser tinyint(1) NOT NULL,
    username varchar(150) NOT NULL,
    first_name varchar(150) NOT NULL,
    last_name varchar(150) NOT NULL,
    email varchar(254) NOT NULL,
    is_staff tinyint(1) NOT NULL,
    is_active tinyint(1) NOT NULL,
    date_joined datetime(6) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY username (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE core_customer (
    user_id int NOT NULL,
    mobile_number varchar(128) NOT NULL,
    address longtext,
    description longtext,
    PRIMARY KEY (user_id),
    CONSTRAINT CORE_customer_user_id_50d0b9cd_fk_auth_user_id FOREIGN KEY (user_id)
        REFERENCES auth_user (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE core_employee (
    id bigint NOT NULL AUTO_INCREMENT,
    DOB date NOT NULL,
    Address longtext NOT NULL,
    mobile_number varchar(128) NOT NULL,
    shift varchar(10) DEFAULT NULL,
    pay_grade_id bigint DEFAULT NULL,
    role_id bigint DEFAULT NULL,
    user_id int NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY user_id (user_id),
    KEY CORE_employee_role_id_d059113d_fk_Masters_master_role_id (role_id),
    KEY CORE_employee_pay_grade_id_dcce3e6e (pay_grade_id),
    CONSTRAINT CORE_employee_pay_grade_id_dcce3e6e_fk_Masters_m FOREIGN KEY (pay_grade_id)
        REFERENCES masters_master_pay_grade_level (id),
    CONSTRAINT CORE_employee_role_id_d059113d_fk_Masters_master_role_id FOREIGN KEY (role_id)
        REFERENCES masters_master_role (id),
    CONSTRAINT CORE_employee_user_id_b261e990_fk_auth_user_id FOREIGN KEY (user_id)
        REFERENCES auth_user (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE core_accountant (
    employee_id bigint NOT NULL,
    education longtext,
    PRIMARY KEY (employee_id),
    CONSTRAINT CORE_accountant_employee_id_1040ddd2_fk_CORE_employee_id FOREIGN KEY (employee_id)
        REFERENCES core_employee (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE core_advisor (
    employee_id bigint NOT NULL,
    education_desc longtext,
    PRIMARY KEY (employee_id),
    CONSTRAINT CORE_advisor_employee_id_c11f806c_fk_CORE_employee_id FOREIGN KEY (employee_id)
        REFERENCES core_employee (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE core_cashier (
    employee_id bigint NOT NULL,
    counter_number varchar(10) NOT NULL,
    PRIMARY KEY (employee_id),
    CONSTRAINT CORE_cashier_employee_id_82ba154b_fk_CORE_employee_id FOREIGN KEY (employee_id)
        REFERENCES core_employee (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE core_mechanic (
    employee_id bigint NOT NULL,
    years_of_experience smallint unsigned NOT NULL,
    certifications longtext,
    expertise_area_id bigint NOT NULL,
    PRIMARY KEY (employee_id),
    KEY CORE_mechanic_expertise_area_id_5a7f3546_fk_Masters_m (expertise_area_id),
    CONSTRAINT CORE_mechanic_employee_id_45c7346e_fk_CORE_employee_id FOREIGN KEY (employee_id)
        REFERENCES core_employee (id),
    CONSTRAINT CORE_mechanic_expertise_area_id_5a7f3546_fk_Masters_m FOREIGN KEY (expertise_area_id)
        REFERENCES masters_master_expertise_area (id),
    CONSTRAINT core_mechanic_chk_1 CHECK ((years_of_experience >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Core Business Object Tables (Vehicles, Parts)
--

CREATE TABLE core_vehicle (
    id bigint NOT NULL AUTO_INCREMENT,
    registration_number varchar(20) NOT NULL,
    chassis_number varchar(17) NOT NULL,
    year smallint unsigned NOT NULL,
    description longtext NOT NULL,
    customer_id int NOT NULL,
    model_id bigint NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY registration_number (registration_number),
    UNIQUE KEY chassis_number (chassis_number),
    KEY CORE_vehicle_customer_id_370e1bb0_fk_CORE_customer_user_id (customer_id),
    KEY CORE_vehicle_model_id_79d8b126_fk_Masters_m (model_id),
    CONSTRAINT CORE_vehicle_customer_id_370e1bb0_fk_CORE_customer_user_id FOREIGN KEY (customer_id)
        REFERENCES core_customer (user_id),
    CONSTRAINT CORE_vehicle_model_id_79d8b126_fk_Masters_m FOREIGN KEY (model_id)
        REFERENCES masters_master_vehicle_model (id),
    CONSTRAINT core_vehicle_chk_1 CHECK ((year >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE core_sparepart (
    id bigint NOT NULL AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    quantity_in_stock int unsigned NOT NULL,
    price decimal(10,2) NOT NULL,
    type_id bigint DEFAULT NULL,
    vehicle_model_id bigint NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY CORE_sparepart_vehicle_model_id_name_32caaead_uniq (vehicle_model_id, name),
    KEY CORE_sparepart_type_id_60c590bf_fk_Masters_m (type_id),
    CONSTRAINT CORE_sparepart_type_id_60c590bf_fk_Masters_m FOREIGN KEY (type_id)
        REFERENCES masters_master_spare_part_type (id),
    CONSTRAINT CORE_sparepart_vehicle_model_id_9af94d87_fk_Masters_m FOREIGN KEY (vehicle_model_id)
        REFERENCES masters_master_vehicle_model (id),
    CONSTRAINT core_sparepart_chk_1 CHECK ((quantity_in_stock >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Transactional Tables (Services, Invoices)
--

CREATE TABLE core_service (
    id bigint NOT NULL AUTO_INCREMENT,
    status varchar(20) NOT NULL,
    description_of_service longtext NOT NULL,
    labor_cost decimal(10,2) NOT NULL,
    service_date datetime(6) NOT NULL,
    customer_id int NOT NULL,
    vehicle_id bigint NOT NULL,
    mechanic_id bigint DEFAULT NULL,
    PRIMARY KEY (id),
    KEY CORE_service_vehicle_id_79f35b9e_fk_CORE_vehicle_id (vehicle_id),
    KEY CORE_service_mechanic_id_9b8019d7_fk_CORE_mechanic_employee_id (mechanic_id),
    KEY CORE_service_customer_id_64546910_fk_CORE_customer_user_id (customer_id),
    CONSTRAINT CORE_service_customer_id_64546910_fk_CORE_customer_user_id FOREIGN KEY (customer_id)
        REFERENCES core_customer (user_id),
    CONSTRAINT CORE_service_mechanic_id_9b8019d7_fk_CORE_mechanic_employee_id FOREIGN KEY (mechanic_id)
        REFERENCES core_mechanic (employee_id),
    CONSTRAINT CORE_service_vehicle_id_79f35b9e_fk_CORE_vehicle_id FOREIGN KEY (vehicle_id)
        REFERENCES core_vehicle (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE core_servicepart (
    id bigint NOT NULL AUTO_INCREMENT,
    quantity int unsigned NOT NULL,
    unit_price decimal(10,2) NOT NULL,
    service_id bigint NOT NULL,
    part_id bigint NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY CORE_servicepart_service_id_part_id_d7a69a0e_uniq (service_id, part_id),
    KEY CORE_servicepart_part_id_4a1c2323_fk_CORE_sparepart_id (part_id),
    CONSTRAINT CORE_servicepart_part_id_4a1c2323_fk_CORE_sparepart_id FOREIGN KEY (part_id)
        REFERENCES core_sparepart (id),
    CONSTRAINT CORE_servicepart_service_id_19b7f66e_fk_CORE_service_id FOREIGN KEY (service_id)
        REFERENCES core_service (id),
    CONSTRAINT core_servicepart_chk_1 CHECK ((quantity >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE core_serviceinvoice (
    id bigint NOT NULL AUTO_INCREMENT,
    date datetime(6) NOT NULL,
    amount decimal(10,2) NOT NULL,
    payment_method varchar(10) NOT NULL,
    status varchar(10) NOT NULL,
    service_id bigint NOT NULL,
    cashier_id bigint NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY service_id (service_id),
    KEY CORE_serviceinvoice_cashier_id_41d6c839_fk_CORE_cash (cashier_id),
    CONSTRAINT CORE_serviceinvoice_cashier_id_41d6c839_fk_CORE_cash FOREIGN KEY (cashier_id)
        REFERENCES core_cashier (employee_id),
    CONSTRAINT CORE_serviceinvoice_service_id_068dcbf3_fk_CORE_service_id FOREIGN KEY (service_id)
        REFERENCES core_service (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE core_inventoryinvoice (
    id bigint NOT NULL AUTO_INCREMENT,
    supplier varchar(100) NOT NULL,
    quantity_received int unsigned NOT NULL,
    date datetime(6) NOT NULL,
    cost decimal(10,2) NOT NULL,
    spare_part_id bigint NOT NULL,
    PRIMARY KEY (id),
    KEY CORE_inventoryinvoic_spare_part_id_91069a8a_fk_CORE_spar (spare_part_id),
    CONSTRAINT CORE_inventoryinvoic_spare_part_id_91069a8a_fk_CORE_spar FOREIGN KEY (spare_part_id)
        REFERENCES core_sparepart (id),
    CONSTRAINT core_inventoryinvoice_chk_1 CHECK ((quantity_received >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
