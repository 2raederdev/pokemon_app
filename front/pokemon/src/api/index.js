import axios from 'axios'

const BASE_URL = `${process.env.VUE_APP_BASE_URL}api/v1/pokemons`

function getPokemon (name) {
  let URL = `${BASE_URL}/${name}`
  return axios.get(URL)
}

function getPokemonList (params) {
  let addParams = { params }
  let URL = `${BASE_URL}`
  return axios.get(URL, addParams)
}

function updatePokemon ({ id, caught }) {
  const pokemon_id = id
  const pokemon_caught = caught

  let URL = `${BASE_URL}/${pokemon_id}`
  const data = { 'caught': pokemon_caught }
 
  return axios.patch(URL, data)
}

export {
    getPokemon,
    getPokemonList,
    updatePokemon
}
