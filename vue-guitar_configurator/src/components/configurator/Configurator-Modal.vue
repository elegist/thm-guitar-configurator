<script setup>
    import ConfiguratorContent from './Configurator-Content.vue';
</script>

<template>
    <div
        class="modal"
        :id="`${model.name}-configuratorModalStep${step}`"
        data-bs-backdrop="static"
        data-bs-keyboard="false"
        tabindex="-1"
        aria-labelledby="configuratorModalLabel"
        aria-hidden="true"
    >
        <div
            class="modal-dialog modal-xl modal-dialog-centered modal-fullscreen-xl-down"
        >
            <div class="modal-content modal-dark">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="configuratorModalLabel">
                        Configure your own {{ model.name }}
                    </h1>
                    <button
                        class="btn-close btn-close-white"
                        type="button"
                        data-bs-dismiss="modal"
                        aria-label="Close"
                    ></button>
                </div>
                
                <div class="modal-body">
                    <ConfiguratorContent />    
                </div>

                
                <div class="modal-footer d-flex justify-content-center">

                    <template v-if="step == 1">
                        <button type="button" class="btn btn-outline-info" disabled>
                        <BootstrapIcon
                            icon="caret-left-fill"/>
                        </button>
                    </template>

                    <template v-else>
                        <button type="button" class="btn btn-outline-info" :data-bs-target="`#${model.name}-configuratorModalStep${step - 1}`" data-bs-toggle="modal">
                        <BootstrapIcon
                            icon="caret-left-fill"/>
                        </button>
                    </template>

                    <div class="progress w-25" style="height: 2rem">
                        <div
                            class="progress-bar text-center"
                            role="progressbar"
                            aria-label="Configurator progress"
                            aria-valuemin="0"
                            aria-valuemax="5"
                            aria-valuenow="1"
                            :style="`width: calc(100% / ${ maxStep } * ${ step })`">
                        <!-- set percentage for the width on each modal -->
                            {{ step }} / {{ maxStep }}
                        </div>
                    </div>

                    <template v-if="step == maxStep">
                        <button type="button" class="btn btn-outline-info" disabled>
                        <BootstrapIcon
                            icon="caret-right-fill"/>
                        </button>
                    </template>

                    <template v-else>
                        <button type="button" class="btn btn-outline-info" :data-bs-target="`#${model.name}-configuratorModalStep${step + 1}`" data-bs-toggle="modal">
                        <BootstrapIcon
                            icon="caret-right-fill"/>
                        </button>
                    </template>
                    
                </div>
            </div>
        </div>
    </div>
</template>

<script>   
    export default {
        name: "ConfiguratorModal",
        components: {  
            ConfiguratorContent,
        },
        props: ["model", "step", "maxStep"],
    }
</script>
<style scoped>

</style>
    