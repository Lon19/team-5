<template>
    <div>
        <div></div>
        <h1></h1>
        <h1>Highest Unemployment Rate Between Wards</h1>
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
        v-on:click="checkWardOrPostCode">Primary</v-btn>
        <p>{{message}}</p>
    </div>
</template>

<script>
/* eslint-disable */
    import axios from 'axios'
export default {
    name: 'CompanyGoogleMap',
    data() {
        return {
            postcode1: null,
            postcode2: null,
            ward: null,
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