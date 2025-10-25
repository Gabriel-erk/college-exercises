class Utilitario extends Carro {
    constructor(placa, cor, ano, modelo, quilometragem, vdiaria, observacao, qtPassageiro, tmBagageiro, kmLitro) {
        super(placa, cor, ano, modelo, quilometragem, vdiaria, observacao);
        this.qtPassageiro = qtPassageiro;
        this.tmBagageiro = tmBagageiro;
        this.kmLitro = kmLitro;
    }
}