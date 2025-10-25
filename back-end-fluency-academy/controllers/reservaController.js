const Reserva = require('./models/Reserva');
const Cliente = require('./models/Cliente');
const Carro = require('./models/Carro');

module.exports = class ReservaController { 
    static async inserir(req, res) {
        
    }
    static async buscar(req, res) {

    }
    static async atualizar(req, res) {
        const id = req.query;

        Reserva.findByIdAndUpdate(id, req.body, { useFindAndModify: false }).then((data) => {
            if (!data) {
                res.status(500).send({
                    message: `Não foi possível atualizar a reserva com id=${id}. Talvez a reserva não tenha sido encontrada!`,
                });
            } else {
                res.send({ message: 'Reserva atualizada com sucesso.' });
            }
        });
    }
}
