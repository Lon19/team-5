<template>
    <div>

        <gmap-map
                :center="center"
                :zoom="10"
                style="width:100%;  height: 400px;"
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
        name: 'GoogleMap',
        data() {
            return {
                info: null,
                center: {lat: 53.801699, lng: -1.583097},
                zoom: 2,
                paths: []
            };

        },

        mounted() {
           console.log("mounted");
           this.getByWardName("heston central");
        },

        methods: {
            decideColour(num) {
                if (num < 100) {
                    return {fillColor: '#6ec20b', fillOpacity: 0.5}
                } else if (num > 100 && num < 150) {
                    return {fillColor: '#c2b700', fillOpacity: 0.5}
                } else {
                    return {fillColor: '#c20400', fillOpacity: 0.5}
                }
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

                return finalData;
            },
            postcodeSearch(postcode) {
                axios
                    .get('http://127.0.0.1:5000/GetCoordinates', {
                        headers: {
                            postCode: "TW59DA",
                            nearests: 2
                        }
                    })
                    .then(response => {
                        let arrayResponse = response.data.data;
                        arrayResponse.forEach(function (item) {
                            let cordsString = item.coordinates;
                            console.log(cordsString);
                            let position = this.buildCoordinatesArrayFromString(cordsString);
                            let options = this.decideColour(item.Total);
                            let name = item.name;
                            let temp = {
                                name: name, position, options
                            };
                            this.paths.push(temp)
                        });


                    });
            },
            getByWardName(wardName) {
                axios
                    .get('http://127.0.0.1:5000/GetWardData', {
                        headers: {
                            wardName: wardName
                        }
                    })
                    .then(response => {
                        let jsonData = response.data.data.coordinates;
                        let options = this.decideColour(response.data.data.Total);
                        let position = this.buildCoordinatesArrayFromString(jsonData);
                        //console.log(jsonData);
                        let temp = {
                            name: wardName, position, options
                        };
                        this.paths.push(temp)

                    });
            }


        }
    };

</script>

<style scoped>

</style>