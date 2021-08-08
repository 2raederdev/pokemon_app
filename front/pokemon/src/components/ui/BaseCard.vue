<template>
  <div class="card-row">
    <div v-if="found" class="card">
      <img :src="image" alt="pokemon picture" class="card-image">
      <div class="card-footer">
        <p class="card-header">{{ headerSeparated }}</p>
        <h3 class="card-title">{{ title }}</h3>
        <div class="card-ball">
          <img   
            :class="{ 'black-white': !imageDraft}"
            src="https://res.cloudinary.com/tworaederdev/image/upload/v1628446340/pokemon_app/2-25193_pokemon-ball-transparent-background-transparent-background-pokeball-png_oyakrr_lrt1vv.png"
            alt="pokemon ball"
            @click="$emit('trigger-card-action')">
        </div>
      </div>
    </div>
    <div v-else class="card not-found">
      <img :src="image" alt="pokemon not found">
        <div class="card-footer">
        <p style="text-align: center">Sorry, but we couldn't find any pokemon that matches the given name.</p>
      </div>
    </div>
  </div>
</template>

<script>

export default {
	props: {
    found: { type: Boolean, default: true },
		image: { type: String, default: 'https://res.cloudinary.com/tworaederdev/image/upload/v1628446340/pokemon_app/image-not-found_dn3wbh_mpl6kv.png' },
		header: { type: String, default: '-' },
		title: { type: String, default: 'Not found' },
		imageDraft: { type: Boolean, default: false }
	},
  computed: {
    headerSeparated () {
      return this.header.replace(',', ' - ')
    }
  }
}
</script>

<style lang="scss" scoped>

	.card-row {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 10px 16px;

  @media (max-width: 1024px) {
    margin: 10px auto;
  }
}

.card {
  position: relative;
  height: 350px;
  width: 240px;
  background: #fff;
  border-radius: 10px;
  overflow: hidden;
  transition: 0.4s all ease-in-out;
  z-index: 1;
  box-shadow: 5px 4px 15px rgba(196, 196, 196, 0.4);
  cursor: pointer;
}

.not-found {
  display: flex;
  flex-direction: column;
}

.card-image {
  position: absolute;
  top: 0;
  height: 240px;
  width: 100%;
  object-fit: cover;
  z-index: -1;
  transition: 0.4s all ease-in-out;
}

.card-footer {
  position: absolute;
  width: 100%;
  bottom: 0;
  box-sizing: border-box;
  padding: 0 16px 8px;
}

.card-title {
  font-size: 18px;
  line-height: 21px;
  margin-top: 5px;
  margin-bottom: 1px;
}

.card-header {
  font-size: 14px;
  letter-spacing: 0.1em;
  font-weight: 400;
  color: $dark-yellow;
}

.card-header:last-child {
  letter-spacing: unset;
}

.card-ball {
  text-align: right;
  margin-right: 2px;

  img {
    width: 30px;

    &:hover {
      cursor: pointer;
    }
  }
}

.card:hover {
  height: 350px;
  width: 240px;
  box-shadow: 4px 6px 4px rgba(0, 0, 0, 0.25);
  cursor: default;
}
.card:hover img:not(.card-ball img) {
  transition: all 0.6s;
  transform: scale(1.4)
}

.card:hover .card-image {
  transition: 0.6s all cubic-bezier(0.28, 0.01, 0.3, 1.02) 0.2s;
  height: 100%;
  opacity: 0.3;
}
</style>