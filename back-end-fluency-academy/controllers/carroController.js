const Carro = require("../models/Carro");

module.exports = class CarroController {
  static async inserir(req, res) {
    const carro = new Carro({
      placa: req.body.placa,
      ano: req.body.ano,
      modelo: req.body.modelo,
      cor: req.body.cor,
      tipo: req.body.tipo,
      quilometragem: req.body.quilometragem,
      vdiaria: req.body.vdiaria,
      observacao: req.body.observacao,
    });

    carro
      .save(carro)
      .then((data) => {
        res.send(data);
      })
      .catch((err) => {
        res.status(500).send({
          message: err.message || "Ocorreu um erro ao inserir o carro.",
        });
      });
  }

  static async buscarPeloTipo(req, res) {
    Carro.find({ tipo: req.query.tipo })
      .then((data) => res.send(data))
      .catch((err) => {
        res.status(404).send({
          message: err.message || "Ocorreu um erro ao buscar carros pelo tipo.",
        });
      });
  }

  static async buscarPelaPlaca(req, res) {
    Carro.find({ placa: req.query.placa })
      .then((data) => res.send(data))
      .catch((err) => {
        res.status(404).send({
          message:
            err.message || "Ocorreu um erro ao buscar carros pela placa.",
        });
      });
  }

  static async deletar(req, res) {
    const id = req.query.id;

    Carro.findByIdAndDelete(id, { useFindAndModify: false })
      .then((data) => {
        if (!data) {
          res.status(404).send({
            message: `Não foi possível deletar o carro com id=${id}. Talvez o carro não tenha sido encontrado!`,
          });
        } else {
          res.send({
            message: "Carro deletado com sucesso!",
          });
        }
      })
      .catch((err) => {
        res.status(500).send({
          message:
            err.message || `Ocorreu um erro ao deletar o carro pela id: ${id}.`,
        });
      });
  }
};
