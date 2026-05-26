// Criando objeto usuario
const usuario = {

    "nome": "Fernanda Lima",
    "plano": "Básico",
    "preço": 50.00,
    "idade": 22,
    "seriesFavoritas": [
        "Dark",
        "Stranger Things",
        "Round 6"
    ],
    "ativo": true
};


// -----------------------------
// CREATE -> adicionando propriedade
// -----------------------------

// Adicionando email
usuario["email"] = "fernanda@gmail.com";


// -----------------------------
// READ -> lendo propriedades
// -----------------------------

console.log(usuario["nome"]);

console.log(usuario["plano"]);

console.log(usuario["seriesFavoritas"]);


// -----------------------------
// UPDATE -> atualizando valores
// -----------------------------

// Atualizando plano
usuario["plano"] = "Premium";

// Atualizando Preço
usuario["preço"] = 250.00;


// -----------------------------
// DELETE -> removendo propriedade
// -----------------------------

delete usuario["ativo"];


// Exibindo objeto final
console.log(usuario);