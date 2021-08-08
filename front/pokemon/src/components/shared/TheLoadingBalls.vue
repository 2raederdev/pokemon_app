<template>
  <div>
    <div class="v-sync v-sync1" :style="[spinnerStyle, spinnerDelay1]"></div>
    <div class="v-sync v-sync2" :style="[spinnerStyle, spinnerDelay2]"></div>
    <div class="v-sync v-sync3" :style="[spinnerStyle, spinnerDelay3]"></div>
  </div>
</template>

<script>
export default {
  name: 'Loader',
  props: {
    color: { type: String, default: '#ffd400' },
    size: { type: String, default: '16px' },
     

  },
  data() {
    return {
      spinnerStyle: {
        backgroundColor: this.color,
        height: this.size,
        width: this.size,
        margin: '2px',
        borderRadius: '100%',
        display: 'inline-block',
        animationName: 'v-syncStretchDelay',
        animationDuration: '0.6s',
        animationIterationCount: 'infinite',
        animationTimingFunction: 'ease-in-out',
        animationFillMode: 'both'
      },
      spinnerDelay1: {
        animationDelay: '0.07s'
      },
      spinnerDelay2: {
        animationDelay: '0.14s'
      },
      spinnerDelay3: {
        animationDelay: '0.21s'
      }
    }
  }
}
</script>

<style>
@-webkit-keyframes v-syncStretchDelay {
  33% {
    -webkit-transform: translateY(10px);
    transform: translateY(10px);
  }
  66% {
    -webkit-transform: translateY(-10px);
    transform: translateY(-10px);
  }
  100% {
    -webkit-transform: translateY(0);
    transform: translateY(0);
  }
}
@keyframes v-syncStretchDelay {
  33% {
    -webkit-transform: translateY(10px);
    transform: translateY(10px);
  }
  66% {
    -webkit-transform: translateY(-10px);
    transform: translateY(-10px);
  }
  100% {
    -webkit-transform: translateY(0);
    transform: translateY(0);
  }
}
</style>
