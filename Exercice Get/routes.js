const express = require('express');
const router = express.Router();
const characterController = require('./controllers');

router.get('/character', characterController.getCharacterHouse);

module.exports = router;
