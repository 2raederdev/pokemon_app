<template>
  <div>
    <div class="main">
      <header>
        <h1>Pokemon App</h1>
      </header>
      <section>
        <h2>Search a pokemon</h2>
        <p>Introduce the name of the pokemon you would like to add to your team and catch it!</p>
        <div class="search">
          <input type="text" v-model.trim="name" placeholder="Search pokemon">
          <BaseButton @trigger-action="search" kind="primary">
            <span v-if="!searching">Buscar</span>
            <div v-else>
              <TheLoadingBalls class="v-spinner" color="#fff" size="8px"/>
            </div>
          </BaseButton>
        </div>
      </section>
      <section>
        <div v-if="loading">
          <TheLoadingBalls class="v-spinner"/>
        </div>
        <div v-else class="filter">
          <h2>Pokemon List</h2>
          <p>This is your team!</p>
          <h3>Choose the results to be displayed</h3>
          <div class="filter__buttons">
            <BaseButton
              @trigger-action="changeFilters('caught', null)"
              kind="secondary"
              :class="{ 'selected': filters.caught === null }">
              <img   
                style="z-index: 5"
                src="https://res.cloudinary.com/tworaederdev/image/upload/v1628446340/pokemon_app/2-25193_pokemon-ball-transparent-background-transparent-background-pokeball-png_oyakrr_lrt1vv.png"
                alt="show all pokemons"
                title="show all pokemons without filtering">
              <img   
                style="margin-left: -10px"
                class="black-white"
                src="https://res.cloudinary.com/tworaederdev/image/upload/v1628446340/pokemon_app/2-25193_pokemon-ball-transparent-background-transparent-background-pokeball-png_oyakrr_lrt1vv.png"
                alt="show all pokemons"
                title="show all pokemons without filtering">
            </BaseButton>
            <BaseButton
              @trigger-action="changeFilters('caught', true)"
              kind="secondary"
              :class="{ 'selected': filters.caught === true }">
              <img   
                src="https://res.cloudinary.com/tworaederdev/image/upload/v1628446340/pokemon_app/2-25193_pokemon-ball-transparent-background-transparent-background-pokeball-png_oyakrr_lrt1vv.png"
                alt="show all pokemons"
                title="show all pokemons without filtering">
            </BaseButton>
            <BaseButton 
              @trigger-action="changeFilters('caught', false)"
              kind="secondary"
              :class="{ 'selected': filters.caught === false }">
              <img   
                class="black-white"
                src="https://res.cloudinary.com/tworaederdev/image/upload/v1628446340/pokemon_app/2-25193_pokemon-ball-transparent-background-transparent-background-pokeball-png_oyakrr_lrt1vv.png"
                alt="show all pokemons"
                title="show all pokemons without filtering">
            </BaseButton>
          </div>
          <div class="pokemon-list">
            <div v-for="pok in pokemonList" :key="pok.name" >
              <BaseCard 
                :image="pok.image_url"
                :title="pok.name"
                :header="pok.types"
                :imageDraft="pok.caught"
                @trigger-card-action="catchPokemon(pok)" />
            </div>
          </div>
        </div>
      </section>
    </div>
    <template v-if="isModalOpen">
      <TheModal :isModalOpen="isModalOpen" @cancel="hideModal">
        <BaseCard
          :image="isPokemonFound ? pokemon.image_url : pokemonNotFound.image_url"
          :title="isPokemonFound ? pokemon.name : pokemonNotFound.name"
          :header="isPokemonFound ? pokemon.types : pokemonNotFound.types"
          :imageDraft="isPokemonCaught(pokemon.api_id)"
          :found="isPokemonFound"
          @trigger-card-action="catchPokemon(pokemon)" />
      </TheModal>
    </template>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

import TheLoadingBalls from '@/components/shared/TheLoadingBalls.vue'
import TheModal from '@/components/shared/TheModal.vue'


export default {
  components: {
    TheLoadingBalls,
    TheModal
  },
  data () {
    return {
      loading: true,
      searching: false,
      name: '',
      list: true,
      isPokemonFound: false,
      isModalOpen: false,
      pokemonNotFound: {
        image_url: 'https://res.cloudinary.com/tworaederdev/image/upload/v1628446340/pokemon_app/image-not-found_dn3wbh_mpl6kv.png',
        name: 'Not found',
        types: '-'
      }
    }
  },
  computed: {
    ...mapGetters({
      pokemon: 'pokemons/getPokemon',
      pokemonList: 'pokemons/getPokemonList',
      filters: 'pokemons/getFilters',
    }),

  },
  async created () {
    await this.$store.dispatch('pokemons/getPokemonList', this.filters)  
    this.loading = false
  },
  methods: {
    isPokemonCaught (api_id) {
      if(!this.isPokemonFound) return false

      const pokemonFound = this.pokemonList.filter(p => p.api_id === api_id)
      
      return pokemonFound.length 
        ? pokemonFound[0].caught
        : false
    },
    async search () {
      if (!this.name.length) return
      try {
        this.searching = true
        await this.$store.dispatch('pokemons/getPokemon', this.name)
        this.isPokemonFound = Object.keys(this.pokemon).length !== 0
        this.isModalOpen = true
        if (this.isPokemonFound) {
          this.$store.commit('pokemons/ADD_POKEMON', this.pokemon)
        }
      } catch (error) {
        console.log(error)
      } finally {
        this.searching = false
      }
    },
    hideModal () {
      this.isModalOpen = false
      this.isPokemonFound = false
      this.name = ''
    },
    async catchPokemon (pokemon) {
      try {
        await this.$store.dispatch('pokemons/catchPokemon', pokemon)
      } catch (error) {
        console.log(error)
      }
    },
    changeFilters (field, value) {
      const filters = { ...this.filters, ...{[field]: value } }
      this.$store.commit('pokemons/SET_FILTERS', filters)
      try {
        this.$store.dispatch('pokemons/getPokemonList', this.filters) 
      } catch (error) {
        console.log(error)
      } 
    }
  }
}
</script>

<style lang="scss" scoped>
.main {
  width: 960px;
  margin: 0 auto;
}

h1, h2, p {
  text-align: center;
}

h1 {
  color: #ffd400;
  font-size: 48px;
  margin-bottom: 48px;
}

section {
  margin-bottom: 40px;
}

.search {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: baseline;

    input {
      width: 75%;
      height: 42px;
      padding: 0 10px;
      border: $dark-grey;
      border-radius: 10px;
      background-color: $cloud;
    }
}

.filter {

  h2, h3, p {
    text-align: center;
  }

  h3 {
    margin-bottom: 0;
  }

  &__buttons {
    margin-bottom: 20px;
    display: flex;
    flex-direction: row;
    justify-content: center;
  }

  img {
    width: 30px;
  }
}

.pokemon-list {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
}

.v-spinner {
  text-align: center;
}

.selected {
  background-color: $cloud !important;
  border: 2px solid $light-grey !important
}

@media (max-width: 1024px) {
  .main {
    width: 420px;
  }

  .search {
    flex-direction: column;

    input {
      position: absolute;
      left: 0;
      right: 0;
      margin: 0 auto;
    }

    button {
      margin: 60px auto 20px auto;
    }
  }

  .filter {
    &__buttons {
      padding: 16px;

      button {
        margin: 8px 4px !important;
        width: 90px !important;
      }
    }
  }
}

@media (max-width: 440px) {
  .main {
    width: 330px;
    margin: 0 auto;
  }
}

</style>