const characters = require('https://hp-api.onrender.com/api/character/');

exports.getCharacterHouse = (req, res) => {
    const { id } = req.query;
    const character = characters[id];
    if (character) {
        res.json({ house: character.house });
    } else {
        res.status(404).json({ error: "Character not found" });
    }
};
