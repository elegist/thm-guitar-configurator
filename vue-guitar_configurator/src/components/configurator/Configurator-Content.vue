<script setup>
    import RadioButton from './Radio-Button.vue';
</script>

<template>
    <div class="container-fluid text-center h-100">
        <div class="configurator-body row d-block d-lg-flex text-center">
            <div class="img-container col-lg-3">
                <img src="" alt="" class="img-fluid img-guitar-preview d-none d-lg-block">
                <img src="" alt="" class="img-fluid img-guitar-preview d-lg-none">
            </div>
            <div class="col-lg-9 input-col">
                <div class="options-container overflow-auto my-2">
                    <!-- <form id="configuratorForm" method="POST">

                    <template v-if="step == 1">
                        <template v-for="configuratorItem in Misc" :key="configuratorItem.id">
                            <RadioButton :configuratorItem="configuratorItem"/>
                        </template>
                    </template>

                    <template v-if="step == 2">
                        <template v-for="configuratorItem in Frets" :key="configuratorItem.id">
                            <RadioButton :configuratorItem="configuratorItem"/>
                        </template>
                    </template>

                    <template v-if="step == 3">
                        <template v-for="configuratorItem in Colors" :key="configuratorItem.id">
                            <RadioButton :configuratorItem="configuratorItem"/>
                        </template>
                    </template>

                    <template v-if="step == 4">
                        <template v-for="configuratorItem in BodyWoods" :key="configuratorItem.id">
                            <RadioButton :configuratorItem="configuratorItem" />
                        </template>
                    </template>

                    <template v-if="step == 5">
                        <template v-for="configuratorItem in NeckWoods" :key="configuratorItem.id">
                            <RadioButton :configuratorItem="configuratorItem"/>
                        </template>
                    </template>

                    <template v-if="step == 6">
                        <template v-for="configuratorItem in Electronics" :key="configuratorItem.id">
                            <RadioButton :configuratorItem="configuratorItem"/>
                        </template>
                    </template>  

                    </form> -->
                </div>
                
                <button class="btn btn-info my-2">Save configuration and quit</button>
                
                <button class="btn btn-success my-2">Complete and add to cart</button>
                <p class="text-color-success my-2">Total: €</p>
            </div>
        </div>
    </div>

</template>

<script>
    export default {
        name: 'ConfiguratorContent',
        data(){
            return {
                APIData: [],
                // Misc: [],
                // Frets:[],
                // Colors:[],
                // BodyWoods:[],
            }
        },
        components: {
            RadioButton
        },
        created (){
            getAPI.get('/api/v1/item/',)
            .then(response => {
                console.log('data fetch from API successful')
                this.APIData = response.data

            })
            .catch(error => {
                console.log(error)
            })    
        }
    }
</script>

<style scoped>

</style>
    