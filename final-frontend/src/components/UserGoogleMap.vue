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
    name: 'UserGoogleMap',
    data() {
        return {
            lng: null,
            lat: null,
            paths: null,
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
                    postCode: this.postCode,
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