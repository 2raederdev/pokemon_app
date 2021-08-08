import * as api from '@/api'

export default {
  namespaced: true,
  state () {
    return {
      pokemon: null,
      pokemonList: [],
      filters: {
        order: 'created_at',
        descending: true,
        caught: null
      },
    }
  },
  getters: {
    getPokemon (state) {
      return state.pokemon
    },
    getPokemonList (state) {
      return state.pokemonList
    },
    getFilters(state) {
      return state.filters
    },
  },
  mutations: {
    SET_POKEMON (state, data) {
      state.pokemon = data
    },
    SET_POKEMON_LIST (state, data) {
      state.pokemonList = data
    },
    SET_CAUGHT_POKEMON (state, pokemon) {
      const index = state.pokemonList.findIndex(p => p.id === pokemon.id)
      state.pokemonList[index].caught = !state.pokemonList[index].caught
    },
    SET_FILTERS (state, data) {
      state.filters = data
    },
    ADD_POKEMON (state, pokemon) {
      state.pokemonList.unshift(pokemon)
    }
  },
  actions: {
    async getPokemon ({ state, commit }, name) {
      let res = await api.getPokemon(name)
      commit('SET_POKEMON', res.data)
    },
    async getPokemonList ({ state, commit }, filters) {
      let res = await api.getPokemonList(filters)
      commit('SET_POKEMON_LIST', res.data)
    },
    async catchPokemon ({ state, commit }, pokemon) {
      const id = pokemon.id
      const caught = !pokemon.caught

      try {
        let res = await api.updatePokemon({ id, caught })
        commit('SET_CAUGHT_POKEMON', res.data)
      } catch (error) {
        console.log(error)
      }
    }
  },
}