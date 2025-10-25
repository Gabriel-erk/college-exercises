const express = require('express');
// dizendo que o arquivo vai ser uma rota
const router = express.Router();
const UtilitarioController = require('../controllers/utilitarioController');

// rota para criar um novo utilitário, dizendo qu quero receber dados via post
router.post('/utilitario', UtilitarioController.inserir);

module.exports = router;    