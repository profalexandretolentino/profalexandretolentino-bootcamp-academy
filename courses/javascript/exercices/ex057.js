const alunos = [

    { nome: "Lucas", nota: 8 },
    { nome: "Maria", nota: 5 },
    { nome: "João", nota: 7 },
    { nome: "Ana", nota: 9 }

];

const aprovados =

    alunos.filter(

        aluno =>
            aluno.nota >= 6

    );

const nomes =

    aprovados.map(

        aluno =>
            aluno.nome

    );

console.log(nomes);