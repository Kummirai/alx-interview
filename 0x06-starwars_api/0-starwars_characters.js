// #!/usr/bin/node

// const request = require('request');

// const movieId = process.argv[2];

// const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// request(url, async (err, res, body) => {
//   err && console.log(err);

//   const charactersArray = (JSON.parse(res.body).characters);
//   for (const character of charactersArray) {
//     await new Promise((resolve, reject) => {
//       request(character, (err, res, body) => {
//         err && console.log(err);

//         console.log(JSON.parse(body).name);
//         resolve();
//       });
//     });
//   }
// });


const request = require('request');

function getCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;

    request(url, { json: true }, (err, res, body) => {
        if (err) {
            return console.log(`Error: Unable to fetch data for movie ID ${movieId}`);
        }

        const characters = body.characters;
        characters.forEach(characterUrl => {
            request(characterUrl, { json: true }, (err, res, characterBody) => {
                if (err) {
                    return console.log(`Error: Unable to fetch character data from ${characterUrl}`);
                }
                console.log(characterBody.name);
            });
        });
    });
}

const movieId = process.argv[2];
if (!movieId) {
    console.log("Usage: node script.js <movie_id>");
} else {
    getCharacters(movieId);
}