const Esportivo = require("../models/esportivo");
const Carro = require("../models/Carro");

module.exports = class EsportivoController {
  static async inserir(req, res) {
    try {
      console.log(req.body);

      // achar o carro pela placa
      const carro = await Carro.findOne({ placa: req.body.placa });

      if (!carro) {
        return res.status(404).send({ message: "Carro não encontrado." });
      }

      // criar objeto esportivo corretamente
      const novoEsportivo = new Esportivo({
        idCarro: carro._id,
        tp100km: req.body.tp100km,
        melhorias: req.body.melhorias,
      });

      const data = await novoEsportivo.save();

      res.send(data);
    } catch (err) {
      res.status(500).send({
        message:
          err.message ||
          "Ocorreu um erro ao inserir o carro esportivo.",
      });
    }
  }
};
