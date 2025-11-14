const cliente = require("./models/cliente");

module.exports = class ClienteController {
  static async inserir(req, res) {
    const cliente = new Cliente({
      nome: req.body.nome,
      cpf: req.body.cpf,
      idade: req.body.idade,
      dtNascimento: req.body.dtNascimento,
      telefone: req.body.telefone,
      email: req.body.email,
      nuCarteiraMotorista: req.body.nuCarteiraMotorista,
      anoVencimentoCarteira: req.body.anoVencimentoCarteira,
    });

    cliente
      .save(cliente)
      .then((data) => {
        res.send(data);
      })
      .catch((err) => {
        res.status(500).send({
          message: err.message || "Ocorreu um erro ao inserir o cliente.",
        });
      });
  }

//   static async inserir(req, res) {
//     console.log(req.body);

//     const pessoa = new Pessoa({
//       nome: req.body.nome,
//       cpf: req.body.cpf,
//       idade: req.body.idade,
//       dtNascimento: req.body.dtNascimento,
//       telefone: req.body.telefone,
//       email: req.body.email,
//       nuCarteiraMotorista: req.body.nuCarteiraMotorista,
//       anoVencimentoCarteira: req.body.anoVencimentoCarteira,
//     });

//     pessoa.save(pessoa).then((data) => {
//       const cliente = new Cliente({
//         idPessoa: data._id,
//         nuCarteiraMotorista: req.body.nuCarteiraMotorista,
//         anoVencimentoCarteira: req.body.anoVencimentoCarteira,
//       });

//       cliente.save(cliente).then(data => {
//         res.send(data);
//       }).catch(err => {
//         res.status(500).send({
//           message: err.message || "Ocorreu um erro ao inserir o cliente.",
//         });
//       });
//     });
//   }
};
