const alunos = [

    { nome: "Lucas", nota: 8 },
    { nome: "Maria", nota: 5 },
    { nome: "João", nota: 7 }

];

const existeReprovado =

    alunos.some(

        aluno =>
            aluno.nota < 6

    );

const todosAprovados =

    alunos.every(

        aluno =>
            aluno.nota >= 6

    );

console.log(existeReprovado);

console.log(todosAprovados);