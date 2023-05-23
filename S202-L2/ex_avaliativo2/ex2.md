# Questão 2
## Encontre o usuário mais velho.

    MATCH (u:Usuario)
    RETURN u.nome, u.idade
    ORDER BY u.idade DESC
    LIMIT 1

    R.: "Eve"	45

## Quantos usuários têm mais de 30 anos?

    MATCH (u:Usuario)
    WHERE u.idade > 30
    RETURN count(u) AS total

    R.: 3

## Qual é a média de idade dos usuários?

    MATCH (u:Usuario)
    WITH avg(u.idade) AS media
    RETURN media

    R.: 35.0
