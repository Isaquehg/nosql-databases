# Spotify

    CREATE(a:Band{nome: "Metallica", ano: "1981", genero: "Heavy Metal"});
    CREATE(b:Band{nome: "Iron Maiden", ano: "1975", genero: "Heavy Metal"});
    CREATE(c:Band{nome: "Bon Jovi", ano: "1983", genero: "Rock"});

    CREATE(f:Album{nome: "Black Album", faixas: 12});
    CREATE(d:Album{nome: "Piece of Mind", faixas: 9});
    CREATE(e:Album{nome: "Crush", faixas: 13});

    CREATE(g:Music{nome: "Enter Sandman", duracao: "5:00"});
    CREATE(h:Music{nome: "The Trooper", duracao: "4:12"});
    CREATE(i:Music{nome: "Its My Life", duracao: "3:45"});

    MATCH(a:Band{nome:"Metallica"}), (f:Album{nome:"Black Album"}), (g:Music{nome: "Enter Sandman"})
    CREATE(a)-[:GRAVOU{ano: 1986}]->(f)-[:POSSUI]->(g);

    MATCH(b:Band{nome:"Iron Maiden"}), (d:Album{nome:"Piece of Mind"}), (h:Music{nome: "The Trooper"})
    CREATE(b)-[:GRAVOU{ano: 1983}]->(d)-[:POSSUI]->(h);

    MATCH(c:Band{nome:"Bon Jovi"}), (e:Album{nome:"Crush"}), (i:Music{nome: "Its My Life"})
    CREATE(c)-[:GRAVOU{ano: 2000}]->(e)-[:POSSUI]->(i);

    MATCH(a:Band{nome:"Metallica"}), (b:Band{nome:"Iron Maiden"})
    CREATE(a)-[:FORTE]->(b);
    MATCH(c:Band{nome:"Iron Maiden"}), (d:Band{nome:"Bon Jovi"})
    CREATE(c)-[:MEDIO]->(d);
    MATCH(e:Band{nome:"Bon Jovi"}), (f:Band{nome:"Metallica"})
    CREATE(e)-[:FRACO]->(f);
