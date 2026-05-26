// Criando objeto produto
const produto = {

    "nome": "Teclado Mecânico RGB",
    "categoria": "Periféricos",
    "preco": 350,
    "plataformas": [
        "Windows",
        "Linux"
    ],
    "estoque": 15
};


// -----------------------------
// CREATE -> adicionando propriedade
// -----------------------------

// Adicionando fabricante
produto["fabricante"] = "HyperTech";


// -----------------------------
// READ -> lendo propriedades
// -----------------------------

console.log(produto["nome"]);

console.log(produto["preco"]);

console.log(produto["estoque"])

console.log(produto["plataformas"]);


// -----------------------------
// UPDATE -> atualizando valores
// -----------------------------

// Atualizando preço
produto["preco"] = 420;

// Atualizando estoque
produto["estoque"] = 10;


// -----------------------------
// DELETE -> removendo propriedade
// -----------------------------

delete produto["categoria"];


// Exibindo objeto final
console.log(produto);