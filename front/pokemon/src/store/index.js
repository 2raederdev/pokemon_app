import { createStore } from 'vuex'

import pokemonsModule from '@/store/modules/pokemons/index.js'


const store = createStore({
  modules: {
    pokemons: pokemonsModule
  }
})

export default store