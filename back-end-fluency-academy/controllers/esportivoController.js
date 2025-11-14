const esportivo = require("../models/promocao");

module.exports = class EsportivoController {
  static async inserir(req, res) {
    console.log(req.body);
    const carro = await Carro.findOne({ placa: req.body.placa });

    const esportivo = new Esportivo({
      idCarro: carro._id,
      tp100km: req.body.tp100km,
      melhorias: req.body.melhorias,
    });

    esportivo
      .save(esportivo)
      .then((data) => {
        res.send(data);
      })
      .catch((err) => {
        res.status(500).send({
          message:
            err.message || `Ocorreu um erro ao inserir o carro esportivo: ${esportivo}.`,
        });
      });
  }
};
