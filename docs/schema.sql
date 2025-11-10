CREATE DATABASE  IF NOT EXISTS `vsc_erp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `vsc_erp`;
-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: vsc_erp
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add employee',7,'add_employee'),(26,'Can change employee',7,'change_employee'),(27,'Can delete employee',7,'delete_employee'),(28,'Can view employee',7,'view_employee'),(29,'Can add customer',8,'add_customer'),(30,'Can change customer',8,'change_customer'),(31,'Can delete customer',8,'delete_customer'),(32,'Can view customer',8,'view_customer'),(33,'Can add accountant',9,'add_accountant'),(34,'Can change accountant',9,'change_accountant'),(35,'Can delete accountant',9,'delete_accountant'),(36,'Can view accountant',9,'view_accountant'),(37,'Can add advisor',10,'add_advisor'),(38,'Can change advisor',10,'change_advisor'),(39,'Can delete advisor',10,'delete_advisor'),(40,'Can view advisor',10,'view_advisor'),(41,'Can add cashier',11,'add_cashier'),(42,'Can change cashier',11,'change_cashier'),(43,'Can delete cashier',11,'delete_cashier'),(44,'Can view cashier',11,'view_cashier'),(45,'Can add mechanic',12,'add_mechanic'),(46,'Can change mechanic',12,'change_mechanic'),(47,'Can delete mechanic',12,'delete_mechanic'),(48,'Can view mechanic',12,'view_mechanic'),(49,'Can add Service Record',13,'add_service'),(50,'Can change Service Record',13,'change_service'),(51,'Can delete Service Record',13,'delete_service'),(52,'Can view Service Record',13,'view_service'),(53,'Can add Spare Part',14,'add_sparepart'),(54,'Can change Spare Part',14,'change_sparepart'),(55,'Can delete Spare Part',14,'delete_sparepart'),(56,'Can view Spare Part',14,'view_sparepart'),(57,'Can add Part Used in Service',15,'add_servicepart'),(58,'Can change Part Used in Service',15,'change_servicepart'),(59,'Can delete Part Used in Service',15,'delete_servicepart'),(60,'Can view Part Used in Service',15,'view_servicepart'),(61,'Can add Inventory Invoice',16,'add_inventoryinvoice'),(62,'Can change Inventory Invoice',16,'change_inventoryinvoice'),(63,'Can delete Inventory Invoice',16,'delete_inventoryinvoice'),(64,'Can view Inventory Invoice',16,'view_inventoryinvoice'),(65,'Can add vehicle',17,'add_vehicle'),(66,'Can change vehicle',17,'change_vehicle'),(67,'Can delete vehicle',17,'delete_vehicle'),(68,'Can view vehicle',17,'view_vehicle'),(69,'Can add Service Invoice',18,'add_serviceinvoice'),(70,'Can change Service Invoice',18,'change_serviceinvoice'),(71,'Can delete Service Invoice',18,'delete_serviceinvoice'),(72,'Can view Service Invoice',18,'view_serviceinvoice'),(73,'Can add maste r_role',19,'add_master_role'),(74,'Can change maste r_role',19,'change_master_role'),(75,'Can delete maste r_role',19,'delete_master_role'),(76,'Can view maste r_role',19,'view_master_role'),(77,'Can add maste r_spare_part_type',20,'add_master_spare_part_type'),(78,'Can change maste r_spare_part_type',20,'change_master_spare_part_type'),(79,'Can delete maste r_spare_part_type',20,'delete_master_spare_part_type'),(80,'Can view maste r_spare_part_type',20,'view_master_spare_part_type'),(81,'Can add maste r_vehicle_brand',21,'add_master_vehicle_brand'),(82,'Can change maste r_vehicle_brand',21,'change_master_vehicle_brand'),(83,'Can delete maste r_vehicle_brand',21,'delete_master_vehicle_brand'),(84,'Can view maste r_vehicle_brand',21,'view_master_vehicle_brand'),(85,'Can add maste r_vehicle_category',22,'add_master_vehicle_category'),(86,'Can change maste r_vehicle_category',22,'change_master_vehicle_category'),(87,'Can delete maste r_vehicle_category',22,'delete_master_vehicle_category'),(88,'Can view maste r_vehicle_category',22,'view_master_vehicle_category'),(89,'Can add maste r_expertise_area',23,'add_master_expertise_area'),(90,'Can change maste r_expertise_area',23,'change_master_expertise_area'),(91,'Can delete maste r_expertise_area',23,'delete_master_expertise_area'),(92,'Can view maste r_expertise_area',23,'view_master_expertise_area'),(93,'Can add maste r_pay_grade_level',24,'add_master_pay_grade_level'),(94,'Can change maste r_pay_grade_level',24,'change_master_pay_grade_level'),(95,'Can delete maste r_pay_grade_level',24,'delete_master_pay_grade_level'),(96,'Can view maste r_pay_grade_level',24,'view_master_pay_grade_level'),(97,'Can add maste r_vehicle_model',25,'add_master_vehicle_model'),(98,'Can change maste r_vehicle_model',25,'change_master_vehicle_model'),(99,'Can delete maste r_vehicle_model',25,'delete_master_vehicle_model'),(100,'Can view maste r_vehicle_model',25,'view_master_vehicle_model');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_accountant`
--

DROP TABLE IF EXISTS `core_accountant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_accountant` (
  `employee_id` bigint NOT NULL,
  `education` longtext,
  PRIMARY KEY (`employee_id`),
  CONSTRAINT `CORE_accountant_employee_id_1040ddd2_fk_CORE_employee_id` FOREIGN KEY (`employee_id`) REFERENCES `core_employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_accountant`
--

LOCK TABLES `core_accountant` WRITE;
/*!40000 ALTER TABLE `core_accountant` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_accountant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_advisor`
--

DROP TABLE IF EXISTS `core_advisor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_advisor` (
  `employee_id` bigint NOT NULL,
  `education_desc` longtext,
  PRIMARY KEY (`employee_id`),
  CONSTRAINT `CORE_advisor_employee_id_c11f806c_fk_CORE_employee_id` FOREIGN KEY (`employee_id`) REFERENCES `core_employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_advisor`
--

LOCK TABLES `core_advisor` WRITE;
/*!40000 ALTER TABLE `core_advisor` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_advisor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_cashier`
--

DROP TABLE IF EXISTS `core_cashier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_cashier` (
  `employee_id` bigint NOT NULL,
  `counter_number` varchar(10) NOT NULL,
  PRIMARY KEY (`employee_id`),
  CONSTRAINT `CORE_cashier_employee_id_82ba154b_fk_CORE_employee_id` FOREIGN KEY (`employee_id`) REFERENCES `core_employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_cashier`
--

LOCK TABLES `core_cashier` WRITE;
/*!40000 ALTER TABLE `core_cashier` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_cashier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_customer`
--

DROP TABLE IF EXISTS `core_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_customer` (
  `user_id` int NOT NULL,
  `mobile_number` varchar(128) NOT NULL,
  `address` longtext,
  `description` longtext,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `CORE_customer_user_id_50d0b9cd_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_customer`
--

LOCK TABLES `core_customer` WRITE;
/*!40000 ALTER TABLE `core_customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_employee`
--

DROP TABLE IF EXISTS `core_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_employee` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `DOB` date NOT NULL,
  `Address` longtext NOT NULL,
  `mobile_number` varchar(128) NOT NULL,
  `shift` varchar(10) DEFAULT NULL,
  `pay_grade_id` bigint DEFAULT NULL,
  `role_id` bigint DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `CORE_employee_role_id_d059113d_fk_Masters_master_role_id` (`role_id`),
  KEY `CORE_employee_pay_grade_id_dcce3e6e` (`pay_grade_id`),
  CONSTRAINT `CORE_employee_pay_grade_id_dcce3e6e_fk_Masters_m` FOREIGN KEY (`pay_grade_id`) REFERENCES `masters_master_pay_grade_level` (`id`),
  CONSTRAINT `CORE_employee_role_id_d059113d_fk_Masters_master_role_id` FOREIGN KEY (`role_id`) REFERENCES `masters_master_role` (`id`),
  CONSTRAINT `CORE_employee_user_id_b261e990_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_employee`
--

LOCK TABLES `core_employee` WRITE;
/*!40000 ALTER TABLE `core_employee` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_inventoryinvoice`
--

DROP TABLE IF EXISTS `core_inventoryinvoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_inventoryinvoice` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `supplier` varchar(100) NOT NULL,
  `quantity_received` int unsigned NOT NULL,
  `date` datetime(6) NOT NULL,
  `cost` decimal(10,2) NOT NULL,
  `spare_part_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CORE_inventoryinvoic_spare_part_id_91069a8a_fk_CORE_spar` (`spare_part_id`),
  CONSTRAINT `CORE_inventoryinvoic_spare_part_id_91069a8a_fk_CORE_spar` FOREIGN KEY (`spare_part_id`) REFERENCES `core_sparepart` (`id`),
  CONSTRAINT `core_inventoryinvoice_chk_1` CHECK ((`quantity_received` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_inventoryinvoice`
--

LOCK TABLES `core_inventoryinvoice` WRITE;
/*!40000 ALTER TABLE `core_inventoryinvoice` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_inventoryinvoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_mechanic`
--

DROP TABLE IF EXISTS `core_mechanic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_mechanic` (
  `employee_id` bigint NOT NULL,
  `years_of_experience` smallint unsigned NOT NULL,
  `certifications` longtext,
  `expertise_area_id` bigint NOT NULL,
  PRIMARY KEY (`employee_id`),
  KEY `CORE_mechanic_expertise_area_id_5a7f3546_fk_Masters_m` (`expertise_area_id`),
  CONSTRAINT `CORE_mechanic_employee_id_45c7346e_fk_CORE_employee_id` FOREIGN KEY (`employee_id`) REFERENCES `core_employee` (`id`),
  CONSTRAINT `CORE_mechanic_expertise_area_id_5a7f3546_fk_Masters_m` FOREIGN KEY (`expertise_area_id`) REFERENCES `masters_master_expertise_area` (`id`),
  CONSTRAINT `core_mechanic_chk_1` CHECK ((`years_of_experience` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_mechanic`
--

LOCK TABLES `core_mechanic` WRITE;
/*!40000 ALTER TABLE `core_mechanic` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_mechanic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_service`
--

DROP TABLE IF EXISTS `core_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_service` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(20) NOT NULL,
  `description_of_service` longtext NOT NULL,
  `labor_cost` decimal(10,2) NOT NULL,
  `service_date` datetime(6) NOT NULL,
  `customer_id` int NOT NULL,
  `vehicle_id` bigint NOT NULL,
  `mechanic_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `CORE_service_vehicle_id_79f35b9e_fk_CORE_vehicle_id` (`vehicle_id`),
  KEY `CORE_service_mechanic_id_9b8019d7_fk_CORE_mechanic_employee_id` (`mechanic_id`),
  KEY `CORE_service_customer_id_64546910_fk_CORE_customer_user_id` (`customer_id`),
  CONSTRAINT `CORE_service_customer_id_64546910_fk_CORE_customer_user_id` FOREIGN KEY (`customer_id`) REFERENCES `core_customer` (`user_id`),
  CONSTRAINT `CORE_service_mechanic_id_9b8019d7_fk_CORE_mechanic_employee_id` FOREIGN KEY (`mechanic_id`) REFERENCES `core_mechanic` (`employee_id`),
  CONSTRAINT `CORE_service_vehicle_id_79f35b9e_fk_CORE_vehicle_id` FOREIGN KEY (`vehicle_id`) REFERENCES `core_vehicle` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_service`
--

LOCK TABLES `core_service` WRITE;
/*!40000 ALTER TABLE `core_service` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_serviceinvoice`
--

DROP TABLE IF EXISTS `core_serviceinvoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_serviceinvoice` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` datetime(6) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `payment_method` varchar(10) NOT NULL,
  `status` varchar(10) NOT NULL,
  `service_id` bigint NOT NULL,
  `cashier_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `service_id` (`service_id`),
  KEY `CORE_serviceinvoice_cashier_id_41d6c839_fk_CORE_cash` (`cashier_id`),
  CONSTRAINT `CORE_serviceinvoice_cashier_id_41d6c839_fk_CORE_cash` FOREIGN KEY (`cashier_id`) REFERENCES `core_cashier` (`employee_id`),
  CONSTRAINT `CORE_serviceinvoice_service_id_068dcbf3_fk_CORE_service_id` FOREIGN KEY (`service_id`) REFERENCES `core_service` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_serviceinvoice`
--

LOCK TABLES `core_serviceinvoice` WRITE;
/*!40000 ALTER TABLE `core_serviceinvoice` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_serviceinvoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_servicepart`
--

DROP TABLE IF EXISTS `core_servicepart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_servicepart` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int unsigned NOT NULL,
  `unit_price` decimal(10,2) NOT NULL,
  `service_id` bigint NOT NULL,
  `part_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `CORE_servicepart_service_id_part_id_d7a69a0e_uniq` (`service_id`,`part_id`),
  KEY `CORE_servicepart_part_id_4a1c2323_fk_CORE_sparepart_id` (`part_id`),
  CONSTRAINT `CORE_servicepart_part_id_4a1c2323_fk_CORE_sparepart_id` FOREIGN KEY (`part_id`) REFERENCES `core_sparepart` (`id`),
  CONSTRAINT `CORE_servicepart_service_id_19b7f66e_fk_CORE_service_id` FOREIGN KEY (`service_id`) REFERENCES `core_service` (`id`),
  CONSTRAINT `core_servicepart_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_servicepart`
--

LOCK TABLES `core_servicepart` WRITE;
/*!40000 ALTER TABLE `core_servicepart` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_servicepart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_sparepart`
--

DROP TABLE IF EXISTS `core_sparepart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_sparepart` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `quantity_in_stock` int unsigned NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `type_id` bigint DEFAULT NULL,
  `vehicle_model_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `CORE_sparepart_vehicle_model_id_name_32caaead_uniq` (`vehicle_model_id`,`name`),
  KEY `CORE_sparepart_type_id_60c590bf_fk_Masters_m` (`type_id`),
  CONSTRAINT `CORE_sparepart_type_id_60c590bf_fk_Masters_m` FOREIGN KEY (`type_id`) REFERENCES `masters_master_spare_part_type` (`id`),
  CONSTRAINT `CORE_sparepart_vehicle_model_id_9af94d87_fk_Masters_m` FOREIGN KEY (`vehicle_model_id`) REFERENCES `masters_master_vehicle_model` (`id`),
  CONSTRAINT `core_sparepart_chk_1` CHECK ((`quantity_in_stock` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_sparepart`
--

LOCK TABLES `core_sparepart` WRITE;
/*!40000 ALTER TABLE `core_sparepart` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_sparepart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_vehicle`
--

DROP TABLE IF EXISTS `core_vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_vehicle` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `registration_number` varchar(20) NOT NULL,
  `chassis_number` varchar(17) NOT NULL,
  `year` smallint unsigned NOT NULL,
  `description` longtext NOT NULL,
  `customer_id` int NOT NULL,
  `model_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `registration_number` (`registration_number`),
  UNIQUE KEY `chassis_number` (`chassis_number`),
  KEY `CORE_vehicle_customer_id_370e1bb0_fk_CORE_customer_user_id` (`customer_id`),
  KEY `CORE_vehicle_model_id_79d8b126_fk_Masters_m` (`model_id`),
  CONSTRAINT `CORE_vehicle_customer_id_370e1bb0_fk_CORE_customer_user_id` FOREIGN KEY (`customer_id`) REFERENCES `core_customer` (`user_id`),
  CONSTRAINT `CORE_vehicle_model_id_79d8b126_fk_Masters_m` FOREIGN KEY (`model_id`) REFERENCES `masters_master_vehicle_model` (`id`),
  CONSTRAINT `core_vehicle_chk_1` CHECK ((`year` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_vehicle`
--

LOCK TABLES `core_vehicle` WRITE;
/*!40000 ALTER TABLE `core_vehicle` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_vehicle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(9,'CORE','accountant'),(10,'CORE','advisor'),(11,'CORE','cashier'),(8,'CORE','customer'),(7,'CORE','employee'),(16,'CORE','inventoryinvoice'),(12,'CORE','mechanic'),(13,'CORE','service'),(18,'CORE','serviceinvoice'),(15,'CORE','servicepart'),(14,'CORE','sparepart'),(17,'CORE','vehicle'),(23,'Masters','master_expertise_area'),(24,'Masters','master_pay_grade_level'),(19,'Masters','master_role'),(20,'Masters','master_spare_part_type'),(21,'Masters','master_vehicle_brand'),(22,'Masters','master_vehicle_category'),(25,'Masters','master_vehicle_model'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-11-07 16:02:59.861031'),(2,'auth','0001_initial','2025-11-07 16:03:00.939548'),(3,'contenttypes','0002_remove_content_type_name','2025-11-07 16:03:01.141490'),(4,'auth','0002_alter_permission_name_max_length','2025-11-07 16:03:01.256219'),(5,'auth','0003_alter_user_email_max_length','2025-11-07 16:03:01.291897'),(6,'auth','0004_alter_user_username_opts','2025-11-07 16:03:01.301914'),(7,'auth','0005_alter_user_last_login_null','2025-11-07 16:03:01.414620'),(8,'auth','0006_require_contenttypes_0002','2025-11-07 16:03:01.417656'),(9,'auth','0007_alter_validators_add_error_messages','2025-11-07 16:03:01.424640'),(10,'auth','0008_alter_user_username_max_length','2025-11-07 16:03:01.542155'),(11,'auth','0009_alter_user_last_name_max_length','2025-11-07 16:03:01.664941'),(12,'auth','0010_alter_group_name_max_length','2025-11-07 16:03:01.690972'),(13,'auth','0011_update_proxy_permissions','2025-11-07 16:03:01.704818'),(14,'auth','0012_alter_user_first_name_max_length','2025-11-07 16:03:01.850410'),(15,'Masters','0001_initial','2025-11-07 16:03:02.592255'),(16,'CORE','0001_initial','2025-11-07 16:03:05.231387'),(17,'CORE','0002_alter_employee_user','2025-11-07 16:03:05.263248'),(18,'admin','0001_initial','2025-11-07 16:03:05.534968'),(19,'admin','0002_logentry_remove_auto_add','2025-11-07 16:03:05.550010'),(20,'admin','0003_logentry_add_action_flag_choices','2025-11-07 16:03:05.569113'),(21,'sessions','0001_initial','2025-11-07 16:03:05.649073');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `masters_master_expertise_area`
--

DROP TABLE IF EXISTS `masters_master_expertise_area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `masters_master_expertise_area` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` longtext,
  `role_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `Masters_master_exper_role_id_82dc56c3_fk_Masters_m` (`role_id`),
  CONSTRAINT `Masters_master_exper_role_id_82dc56c3_fk_Masters_m` FOREIGN KEY (`role_id`) REFERENCES `masters_master_role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `masters_master_expertise_area`
--

LOCK TABLES `masters_master_expertise_area` WRITE;
/*!40000 ALTER TABLE `masters_master_expertise_area` DISABLE KEYS */;
/*!40000 ALTER TABLE `masters_master_expertise_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `masters_master_pay_grade_level`
--

DROP TABLE IF EXISTS `masters_master_pay_grade_level`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `masters_master_pay_grade_level` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `level` varchar(10) NOT NULL,
  `base_salary` decimal(10,2) NOT NULL,
  `description` longtext,
  `role_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Masters_master_pay_grade_level_role_id_level_3194a9d6_uniq` (`role_id`,`level`),
  CONSTRAINT `Masters_master_pay_g_role_id_691cc7b2_fk_Masters_m` FOREIGN KEY (`role_id`) REFERENCES `masters_master_role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `masters_master_pay_grade_level`
--

LOCK TABLES `masters_master_pay_grade_level` WRITE;
/*!40000 ALTER TABLE `masters_master_pay_grade_level` DISABLE KEYS */;
/*!40000 ALTER TABLE `masters_master_pay_grade_level` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `masters_master_role`
--

DROP TABLE IF EXISTS `masters_master_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `masters_master_role` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `masters_master_role`
--

LOCK TABLES `masters_master_role` WRITE;
/*!40000 ALTER TABLE `masters_master_role` DISABLE KEYS */;
/*!40000 ALTER TABLE `masters_master_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `masters_master_spare_part_type`
--

DROP TABLE IF EXISTS `masters_master_spare_part_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `masters_master_spare_part_type` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `masters_master_spare_part_type`
--

LOCK TABLES `masters_master_spare_part_type` WRITE;
/*!40000 ALTER TABLE `masters_master_spare_part_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `masters_master_spare_part_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `masters_master_vehicle_brand`
--

DROP TABLE IF EXISTS `masters_master_vehicle_brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `masters_master_vehicle_brand` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `masters_master_vehicle_brand`
--

LOCK TABLES `masters_master_vehicle_brand` WRITE;
/*!40000 ALTER TABLE `masters_master_vehicle_brand` DISABLE KEYS */;
/*!40000 ALTER TABLE `masters_master_vehicle_brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `masters_master_vehicle_category`
--

DROP TABLE IF EXISTS `masters_master_vehicle_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `masters_master_vehicle_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `licence_type` varchar(20) NOT NULL,
  `wheels` smallint unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  CONSTRAINT `masters_master_vehicle_category_chk_1` CHECK ((`wheels` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `masters_master_vehicle_category`
--

LOCK TABLES `masters_master_vehicle_category` WRITE;
/*!40000 ALTER TABLE `masters_master_vehicle_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `masters_master_vehicle_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `masters_master_vehicle_model`
--

DROP TABLE IF EXISTS `masters_master_vehicle_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `masters_master_vehicle_model` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `engine` varchar(50) NOT NULL,
  `weight` int unsigned DEFAULT NULL,
  `description` longtext NOT NULL,
  `brand_id` bigint NOT NULL,
  `category_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Masters_master_vehicle_model_brand_id_name_c8eaf8de_uniq` (`brand_id`,`name`),
  KEY `Masters_master_vehic_category_id_46c005b1_fk_Masters_m` (`category_id`),
  CONSTRAINT `Masters_master_vehic_brand_id_2c81c645_fk_Masters_m` FOREIGN KEY (`brand_id`) REFERENCES `masters_master_vehicle_brand` (`id`),
  CONSTRAINT `Masters_master_vehic_category_id_46c005b1_fk_Masters_m` FOREIGN KEY (`category_id`) REFERENCES `masters_master_vehicle_category` (`id`),
  CONSTRAINT `masters_master_vehicle_model_chk_1` CHECK ((`weight` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `masters_master_vehicle_model`
--

LOCK TABLES `masters_master_vehicle_model` WRITE;
/*!40000 ALTER TABLE `masters_master_vehicle_model` DISABLE KEYS */;
/*!40000 ALTER TABLE `masters_master_vehicle_model` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-07 21:34:43
