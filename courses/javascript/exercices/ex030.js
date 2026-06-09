// Factory Function
function gerarNotificacao(remetente, tipo, conteudo) {
    return {
        remetente,
        tipo,
        conteudo,
        lida: false,

        marcarComoLida() {
            this.lida = true;
        },

        exibirAlerta() {
            if (!this.lida) {
                console.log(`[Novo Alerta de ${this.remetente}]: ${this.conteudo}`);
            } else {
                console.log("(Mensagem antiga arquivada)");
            }
        }
    };
}

// Criando as notificações
const notificacao1 = gerarNotificacao(
    "João",
    "mensagem",
    "Você recebeu uma nova mensagem."
);

const notificacao2 = gerarNotificacao(
    "Sistema",
    "sistema",
    "Sua senha será alterada em breve."
);

// Exibindo os alertas
notificacao1.exibirAlerta();
notificacao2.exibirAlerta();

// Marcando a primeira notificação como lida
notificacao1.marcarComoLida();

console.log("Após marcar a primeira notificação como lida:");

// Exibindo novamente os alertas
notificacao1.exibirAlerta();
notificacao2.exibirAlerta();