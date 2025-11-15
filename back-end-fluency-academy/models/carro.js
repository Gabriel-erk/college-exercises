const mongoose = require('mongoose');
const Carro = new mongoose.Schema({
    placa: { type: String, required: true },
    ano: { type: Number, required: true },
    modelo: { type: String, required: true },
    cor: { type: String, required: true },
    tipo: { type: String, required: true },
    quilometragem: { type: Number, required: true },
    vdiaria: { type: Number, required: true },
    observacao: { type: String, required: false }
}, {versionKey: false });

module.exports = mongoose.model('Carro', Carro);