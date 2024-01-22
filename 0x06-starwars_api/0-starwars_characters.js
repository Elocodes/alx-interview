#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
//
// The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name per line in the same order as the “characters” list in the /films/ endpoint
// You must use the Star wars API
// You must use the request module

const req = require('request');

const fetchCharacterData = (characterUrl) => {
  return new Promise((resolve, reject) => {
    req(characterUrl, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

const fetchAndPrintCharacters = async (movieUrl) => {
  try {
    const movieData = await new Promise((resolve, reject) => {
      req(movieUrl, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });

    const characterUrls = movieData.characters;
    const characterDataArray = await Promise.all(characterUrls.map(fetchCharacterData));

    // Sort characters based on their appearance order in the movie
    const sortedCharacterData = characterDataArray.sort((a, b) => {
      return characterUrls.indexOf(a.url) - characterUrls.indexOf(b.url);
    });

    // Print character names
    sortedCharacterData.forEach((characterData) => {
      console.log(characterData.name);
    });
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};

const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide the Movie ID as a command line argument.');
  process.exit(1);
}

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
fetchAndPrintCharacters(movieUrl);
