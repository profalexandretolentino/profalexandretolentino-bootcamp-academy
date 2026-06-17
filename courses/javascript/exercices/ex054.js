const alunos = [
    "Lucas",
    "Maria",
    "João",
    "Ana",
    "Carlos",
    "Fernanda"
];

// Cria grupo
const grupo =
    alunos.slice(0, 3);

// Troca João por Pedro
alunos.splice(
    2,
    1,
    "Pedro"
);

console.log(grupo);
console.log(alunos);