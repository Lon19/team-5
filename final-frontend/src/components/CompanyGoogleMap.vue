<template>
    <div>
        <div></div>
        <h1></h1>
        <h1>Unemployment Rate Between Wards</h1>
        <v-container grid-list-md text-xs-center>
            <v-layout row wrap>
            <v-flex xs6>
                <v-text-field
                class="compact-form"
                v-model="postcode1"
                label="Postcode One"
                ></v-text-field>
            </v-flex>
            <v-flex xs6>
                <v-text-field
                class="compact-form"
                v-model="postcode2"
                label="Postcode Two"
                ></v-text-field>
            </v-flex>
            </v-layout>
        </v-container>

        <v-btn large center color="primary"
        v-on:click="compareWards">Primary</v-btn>
        <p>{{message}}</p>

          <gmap-map
                :center="center"
                :zoom="10"
                style="width:100%;  height: 400px;"
        >
            <!-- <gmap-polygon
                    v-for="(pin, index) in paths"
                    :key=index
                    :paths=pin.position
                    :options="{fillColor: '#f70539', fillOpacity:0.2}"
            >
            </gmap-polygon> -->
        </gmap-map>
    </div>
</template>

<script>
/* eslint-disable */
    import axios from 'axios'
export default {
    name: 'CompanyGoogleMap',
    data() {
        return {
            center: {lat: 53.43198013, lng: -2.95573997},
            postcode1: null,
            postcode2: null,
            message: null,
        }
    },
    methods: {
        compareWards: function() {
            
        },
        getPostCodeData() {
            axios
            .get('http://127.0.0.1:5000/GetCoordinates', {
                headers: {
                    postCode: this.postCode,
                    nearests: 5
                }
            })
            .then(response => {
            /* eslint-disable no-console */
            console.log(response.data)
            });
        }
    }
    
}
</script>

<style scoped>
    .compact-form {
    transform: scale(0.875);
    transform-origin: left;
}
</style>