CREATE DATABASE  IF NOT EXISTS `mydb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `mydb`;
-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `WAEL_info`
--

DROP TABLE IF EXISTS `WAEL_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WAEL_info` (
  `idWAEL_info` int(11) NOT NULL AUTO_INCREMENT,
  `electricity_expenses` varchar(50) DEFAULT NULL,
  `water_expenses` varchar(50) DEFAULT NULL,
  `car_number` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`idWAEL_info`),
  UNIQUE KEY `idWAEL_info_UNIQUE` (`idWAEL_info`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `car_info`
--

DROP TABLE IF EXISTS `car_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `car_info` (
  `idcar_info` int(11) NOT NULL AUTO_INCREMENT,
  `car_number` varchar(8) DEFAULT NULL,
  `owner_company` varchar(50) DEFAULT NULL,
  `branch` varchar(50) DEFAULT NULL,
  `service_mode` int(11) DEFAULT NULL,
  `shaceh_number` varchar(10) DEFAULT NULL,
  `motor_number` varchar(10) DEFAULT NULL,
  `fuel_type` int(11) DEFAULT NULL,
  `car_type` varchar(50) DEFAULT NULL,
  `car_model` int(11) DEFAULT NULL,
  `car_load` float DEFAULT NULL,
  `car_weight` float DEFAULT NULL,
  `car_shape` varchar(50) DEFAULT NULL,
  `car_color` varchar(50) DEFAULT NULL,
  `car_infocol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idcar_info`),
  UNIQUE KEY `idcar_info_UNIQUE` (`idcar_info`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fuel_info`
--

DROP TABLE IF EXISTS `fuel_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fuel_info` (
  `idfuel_info` int(11) NOT NULL AUTO_INCREMENT,
  `liter_number` float DEFAULT NULL,
  `counter_reading` float DEFAULT NULL,
  `tips` float DEFAULT NULL,
  `liter_price` float DEFAULT NULL,
  `total` float DEFAULT NULL,
  `car_number` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idfuel_info`),
  UNIQUE KEY `idfuel_info_UNIQUE` (`idfuel_info`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `licence_info`
--

DROP TABLE IF EXISTS `licence_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `licence_info` (
  `idlicence_info` int(11) NOT NULL AUTO_INCREMENT,
  `annual_renew` varchar(50) DEFAULT NULL,
  `newcar_licence` varchar(50) DEFAULT NULL,
  `renew_permission` varchar(50) DEFAULT NULL,
  `infraction_info` varchar(50) DEFAULT NULL,
  `annual_infraction` varchar(50) DEFAULT NULL,
  `stamping_receipts` varchar(50) DEFAULT NULL,
  `withdrawn_licence` varchar(50) DEFAULT NULL,
  `withdrawn_infraction` varchar(50) DEFAULT NULL,
  `car_number` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`idlicence_info`),
  UNIQUE KEY `idlicence_info_UNIQUE` (`idlicence_info`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `maintenance_info`
--

DROP TABLE IF EXISTS `maintenance_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maintenance_info` (
  `idmaintenance_info` int(11) NOT NULL AUTO_INCREMENT,
  `engine_amra` varchar(50) DEFAULT NULL,
  `mechanics` varchar(50) DEFAULT NULL,
  `electricity` varchar(50) DEFAULT NULL,
  `samkara` varchar(50) DEFAULT NULL,
  `afsha` varchar(50) DEFAULT NULL,
  `periodic_maintenance` varchar(50) DEFAULT NULL,
  `cooling` varchar(50) DEFAULT NULL,
  `glass` varchar(50) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  `car_number` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`idmaintenance_info`),
  UNIQUE KEY `idmaintenance_info_UNIQUE` (`idmaintenance_info`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rent_info`
--

DROP TABLE IF EXISTS `rent_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rent_info` (
  `idrent_info` int(11) NOT NULL AUTO_INCREMENT,
  `monthly_revenu` varchar(50) DEFAULT NULL,
  `arab_ghofra` varchar(50) DEFAULT NULL,
  `car_number` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`idrent_info`),
  UNIQUE KEY `idrent_info_UNIQUE` (`idrent_info`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `revenue_info`
--

DROP TABLE IF EXISTS `revenue_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `revenue_info` (
  `idrevenue_info` int(11) NOT NULL AUTO_INCREMENT,
  `kohna_selling` varchar(50) DEFAULT NULL,
  `insurance_compensation` varchar(50) DEFAULT NULL,
  `accedint_compensation` varchar(50) DEFAULT NULL,
  `car_number` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`idrevenue_info`),
  UNIQUE KEY `idrevenue_info_UNIQUE` (`idrevenue_info`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `idusers` int(11) NOT NULL,
  `user_name` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `permissions` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idusers`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-30 21:10:08
