<template>
  <div class="home">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <GoogleMap />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import GoogleMap from '@/components/GoogleMap.vue'

export default {
  name: 'home',
  components: {
    HelloWorld,
    GoogleMap
  }
}
</script>
