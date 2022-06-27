<template>
  <div class="w-full pt-20 bg-gray-200 min-h-screen">
    <h2 class="text-green-500 text-center text-4xl font-semibold mb-10">
      Build your short URL
    </h2>

    <div class="flex items-center justify-center">
      <div class="w-8/12 flex flex-col justify-center items-center px-10">
        <!-- Form component -->
        <Form @ShortenedLink='handleShortenedLink' />
        
        <!-- Link component -->
        <Link v-if='shortened_link'/>
      </div>
    </div>
  </div>
</template>

<script>
  import Form from '~/components/Form'
  import Link from '~/components/Link'

  export default {
    components: {
      Form,
      Link
    },

    data() {
      return {
        shortened_link: null
      }
    },

    methods: {
      handleShortenedLink(link) {
        let code = link.split('/').slice(-1)
        this.$data.shortened_link = `http://localhost:3000/${code}`
      }
    }
  }
</script>
