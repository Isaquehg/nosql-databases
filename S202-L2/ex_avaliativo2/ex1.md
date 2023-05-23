# Questão 1
## Quem é amigo de Bob?

    MATCH (:Usuario {nome: 'Bob'})-[:AMIGO]->(amigo)
    RETURN amigo.nome

    R.: "Charlie"
## Quem postou a 'Postagem 2'?

    MATCH (:Postagem {titulo: 'Memórias da Tarde'})<-[:POSTOU]-(autor)
    RETURN autor.nome

    R.: "Bob"
##  Quem tem mais de 35 anos e fez uma postagem?

    MATCH (u:Usuario)-[:POSTOU]->(:Postagem)
    WHERE u.idade > 35
    RETURN u.nome

    R.: N.A.