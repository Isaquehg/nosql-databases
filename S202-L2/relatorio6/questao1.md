## Questão 01
### Elabore consultas em Neo4j para obter os seguintes resultados:
1. Todos os registros do banco de dados.

        MATCH(n) RETURN n;

2. Jogos lançados após o ano de 2012.

        MATCH(n:Game) WHERE n.ano > 2012 RETURN n;

3. Jogos do gênero de terror.

        MATCH(n:Game) WHERE n.genero = "Terror" RETURN n;

4. Jogos com uma nota igual ou maior que 7.

        MATCH (n:Jurado)-[m:JOGOU]->(Game) WHERE m.nota > 7 RETURN m;