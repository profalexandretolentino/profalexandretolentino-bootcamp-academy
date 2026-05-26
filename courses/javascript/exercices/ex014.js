// Funções com retorno
function soma(a, b) {
    return a + b;
}

function subtracao(a, b) {
    return a - b;
}

function multiplicacao(a, b) {
    return a * b;
}

function divisao(a, b) {
    if (b === 0) {
        return "Erro: divisão por zero!";
    }
    return a / b;
}

// Procedimento (sem retorno)
function imprimirResultado(resultado) {
    console.log("Resultado:", resultado);
}

// Testando as funções
imprimirResultado(soma(10, 5));
imprimirResultado(subtracao(10, 5));
imprimirResultado(multiplicacao(10, 5));
imprimirResultado(divisao(10, 5));