<template>
  <button v-if="!link" @click.prevent="triggerAction" :class="kind">
    <slot></slot>
  </button>
  <router-link v-else :to="to">
    <slot></slot>
  </router-link>
</template>

<script>
export default {
  props: {
    link: {
      type: Boolean,
      required: false,
      default: false
    },
    to: {
      type: String,
      required: false,
      default: '/'
    },
    kind: {
      type: String,
      required: false,
      default: 'primary'
    }
  },
  methods: {
    triggerAction () {
      this.$emit('trigger-action')
    }
  }
}
</script>

<style scoped lang="scss">

button, a {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 42px;
  width: 180px;
  padding: 0.75rem 1.5rem;
  background-color: $medium-yellow;
  font-weight: 800;
  font-size: 16px;
  color: #fff;
  border: none;
  cursor: pointer;
  border-radius: 10px;
  margin: 20px 8px 20px 0;

  &:hover, &:active, &:focus {
    background-color: $light-yellow;
  }

  a {
    text-decoration: none;
    color: #fff;
  }
}

.primary {
  background-color: $medium-yellow;
  border: $medium-yellow;

  &:hover, &:active, &:focus {
    background-color: $light-yellow;
    border: $light-yellow;
  }
}

.secondary {
  background-color: #fff;
  border: 1px solid $light-grey;

  &:hover, &:active, &:focus {
    background-color: $light-grey;
    border: $light-grey;
  }
}

</style>