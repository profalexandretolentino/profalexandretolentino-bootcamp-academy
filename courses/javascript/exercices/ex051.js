// Nome do aluno
const aluno = "Lucas";

// Data atual
const matricula = new Date();

// Exibe informações
console.log(
    `Aluno: ${aluno}`
);

console.log(
    `Data:
    ${matricula.toLocaleDateString()}`
);

console.log(
    `Horário:
    ${matricula.toLocaleTimeString()}`
);