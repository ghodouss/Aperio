
<template>
  <v-app light>
    <v-toolbar flat class="white pb-5 mr-5 pr-5 pl-5 pt-0 mt-0" height="60" >
      <img src="../assets/aperioLogo.png" alt="Vuetify.js" height="90">
      <v-spacer></v-spacer>
      <v-toolbar-side-icon class="hidden-md-and-up"></v-toolbar-side-icon>
      <v-toolbar-items class="hidden-sm-and-down pr-5" style="font-family:NexaBold" >
        <img src="../assets/aboutButton.png" alt="Vuetify.js" class="mr-5 pr-5"  height="60">
      </v-toolbar-items>
    </v-toolbar>

    <v-content>
      <v-container>


        <section>
          <v-layout
            column
            wrap
            class=""
            align-center
          >
            <v-flex md6>
              <v-container grid-list-xl>
                <v-layout row wrap align-center>

                  <v-flex xs6>
                    <v-card class="elevation-0 transparent">
                      <v-card-text class="text-xs-left">

                      </v-card-text>
                      <v-card-title primary-title class="layout justify-left">
                        <div class="headline" style="font-size:30px; line-height: 40px; text-align: left; font-family:NexaBold; font-weight:20px;">Machine Learning
                          for Video Enhancement</div>
                      </v-card-title>
                      <v-card-text  class="layout justify-left " style=" font-size:20px; line-height: 23px; text-align: left; font-family:NexaLight; font-weight:20px" >
                        Our state of the art neural networks
                        boost video resolution and double the
                        frame rate.

                        <br>
                        <br>

                        Drag and drop a video to begin.
                      </v-card-text>
                    </v-card>
                  </v-flex>

                  <v-flex xs6 >
                    <v-card class="elevation-0 transparent">
                      <img src="../assets/mediumSlow.gif" alt="Vuetify.js" class="mr-4"  height="600">
                    </v-card>
                  </v-flex>

                </v-layout>
              </v-container>
            </v-flex>
          </v-layout>
        </section>
        <vue-dropzone ref="myVueDropzone" id="dropzone" :options="dropzoneOptions"></vue-dropzone>

      </v-container>
    </v-content>
  </v-app>

</template>

<style type="text/css">
  @font-face {
    font-family: NexaBold;
    src: url('../assets/fonts/nexa/Nexa Bold.otf');
  }
  @font-face {
    font-family: NexaLight;
    src: url('../assets/fonts/nexa/Nexa Light.otf');
  }
</style>

<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script src="https://unpkg.com/vuetify/dist/vuetify.js"></script>
<script >
  import vue2Dropzone from 'vue2-dropzone'
  import 'vue2-dropzone/dist/vue2Dropzone.css'
  import axios from 'axios'
  export default {
    name: 'app',
    components: {
      vueDropzone: vue2Dropzone
    },
    data () {
      return {
        dropzoneOptions: {
          url: 'http://127.0.0.1:5000/',
          thumbnailWidth: 150,
          maxFilesize: 0.5,
          headers: { 'My-Awesome-Header': 'header value' }
        },
        randomNumber: 0
      }
    },
    methods: {
      getRandomInt (min, max) {
        min = Math.ceil(min)
        max = Math.floor(max)
        return Math.floor(Math.random() * (max - min + 1)) + min
      },
      getRandom () {
        // this.randomNumber = this.getRandomInt(1, 100)
        this.randomNumber = this.getRandomFromBackend()
      },
      getRandomFromBackend () {
        const path = `http://localhost:5000/api/random`
        axios.get(path)
        .then(response => {
          this.randomNumber = response.data.randomNumber
        })
        .catch(error => {
          console.log(error)
        })
      }
    },
    created () {
      this.getRandom()
    }
  }
</script>
