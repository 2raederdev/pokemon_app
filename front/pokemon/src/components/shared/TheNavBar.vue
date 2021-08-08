<template>
	<header class="navbar">
		<nav>
			<router-link to="/" class="nav-logo">
				<img src="https://res.cloudinary.com/tworaederdev/image/upload/v1628446340/pokemon_app/pokemon_logo_or5baa_moamj8.svg" alt="App logo">
			</router-link>
		</nav>
	</header>
</template>

<script>
export default {

}
</script>

<style scoped lang="scss">
.navbar {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
  background-color: #fff;
  box-shadow: 0 2px 8px 0 rgba(60, 24, 226, 0.09);
  display: flex;
  align-items: center;
  justify-content: center;
  height: 60px;
  font-weight: 700;

  img {
    width: 40px;
		padding-top: 6px;
  }

  a {
    color: $black-title;
    text-decoration: none;
    display: inline-block;
    padding: 0 20px;
    border: 1px solid transparent;

      &:active:not(.nav-logo), &:hover:not(.nav-logo), &.router-link-active:not(.nav-logo) {
        border: 1px solid $black-title;
      }

  }

  nav {
    width: 90%;
    margin: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;

    ul {
      list-style: none;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;

      li {
        margin: 0 8px;
      }
    }
  }
}
</style>