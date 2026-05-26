// Criando um objeto chamado servidor
const servidor = {
    // Nome do servidor
    nome: "Servidor Linux",
  
    // Endereço IP do servidor
    ip: "192.168.0.10",
  
    // Status do servidor (true = ativo / false = desligado)
    ativo: true,
  
    // Quantidade de usuários conectados
    usuariosOnline: 154,
  
    // Uso atual da CPU em porcentagem
    usoCPU: 73.5
  };
  
  // Exibindo os dados do servidor no console
  console.log("Nome do Servidor: ", servidor.nome);
  console.log("IP: ", servidor.ip);
  console.log("Servidor Ativo: ", servidor.ativo);
  console.log("Usuários Online: ", servidor.usuariosOnline);
  console.log("Uso de CPU: ", servidor.usoCPU);
  
  
  // CREATE - Adicionando novas propriedades ao objeto servidor
  
  // Quantidade de memória RAM
  servidor.memoriaRAM = "32GB";
  
  // Data do último backup realizado
  servidor.dataBackup = "2026-05-19";
  
  // Lista de serviços que estão rodando no servidor
  servidor.servicosRodando = ["Apache", "Docker", "MySQL"];
  
  // Exibindo as novas propriedades no console
  console.log("\nMemória RAM: ", servidor.memoriaRAM);
  console.log("Data do Backup: ", servidor.dataBackup);
  console.log("Serviços Rodando: ", servidor.servicosRodando);
  
// Exibindo o nome do servidor
console.log(servidor.nome);

// Exibindo o endereço IP do servidor
console.log(servidor.ip);

// Exibindo a quantidade de usuários online
console.log(servidor.usuariosOnline);

// Exibindo o segundo serviço do array
console.log(servidor.servicosRodando[1]);


// UPDATE - Atualizando o uso da CPU do servidor
servidor.usoCPU = 91.8;

// Atualizando a quantidade de usuários online
servidor.usuariosOnline = 203;

// Adicionando um novo serviço ao array
servidor.servicosRodando.push("Node.js");


// Inicia READ do UPDATE
console.log("-- Dados atualizados no UPDATE -- ")

// Exibindo os valores atualizados
console.log(servidor.usoCPU);
console.log(servidor.usuariosOnline);
console.log(servidor.servicosRodando);

