CREATE DATABASE IF NOT EXISTS teste DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_0900_ai_ci;
USE teste;

CREATE TABLE musica (
  idMusica int NOT NULL AUTO_INCREMENT,
  nomeMusica varchar(50) NOT NULL,
  PRIMARY KEY (idMusica)
);


CREATE TABLE musicaData (
  idMusicaData int NOT NULL AUTO_INCREMENT,
  idMusica int NOT NULL,
  posicao int NOT NULL,
  dt date NOT NULL,
  PRIMARY KEY (idMusicaData),
  CONSTRAINT musicaData_musica
    FOREIGN KEY (idMusica)
    REFERENCES musica (idMusica)
);


CREATE TABLE cantor (
  idCantor int NOT NULL AUTO_INCREMENT,
  nomeCantor varchar(50) NOT NULL,
  PRIMARY KEY (idCantor)
);


CREATE TABLE musica_cantor (
  idMusicaCantor int NOT NULL AUTO_INCREMENT,
  idMusica int NOT NULL,
  idCantor int NOT NULL,
  PRIMARY KEY (idMusicaCantor),
  CONSTRAINT musica_cantor_idmusica
    FOREIGN KEY (idMusica)
    REFERENCES musica (idMusica),
  CONSTRAINT musica_canto_idcantor
    FOREIGN KEY (idCantor)
    REFERENCES cantor (idCantor)
);
