<template>
  <div class="modal" :class="{ 'modal--show': isModalOpen }" @click="$emit('cancel')">
    <slot></slot>
  </div>
</template>

<script>
export default {
  props: {
    isModalOpen: {
      type: Boolean,
      default: false
    },
    closeModalX: {
      type: Boolean,
      default: true
    },
    widthPx: {
      type: String,
      default: '671px'
    }
  },
  computed: {
    style () {
      return `max-width: ${this.widthPx}`
    }
  },
}
</script>

<style lang="scss" scoped>
 .modal {
  left: -9999px;
  opacity: 0;
  transition: .1s opacity;
  background-color: rgba(0,0,0,.3);
  backdrop-filter: blur(1px);
  z-index: 9998;
  display: grid;
  place-items: center;
  padding: 0;
  width:      100%;
  height:     100%; 
  z-index:    10;
  top:        0; 
  left:       0; 
  position:   fixed; 

  &--show {
    left: 0;
    opacity: 1;
  }

 }

</style>
