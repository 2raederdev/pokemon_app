<template>
  <section>
    <img src="https://res.cloudinary.com/tworaederdev/image/upload/v1628446340/pokemon_app/404_Error-amico_v7kzsa_ny5ugd_p5ab20.svg" alt="error">
    <h2>Oops! This page doesn’t seem to exist.</h2>
    <p>But, don't panic! Yo cann still go to the <router-link to="/">home page</router-link>.</p>
  </section>
</template>

<style scoped>
section {
  display: flex;
  flex-direction: column;
  margin: 0 auto;
  text-align: center;
}
img {
  margin: 40px auto;
  width: 400px;
}

h2 {
  margin: 0;
}
</style>