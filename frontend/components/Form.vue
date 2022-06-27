<template>
  <form @submit.prevent='handleSubmit' class="w-full mb-10">
    <input v-model="url" type="text" class="w-full p-2 placeholder-gray-500 block outline-none block outline-none rounded-lg shadow-lg my-4" placeholder="Paste your long link here" id="" name="">

    <button class="block py-2 bg-blue-500 w-full focus:outline-name rounded-lg shadow-md text-gray-100 font-semibold uppercase">
      build short url
    </button>
  </form>
</template>

<script>
  export default {
    data() {
      return {
        url: ''
      }
    },

    methods: {
      async handleSubmit() {
        try {
          const formdata = new FormData()
          formdata.append('original_link', this.$data.url)

          const res = await fetch('http://localhost:8000/api/create/', {
            method: 'POST',
            body: formdata
          })

          if (!res.ok) {
            throw Error('error')
          }

          const data = await res.json()
          this.$data.url = ''

          this.$emit('ShortenedLink', data['shortened_link'])
        } catch(err) {
          console.log(err.message);
        }
      }
    }
  }
</script>

<style>

</style>
