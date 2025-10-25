const Utilitario = require("../models/utilitario");

module.exports = class UtilitarioController {
  static async inserir(req, res) {
    try {
        res.send(new Utilitario('ABC-1234', 2020, 'Prata', 'Fiat Toro', 15000, 250, 'Em ótimo estado', 5, '500L', 12));
    } catch (error) {
        // .send indica o envio de uma responsta
        res.status(500).send({ error: error.message  || 'Erro ao inserir utilitário.' });
    }
  }
};
