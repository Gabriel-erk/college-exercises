const mongoose = require("mongoose");

const EsportivoSchema = new mongoose.Schema(
  {
    idCarro: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "Carro",
      required: true,
    },
    tp100km: { type: Number, required: true },
    melhorias: { type: [String], required: true },
  },
  { versionKey: false }
);

module.exports = mongoose.model("Esportivo", EsportivoSchema);
