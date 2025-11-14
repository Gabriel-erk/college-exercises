const mongoose = require("mongoose");

const UtilitarioSchema = new mongoose.Schema(
  {
    idCarro: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "Carro",
      required: true,
    },
    qtPassageiro: { type: Number, required: true },
    tmBagageiro: { type: Number, required: true },
    kmLitro: { type: Number, required: true },
  },
  { versionKey: false }
);

module.exports = mongoose.model("Utilitario", UtilitarioSchema);
