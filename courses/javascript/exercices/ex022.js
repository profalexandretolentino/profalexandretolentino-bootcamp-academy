// Criando um objeto chamado dev
const dev = {
  nome: "Carlos Silva",
  linguagemPrincipal: "JavaScript",
  senioridade: "Júnior",
  salario: 3500.00,
  projetos: ["Sistema Web", "API REST", "Dashboard"],
  trabalhandoRemoto: true
};

// -----------------------------
// CREATE -> adicionando propriedade
// -----------------------------

// Adicionando uma nova propriedade
dev.empresa = "Tech Solutions";

// -----------------------------
// READ -> lendo propriedades
// -----------------------------

// Exibindo informações do desenvolvedor
console.log(dev.nome);
console.log(dev.linguagemPrincipal);
console.log(dev.projetos);

// -----------------------------
// UPDATE -> atualizando valores
// -----------------------------

// Atualizando nível de senioridade
dev.senioridade = "Pleno";

// Atualizando salário
dev.salario = 5200.00;

// -----------------------------
// DELETE -> removendo propriedade
// -----------------------------

// Removendo a propriedade trabalhandoRemoto
delete dev.trabalhandoRemoto;

// Exibindo objeto final
console.log(dev);
