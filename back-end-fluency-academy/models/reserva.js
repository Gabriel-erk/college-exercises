const mongoose = require("mongoose");
const Reserva = mongoose.Schema;
({
  qtPassageiro: { type: Number, required: true },
  placaCarro: { type: String, ref: "Carro", required: false },
  cpfCliente: { type: String, ref: "Cliente", required: true },
  status: { type: Boolean, required: true },
  dtInicio: { type: Date, required: true },
  dtFim: { type: Date, required: true },
}),
  { versionKey: false };

module.exports = mongoose.model("Reserva", Reserva);
