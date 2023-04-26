## Questão 02

1. Acrescente quatro novos jogos ao banco de dados.

        CREATE(m:Game{ano: 2013, genero: "Aventura", titulo: "The Last of Us"});
        CREATE(n:Game{ano: 2015, genero: "FPS", titulo: "Rainbow Six Siege"});
        CREATE(o:Game{ano: 2016, genero: "Aventura", titulo: "Uncharted 4"});

2. Adicione três novos jurados ao banco de dados.

        CREATE(p:Jurado{nome:"Isaque"});
        CREATE(q:Jurado{nome:"Larry"});
        CREATE(r:Jurado{nome:"Darry"});

3. Estabeleça as relações entre os jurados e os jogos que eles avaliaram, incluindo a nota e a quantidade de horas jogadas.

        MATCH(p:Jurado{nome:"Isaque"}), (m:Game{titulo:"The Last of Us"})
        CREATE(p)-[:JOGOU{horas: 120, nota: 10}]->(m);
        MATCH(q:Jurado{nome:"Larry"}), (n:Game{titulo:"Rainbow Six Siege"})
        CREATE(q)-[:JOGOU{horas: 2355, nota: 8}]->(n);
        MATCH(r:Jurado{nome:"Darry"}), (o:Game{titulo:"Uncharted 4"})
        CREATE(r)-[:JOGOU{horas: 542, nota: 9}]->(o);