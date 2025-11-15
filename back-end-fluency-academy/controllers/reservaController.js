const Reserva = require("../models/Reserva");
const Cliente = require("../models/cliente");
const Carro = require("../models/Carro");

module.exports = class ReservaController {
  static async inserir(req, res) {
    const reserva = new Reserva({
      qtPassageiro: req.body.qtPassageiro,
      placaCarro: req.body.placaCarro,
      cpfCliente: req.body.cpfCliente,
      status: req.body.status,
      dtInicio: req.body.dtInicio,
      dtFim: req.body.dtFim,
    });

    reserva
      .save(reserva)
      .then((data) => {
        res.send(data);
      })
      .catch((err) => {
        res.status(500).send({
          message: err.message || "Ocorreu um erro ao inserir a reserva.",
        });
      });
  }
  // buscar pela placa do carro na url
  static async buscar(req, res) {
    Reserva.find({ placaCarro: req.query.placaCarro })
      .then((data) => res.send(data))
      .catch((err) => {
        res.status(404).send({
          message: err.message || "Erro ao buscar reserva pela placa.",
        });
      });
  }

  
  static async atualizar(req, res) {
    const id = req.query;

    Reserva.findByIdAndUpdate(id, req.body, { useFindAndModify: false }).then(
      (data) => {
        if (!data) {
          res.status(500).send({
            message: `Não foi possível atualizar a reserva com id=${id}. Talvez a reserva não tenha sido encontrada!`,
          });
        } else {
          res.send({ message: "Reserva atualizada com sucesso." });
        }
      }
    );
  }
};
