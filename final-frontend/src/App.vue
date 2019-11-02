<!--
<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Vuetify</span>
        <span class="font-weight-light">MATERIAL DESIGN</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        text
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
        <span class="mr-2">Latest Release</span>
      </v-btn>
    </v-app-bar>

    <v-content>
      <HelloWorld/>
    </v-content>
  </v-app>
</template>
-->

<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
    <div class="app">
    <v-app>
        <v-app-bar 
                color=""
                dark
        >
            <v-app-bar-nav-icon></v-app-bar-nav-icon>

            <v-toolbar-title>Page title</v-toolbar-title>

            <v-spacer></v-spacer>

        </v-app-bar>
        <v-content>
            <UserGoogleMap />
            <HelloWorld/>
        </v-content>
    </v-app>
    </div>
</template>

<script>
    import HelloWorld from './components/HelloWorld';
    import UserGoogleMap from './components/UserGoogleMap';

    export default {
        name: 'App',
        components: {
            UserGoogleMap,
            HelloWorld,
        },
        data: () => ({
            //
        }),
    };
</script>

<style scoped>
    .app {
        min-height: 10px;
        max-height: 20px;
    }
</style>
