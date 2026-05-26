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
console.log("Servidor Ligado: ", servidor.ativo);
console.log("Usuários Online: ", servidor.usuariosOnline);
console.log("Uso de CPU: ", servidor.usoCPU, "%\n");

// Exibindo o objeto completo com todas as propriedades
console.log(servidor)