
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
      <v-container class="pt-0">


        <section>
          <v-layout
            column
            wrap
            class="mt-0"
            align-center
          >
            <v-flex md6>
              <v-container grid-list-xl>
                <v-layout row wrap align-center>

                  <v-flex xs6>
                    <v-card class="elevation-0 transparent ">
                      <div v-if="playingVideos">
                        <v-card-title primary-title class="layout justify-left">
                          <div class="headline" style="font-size:30px; line-height: 40px; text-align: left; font-family:NexaBold; font-weight:30px;"> Processing Video... </div>
                        </v-card-title>
                      </div>
                      <div v-else>
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
                      </div>
                    </v-card>
                  </v-flex>

                  <v-flex xs6 >
                    <v-card class="elevation-0 transparent ">
                      <vue-dropzone ref="myVueDropzone"  :options="dropzoneOptions" acceptedFileTypes=".mp4" v-on:vdropzone-success="showSuccess" :include-styling="false"
                                    id="customdropzone"> </vue-dropzone>

                      <div v-if="playingVideos" >
                        hi
                      </div>
                    </v-card>
                  </v-flex>

                </v-layout>
              </v-container>
            </v-flex>
          </v-layout>
        </section>

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

  #customdropzone {
    background-image: url("../assets/mediumSlow.gif");
    background-size: 500px;
    font-family: 'Nexa Bold', sans-serif;
    letter-spacing: 0.2px;
    color: #777;
    transition: background-color .2s linear;
    height: 600px;
    width: 600px;
    margin-top: 100px;
  }

  #customdropzone .dz-preview {
    width: 160px;
    display: inline-block
  }
  #customdropzone .dz-preview .dz-image {
    width: 80px;
    height: 80px;
    margin-left: 40px;
    margin-bottom: 10px;
  }
  #customdropzone .dz-preview .dz-image > div {
    width: inherit;
    height: inherit;
    border-radius: 50%;
    background-size: contain;
  }
  #customdropzone .dz-preview .dz-image > img {
    width: 100%;
  }

  #customdropzone .dz-preview .dz-details {
    color: black;
    transition: opacity .2s linear;
    text-align: center;
    padding-right: 10px;
  }
  #customdropzone .dz-success-mark, .dz-error-mark, .dz-remove {
    display: none;
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
        playingVideos: false,
        dropzoneOptions: {
          url: 'http://127.0.0.1:5000/api/video',
          thumbnailWidth: 150,
          maxFilesize: 10,
          previewTemplate: this.template(),
          headers: { 'enctype': 'multipart/form-data' }
        },
        randomNumber: 0

      }
    },
    methods: {
      showSuccess (file, response) {
        this.playingVideos = true
      },
      template: function () {
        return `<div class="dz-preview dz-file-preview">
                  <div class="dz-image">
                      <div data-dz-thumbnail-bg></div>
                  </div>

                  <div class="dz-progress"><span class="dz-upload" data-dz-uploadprogress></span></div>
                  <div class="dz-error-message"><span data-dz-errormessage></span></div>
                  <div class="dz-success-mark"><i class="fa fa-check"></i></div>
                  <div class="dz-error-mark"><i class="fa fa-close"></i></div>
              </div>
          `
      },
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
