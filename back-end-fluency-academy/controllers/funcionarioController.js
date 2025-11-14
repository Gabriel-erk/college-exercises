const funcionario = require("../models/funcionario");
module.exports = class FuncionarioController { 
      static async inserir(req, res) {
        const funcionario = new Funcionario({
          nome: req.body.nome,
          cpf: req.body.cpf,
          idade: req.body.idade,
          dtNascimento: req.body.dtNascimento,
          telefone: req.body.telefone,
          email: req.body.email,
          nuCarteiraMotorista: req.body.nuCarteiraMotorista,
          anoVencimentoCarteira: req.body.anoVencimentoCarteira,
        });
    
        funcionario
          .save(funcionario)
          .then((data) => {
            res.send(data);
          })
          .catch((err) => {
            res.status(500).send({
              message: err.message || "Ocorreu um erro ao inserir o funcionario.",
            });
          });
      }
};
