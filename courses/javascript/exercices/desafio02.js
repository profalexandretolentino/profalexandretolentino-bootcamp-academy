// =========================================
// SISTEMA ESCOLAR - DATE
// =========================================

// Nome do aluno
const aluno = "Lucas Silva";

// Data atual do sistema
const dataAtual = new Date();

// =========================================
// DATA ATUAL
// =========================================

console.log(
    `Data atual: ${
        dataAtual.toLocaleDateString()
    }`
);

// =========================================
// HORÁRIO ATUAL
// =========================================

console.log(
    `Horário atual: ${
        dataAtual.toLocaleTimeString()
    }`
);

// =========================================
// ANO ATUAL
// =========================================

console.log(
    `Ano atual: ${
        dataAtual.getFullYear()
    }`
);

// =========================================
// MÊS ATUAL
// =========================================

// Soma +1 porque os meses começam em ZERO
const mesAtual =
    dataAtual.getMonth() + 1;

console.log(
    `Mês atual: ${mesAtual}`
);

// =========================================
// DATA DE MATRÍCULA
// =========================================

// Cria uma matrícula usando a data atual
const dataMatricula = new Date();

// =========================================
// EXIBINDO DADOS DO ALUNO
// =========================================

console.log(
    `
    ==========================
    DADOS DO ALUNO
    ==========================

    Nome: ${aluno}

    Data da matrícula:
    ${dataMatricula.toLocaleDateString()}

    Horário da matrícula:
    ${dataMatricula.toLocaleTimeString()}
    `
);