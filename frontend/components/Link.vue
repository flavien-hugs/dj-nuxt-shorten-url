<template>
	<div class="w-8/12 mx-auto flex justify-between items-center my-5 bg-gray-500 px-5 py-3 rounded-sm">
		<div>
			<p class="text-gray-100">
				{{ shortened_link }}
			</p>
		</div>

		<div>
			<button
				@click="copyClipBoard"
				class="py-1 px-3 bg-blue-500 rounded-sm text-gray-100 focus:outline-none focus:bg-blue-700">
				copy link
			</button>
		</div>
	</div>
</template>

<script>
	export default {
		props: [
			'shortened_link'
		],
		methods: {
			copyClipBoard() {
				navigator.clipboard.writeText(this.$props.shortened_link)
				alert('Link Copied !')
			}
		}
	}
</script>

<style>

</style>
