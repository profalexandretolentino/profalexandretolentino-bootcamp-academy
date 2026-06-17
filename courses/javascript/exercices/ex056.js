const alunos = [

    {
        nome: "Lucas",
        nota: 8
    },

    {
        nome: "Maria",
        nota: 5
    },

    {
        nome: "João",
        nota: 7
    },

    {
        nome: "Ana",
        nota: 9
    }

];

const aluno =
    alunos.find(

        aluno =>
            aluno.nome === "Ana"

    );

console.log(aluno);