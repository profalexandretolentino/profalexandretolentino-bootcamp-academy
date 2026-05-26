// Funções de conversão (com retorno)

function converterParaCelsius(temperatura, escalaOrigem) {
    if (escalaOrigem === "F") {
        return (temperatura - 32) * 5 / 9;
    } else if (escalaOrigem === "K") {
        return temperatura - 273.15;
    }
    return temperatura; // já está em Celsius
}

function converterParaFahrenheit(temperatura, escalaOrigem) {
    if (escalaOrigem === "C") {
        return (temperatura * 9 / 5) + 32;
    } else if (escalaOrigem === "K") {
        return (temperatura - 273.15) * 9 / 5 + 32;
    }
    return temperatura; // já está em Fahrenheit
}

function converterParaKelvin(temperatura, escalaOrigem) {
    if (escalaOrigem === "C") {
        return temperatura + 273.15;
    } else if (escalaOrigem === "F") {
        return (temperatura - 32) * 5 / 9 + 273.15;
    }
    return temperatura; // já está em Kelvin
}

// Procedimento (sem retorno)
function exibirResultado(valor, escalaDestino) {
    console.log(`Temperatura convertida: ${valor.toFixed(2)} °${escalaDestino}`);
}

// Exemplos de uso
let resultado1 = converterParaFahrenheit(25, "C");
exibirResultado(resultado1, "F");

let resultado2 = converterParaKelvin(30, "C");
exibirResultado(resultado2, "K");

let resultado3 = converterParaCelsius(98.6, "F");
exibirResultado(resultado3, "C");