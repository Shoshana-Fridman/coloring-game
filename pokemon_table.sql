USE sql_intro;

DROP TABLE pokemon_types;
DROP TABLE pokemon_ownership;
DROP TABLE pokemons;
DROP TABLE trainers;

CREATE TABLE Pokemons(
    id INT NOt NULL PRIMARY KEY,
    name VARCHAR(30),
    height INT,
    weight INT
);

CREATE TABLE Trainers(
    name VARCHAR(30) PRIMARY KEY,
    town VARCHAR(30)
);

CREATE TABLE pokemon_ownership(
    pokemonId INT,
    trainerName VARCHAR(30),

    PRIMARY KEY (pokemonId, trainerName),
    FOREIGN KEY (pokemonId) REFERENCES Pokemons(id),
    FOREIGN KEY (trainerName) REFERENCES Trainers(name)
);

CREATE TABLE pokemon_types(
    pokemonId INT,
    PokemonType VARCHAR(30),

    PRIMARY KEY (pokemonId, PokemonType),
    FOREIGN KEY (pokemonId) REFERENCES Pokemons(id)
);

