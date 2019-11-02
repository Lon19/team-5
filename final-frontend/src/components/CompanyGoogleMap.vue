<template>
    <div>

        <v-container grid-list-md text-xs-center>
            <v-layout row wrap>
                <v-flex xs6>
                    <v-text-field
                            class="compact-form"
                            v-model="postcode1"
                            label="Postcode"
                    ></v-text-field>
                </v-flex>
                <v-flex xs6>
                    <v-text-field
                            class="compact-form"
                            v-model="wardName"
                            label="Ward Name"
                    ></v-text-field>
                </v-flex>
                <v-flex xs6>
                    <v-text-field
                            class="compact-form"
                            v-model="unemployemntRate"
                            label="Unemployment Rate >"
                    ></v-text-field>
                </v-flex>
                <v-flex xs6>
                    <v-text-field
                            class="compact-form"
                            v-model="limit"
                            label="Limit Highest >"
                    ></v-text-field>
                </v-flex>
                <p>Gender</p>
                <v-radio-group v-model="radios" :mandatory="false">
                    <v-radio label="Male" value="Male"></v-radio>
                    <v-radio label="Female" value="Female"></v-radio>
                    <v-radio label="Total" value="Total"></v-radio>
                </v-radio-group>
            </v-layout>
        </v-container>




        <v-row style="justify-content: space-evenly">
            <v-btn large center color="primary"
                   v-on:click="getWardsByPostcode(postcode1)">Postcode
            </v-btn>

            <v-btn large center color="primary"
                   v-on:click="getByWardName(wardName)">Ward Name
            </v-btn>
            <v-btn large center color="primary"
                   v-on:click="getByUnemploymentRate(unemployemntRate)">Uneployment Rate
            </v-btn>
            <v-btn large center color="primary"
                   v-on:click="getHighest(limit)">Get Highest
            </v-btn>
        </v-row>





        <gmap-map
                :center="center"
                :zoom="10"
                style="width:100%;  height: 800px;"
        >
            <gmap-polygon
                    v-for="(pin, index) in paths"
                    :key=index
                    :label=pin.name
                    :paths=pin.position
                    :options=pin.options
            >
            </gmap-polygon>
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
                center: {lat: 51.5074, lng: 0.1278},
                zoom: 2,
                paths: [],
                postcode1: null,
                wardName: null,
                unemployemntRate: null,
                limit: null,
                radios: "Total",

            }
        },
        methods: {
            getWardsByPostcode(postcode) {
                this.clear();
                axios
                    .get('http://127.0.0.1:5000/GetCoordinates', {
                        headers: {
                            postCode: postcode.replace(/\s/g,''),
                            nearests: 500
                        }
                    })
                    .then(response => {
                        let arrayResponse = response.data.data;
                        //console.log(arrayResponse);
                        arrayResponse.forEach(function (item) {
                            let cordsString = item.coordinates;
                            //console.log(cordsString);
                            let position = this.buildCoordinatesArrayFromString(cordsString);

                            let options = this.decideColour(item[this.radios]);
                            let name = item.name;
                            let temp = {
                                name: name, position, options
                            };
                            this.paths.push(temp)
                        }.bind(this))


                    });
            },
            clear(){
                this.paths = [];
            },
            getByWardName(wardName) {
                this.clear();
                axios
                    .get('http://127.0.0.1:5000/GetWardData', {
                        headers: {
                            wardName: wardName
                        }
                    })
                    .then(response => {
                        let jsonData = response.data.data.coordinates;
                        let options = this.decideColour(response.data.data[this.radios]);
                        let position = this.buildCoordinatesArrayFromString(jsonData);
                        //console.log(position,"ward NAME");
                        let temp = {
                            name: wardName, position, options
                        };
                        this.paths.push(temp)

                    });
            },

            getByUnemploymentRate(un) {
                this.clear();
                axios
                    .get('http://127.0.0.1:5000/GetWardsUnemployment', {
                        headers: {
                            unemployment_number: un.replace(/\s/g,''),
                            gender: this.radios
                        }
                    })
                    .then(response => {
                        let arrayResponse = response.data.data;
                        //console.log(arrayResponse);
                        arrayResponse.forEach(function (item) {
                            let cordsString = item.coordinates;
                            //console.log(cordsString);
                            let position = this.buildCoordinatesArrayFromString(cordsString);
                            //console.log(position);

                            let options = this.decideColour(item[this.radios]);
                            let name = item.name;
                            let temp = {
                                name: name, position, options
                            };
                            this.paths.push(temp)
                        }.bind(this))

                    });
            },
            getHighest(limit) {
                this.clear();
                axios
                    .get('http://127.0.0.1:5000/GetHighest', {
                        headers: {
                            limit: limit.replace(/\s/g,''),
                        }
                    })
                    .then(response => {
                        let arrayResponse = response.data.data;
                        //console.log(arrayResponse);
                        arrayResponse.forEach(function (item) {
                            let cordsString = item.coordinates;
                            //console.log(cordsString);
                            let position = this.buildCoordinatesArrayFromString(cordsString);
                            //console.log(position);

                            let options = this.decideColour(item[this.radios]);
                            let name = item.name;
                            let temp = {
                                name: name, position, options
                            };
                            this.paths.push(temp)
                        }.bind(this))

                    });
            },
            buildCoordinatesArrayFromString(MultiGeometryCoordinates) {
                var finalData = [];
                var grouped = MultiGeometryCoordinates.split(" ");


                grouped.forEach(function (item, i) {
                    let a = item.trim().split(',');

                    finalData.push({
                        lng: parseFloat(a[0]),
                        lat: parseFloat(a[1])
                    });
                });
                //console.log(finalData,"TESTTT");


                return finalData;
            },
            decideColour(num) {
                if (num < 50) {
                    return {fillColor: '#94949f', fillOpacity: 0.5}
                } else if (num > 50 && num < 100) {
                    return {fillColor: '#01e900', fillOpacity: 0.5}
                }
                else if (num > 100 && num < 150) {
                    return {fillColor: '#168200', fillOpacity: 0.5}
                }
                else if (num > 150 && num < 200) {
                    return {fillColor: '#e8e900', fillOpacity: 0.5}
                }
                else if (num > 200 && num < 300) {
                    return {fillColor: '#e97600', fillOpacity: 0.5}
                }
                else {
                    return {fillColor: '#c20400', fillOpacity: 0.5}
                }
            },

        },


    }
</script>

<style scoped>
    .compact-form {
        transform: scale(0.875);
        transform-origin: left;
    }
</style>