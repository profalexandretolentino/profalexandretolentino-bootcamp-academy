// Factory Function
function criarCupom(codigo, descontoPorcentagem, estaAtivo) {
    return {
        codigo,
        descontoPorcentagem,
        estaAtivo,

        exibirInformacoes() {
            console.log(
                `Cupom ${this.codigo} oferece ${this.descontoPorcentagem}% de desconto.`
            );
        }
    };
}

// Criando os cupons
const cupom1 = criarCupom("PROMO10", 10, true);
const cupom2 = criarCupom("BLACK50", 50, true);
const cupom3 = criarCupom("VIP25", 25, false);

// Executando o método
cupom1.exibirInformacoes();
cupom2.exibirInformacoes();
cupom3.exibirInformacoes();