<template>
    <div>
        <v-container grid-list-md text-xs-center>
            <v-layout row wrap>
            <v-flex xs6>
                <v-text-field
                class="compact-form"
                v-model="postcode"
                label="Postcode"
                ></v-text-field>
            </v-flex>
            <v-flex xs6>
                <v-text-field
                class="compact-form"
                v-model="ward"
                label="Ward Name"
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
    name: 'UserGoogleMap',
    data() {
        return {
            lng: null,
            lat: null,
            postcode: null,
            ward: null,
            message: null,
        }
    },
    methods: {
        checkWardOrPostCode: function() {
            if (this.postcode != null) {
                /* eslint-disable no-console */
                console.log(this.postcode)
                this.message = "Results for your postcode - " + this.postcode
                this.postCode = null,
                // api calls
                alert(this.postcode)
            } else {
                this.message = "Results for your ward - " + this.ward
                this.getWardData()    
                this.ward = null
            }
        },
        getWardData() {
            axios
                .get('http://127.0.0.1:5000/GetWardData', {
                    headers: {
                        wardName: this.ward
                    }
                })
                .then(response => {
                    /* eslint-disable no-console */
                    console.log("calling @", response.data)
                    return response.data
                });
        },
        getPostCodeData() {
            axios
            .get('http://127.0.0.1:5000/GetCoordinates', {
                headers: {
                    postCode: this.postCode
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