const mongoose = require("mongoose");

const Reserva = new mongoose.Schema(
  {
    qtPassageiro: { type: Number, required: true },

    // Se quiser relacionar pelo ID do carro, deveria ser ObjectId.
    placaCarro: { type: String, ref: "Carro", required: false },

    // Aqui também: se o cliente fosse por ID, seria ObjectId.
    cpfCliente: { type: String, ref: "Cliente", required: true },

    status: { type: Boolean, required: true },
    dtInicio: { type: Date, required: true },
    dtFim: { type: Date, required: true },
  },
  { versionKey: false }
);

module.exports = mongoose.model("Reserva", Reserva);
