const alunos = [

    { nome: "Lucas", nota: 8 },

    { nome: "Maria", nota: 5 },

    { nome: "João", nota: 7 },

    { nome: "Ana", nota: 9 },

    { nome: "Carlos", nota: 6 },

    { nome: "Fernanda", nota: 10 },

    { nome: "Pedro", nota: 4 }

];

// FIND
const fernanda =

    alunos.find(

        aluno =>
            aluno.nome === "Fernanda"

    );

// FILTER
const aprovados =

    alunos.filter(

        aluno =>
            aluno.nota >= 6

    );

// MAP
const nomesAprovados =

    aprovados.map(

        aluno =>
            aluno.nome

    );

// REDUCE
const soma =

    alunos.reduce(

        (total, aluno) =>

            total + aluno.nota,

        0

    );

const media =
    soma / alunos.length;

// SORT
const ranking =

    [...alunos].sort(

        (a, b) =>

            b.nota - a.nota

    );

// SOME
const existeReprovado =

    alunos.some(

        aluno =>
            aluno.nota < 6

    );

// EVERY
const todosAprovados =

    alunos.every(

        aluno =>
            aluno.nota >= 6

    );

console.log(fernanda);

console.log(nomesAprovados);

console.log(media);

console.log(ranking);

console.log(existeReprovado);

console.log(todosAprovados);