// Classe responsável pelo CRUD de chamados
class Chamado {

    constructor() {

        // Array que armazenará os chamados
        this["listaChamados"] = [];
    }

    // CREATE
    criarChamado(id, cliente, problema, status) {

        // Objeto do chamado
        let chamado = {
            "id": id,
            "cliente": cliente,
            "problema": problema,
            "status": status
        };

        // Adiciona no array
        this["listaChamados"]["push"](chamado);

        console["log"]("Chamado cadastrado com sucesso!");
    }

    // READ
    listarChamados() {

        console["log"]("LISTA DE CHAMADOS:");

        this["listaChamados"]["forEach"](function(chamado) {

            console["log"](chamado);

        });
    }

    // UPDATE
    atualizarStatus(id, novoStatus) {

        this["listaChamados"]["forEach"](function(chamado) {

            // Verifica o ID
            if(chamado["id"] === id) {

                // Atualiza o status
                chamado["status"] = novoStatus;

                console["log"]("Status atualizado!");
            }
        });
    }

    // DELETE
    removerChamado(id) {

        this["listaChamados"] =
        this["listaChamados"]["filter"](function(chamado) {

            return chamado["id"] !== id;
        });

        console["log"]("Chamado removido!");
    }
}


// Criando objeto
let sistema = new Chamado();


// CREATE
sistema["criarChamado"](
    1,
    "Empresa Alpha",
    "Erro no login",
    "Aberto"
);

sistema["criarChamado"](
    2,
    "Loja Tech",
    "Sistema lento",
    "Em análise"
);


// READ
sistema["listarChamados"]();


// UPDATE
sistema["atualizarStatus"](
    1,
    "Resolvido"
);


// READ novamente
sistema["listarChamados"]();


// DELETE
sistema["removerChamado"](2);


// READ final
sistema["listarChamados"]();