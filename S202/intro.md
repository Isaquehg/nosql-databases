# Intro NoSQL
## Motivação
### Suporte ao Big Data (3Vs)
- Volume
- Velocity
- Variety
## Características
- Schemaless
- Escalabilidade Horizontal (Trocar roda do carro andando)
- Modelo BASE ao invés de ACID
    - BA -> Apenas algumas partes do sistema ficam indisponível (Basically Avaliable)
    - S -> Um servidor não avisa imediatamente outros servidores após uma operação, como inclusão ou edição (Soft State)
    - E -> Em um mesmo momento podem haver dois valores para um mesmo dado (Eventually Consistent)
## Tipos
- Orientado a Documentos
    - Dados são documentos dentro de documentos(JSON)
    - Pode ser necessário duplicar dados pelo modelo
- Orientado a Grafos
    - Destinado a relações de linearidade
    - Todas relações já indexadas
    - Cypher
- Orientado a Colunas
    - Baseado em Família de Colunas
    - Reduz custo e espaço
- Orientado a Chave-Valor
    - Alta performance
    - Trabalha na memória RAM
    - Utilizado como cache, para arquivos mais acessado, por exemplo

## CAP
- Consistency
- Avaliability
- Partition Tolerance

## Não Ocorrem
- Joins
- Auto Trasactions
- Constraints (Foreign Keys)