const alunos = [
    "Lucas",
    "Maria",
    "João"
];

alunos.push("Ana");

alunos.unshift("Carlos");

alunos.pop();

alunos.shift();

const grupo =
    alunos.slice(0, 2);

alunos.splice(
    1,
    1,
    "Fernanda"
);

const turma2 = [
    "Pedro",
    "Julia"
];

const turmaFinal = [
    ...alunos,
    ...turma2
];

const [
    primeiro,
    segundo
] = turmaFinal;

console.log(turmaFinal);

console.log(primeiro);

console.log(segundo);