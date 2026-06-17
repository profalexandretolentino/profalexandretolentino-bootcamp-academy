const alunos = [

    { nome: "Lucas", nota: 8 },
    { nome: "Maria", nota: 5 },
    { nome: "João", nota: 7 },
    { nome: "Ana", nota: 9 }

];

const soma =

    alunos.reduce(

        (total, aluno) =>

            total + aluno.nota,

        0

    );

const media =
    soma / alunos.length;

alunos.sort(

    (a, b) =>

        b.nota - a.nota

);

console.log(
    `Média: ${media}`
);

console.log(alunos);