create table if not exists Store (
	id_store int, 
	indirizzo_fisico text(255) not null, 
	numero_di_telefono text(255) not null,
		primary key (id_store)
);

create table if not exists Dipendente (
	codice_fiscale varchar(16),
	nome text(255) not null,
	titolo_di_studio text(255) not null,
	recapito text(255) not null,
	ruolo text(255) not null,
	id_store int not null, 
	data_inizio_impiego date not null,
	data_fine_impiego date,
		primary key (codice_fiscale,data_inizio_impiego),
			foreign key (id_store) references Store(id_store) on update cascade on delete no action
);

create table if not exists Settore (
	id_store int, 
	id_settore int,
		primary key (id_store,id_settore),
			foreign key (id_store) references Store(id_store) on update cascade on delete no action
);

create table if not exists Videogiochi (
	titolo varchar(255),
	sviluppatore varchar(255), 
	anno_di_uscita date not null, 
	prezzo decimal(5,2) not null,
	genere text(255) not null, 
	remake boolean not null,
		primary key (titolo,sviluppatore)
);

create table if not exists Si_trova (
	id_store int, 
	id_settore int, 
	posizione text(255) not null, 
	disponibilità boolean not null, 
	titolo varchar(255) not null, 
	sviluppatore varchar(255) not null,
		primary key (id_store,id_settore,titolo,sviluppatore),
			foreign key (id_store) references Store(id_store) on update cascade on delete no action,
            foreign key (titolo,sviluppatore) references Videogiochi(titolo,sviluppatore) on update cascade on delete no action         
);







