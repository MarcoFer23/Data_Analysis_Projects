-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema er_model_sample
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema er_model_sample
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `er_model_sample` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `er_model_sample` ;

-- -----------------------------------------------------
-- Table `er_model_sample`.`Videogiochi`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `er_model_sample`.`Videogiochi` (
  `id_videogioco` INT NOT NULL,
  `titolo_videogioco` VARCHAR(45) NULL,
  `casa_produttrice` VARCHAR(45) NULL,
  PRIMARY KEY (`id_videogioco`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `er_model_sample`.`Sviluppatore`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `er_model_sample`.`Sviluppatore` (
  `id_sviluppatore` INT NOT NULL,
  `id_videogioco` INT NOT NULL,
  PRIMARY KEY (`id_sviluppatore`, `id_videogioco`),
  INDEX `fk_id_videogioco_idx` (`id_videogioco` ASC) VISIBLE,
  CONSTRAINT `fk_id_videogioco`
    FOREIGN KEY (`id_videogioco`)
    REFERENCES `er_model_sample`.`Videogiochi` (`id_videogioco`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
