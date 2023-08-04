CREATE TABLE Store (
    id_store INT,
    indirizzo_fisico TEXT(255) NOT NULL,
    numero_di_telefono TEXT(255) NOT NULL,
    PRIMARY KEY (id_store)
);

CREATE TABLE Dipendente (
    codice_fiscale VARCHAR(16),
    nome TEXT(255) NOT NULL,
    titolo_di_studio TEXT(255) NOT NULL,
    recapito TEXT(255) NOT NULL,
    ruolo TEXT(255) NOT NULL,
    id_store INT NOT NULL,
    data_inizio_impiego DATE NOT NULL,
    data_fine_impiego DATE,
    PRIMARY KEY (codice_fiscale , data_inizio_impiego),
    CONSTRAINT FK_Store_Dipendente FOREIGN KEY (id_store)
        REFERENCES Store (id_store)
        ON UPDATE CASCADE ON DELETE NO ACTION
);

CREATE TABLE Settore (
    id_store INT,
    id_settore INT,
    PRIMARY KEY (id_store , id_settore),
    CONSTRAINT FK_Store_Settore FOREIGN KEY (id_store)
        REFERENCES Store (id_store)
        ON UPDATE CASCADE ON DELETE NO ACTION
);

CREATE INDEX idx_id_settore ON Settore (id_settore);


CREATE TABLE Videogiochi (
    titolo VARCHAR(255),
    sviluppatore VARCHAR(255),
    anno_di_uscita DATE NOT NULL,
    prezzo DECIMAL(5 , 2 ) NOT NULL,
    genere TEXT(255) NOT NULL,
    remake BOOLEAN NOT NULL,
    PRIMARY KEY (titolo , sviluppatore)
);


CREATE TABLE Si_trova (
    id_store INT,
    id_settore INT,
    posizione TEXT(255) NOT NULL,
    disponibilità BOOLEAN NOT NULL,
    titolo VARCHAR(255) NOT NULL,
    sviluppatore VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_store , id_settore , titolo , sviluppatore),
    CONSTRAINT FK_Store_Si_trova FOREIGN KEY (id_store)
        REFERENCES Store (id_store)
        ON UPDATE CASCADE ON DELETE NO ACTION,
    CONSTRAINT FK_Settore_Si_trova FOREIGN KEY (id_settore)
        REFERENCES Settore (id_settore)
        ON UPDATE CASCADE ON DELETE NO ACTION,
    CONSTRAINT FK_Videogiochi_Si_trova FOREIGN KEY (titolo , sviluppatore)
        REFERENCES Videogiochi (titolo , sviluppatore)
        ON UPDATE CASCADE ON DELETE NO ACTION
);