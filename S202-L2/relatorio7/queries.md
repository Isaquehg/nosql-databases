# Relatório 7
## Agregações

    1. MATCH(n:Purchase) RETURN COUNT(n.amount);
    2. MATCH(n:Purchase) RETURN SUM(n.amount);
    3. MATCH(n:Purchase) RETURN AVG(n.amount);
    4. MATCH(n:Purchase) RETURN MIN(n.amount);
    5. MATCH(n:Purchase) RETURN MAX(n.amount);

## Funções Matemáticas 

    1. MATCH(n:Purchase) RETURN ABS(n.amount);
    2. RETURN RAND();
    3. MATCH(n:UnsecuredLoan) RETURN ROUND(n.balance, 2, 'CEILING');
    4. RETURN SIGN(-17654321);
    5. RETURN FLOOR(0.75)

## Funções de String

    1. MATCH(n:AccountHolder) RETURN LEFT(n.firstName, 3);
    2. MATCH(n:AccountHolder) RETURN TOUPPER(n.lastName);
    3. MATCH(n:AccountHolder) RETURN REVERSE(n.fullName);
    4. MATCH(n:FinancialInstitute) RETURN SPLIT(n.name, ' ');
    5. MATCH(n:FinancialInstitute) RETURN TOLOWER(n.name);
