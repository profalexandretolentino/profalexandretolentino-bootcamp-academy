const turmaA = [
    "Lucas",
    "Maria"
];

const turmaB = [
    "Ana",
    "João"
];

// Une turmas
const turmaCompleta = [
    ...turmaA,
    ...turmaB
];

// Desestrutura
const [
    aluno1,
    aluno2
] = turmaCompleta;

console.log(turmaCompleta);

console.log(aluno1);
console.log(aluno2);