<template>
  <div>
    <TheNavBar></TheNavBar>
    <router-view></router-view>
  </div>
</template>

<script>
import TheNavBar from '@/components/shared/TheNavBar.vue'

export default {
  name: 'App',
  components: {
    TheNavBar
  },
  beforeCreate () {
    document.title = 'Pokemon App'
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Nunito&display=swap');

html, body, #app {
  margin: 0;
  padding: 0;
}

#app {
  font-family: 'Nunito', Helvetica, Arial, sans-serif;
  color: $black-title;
  padding-top: 80px;
  margin: 0 auto;
}

p {
  font-weight: 500;
}
</style>
