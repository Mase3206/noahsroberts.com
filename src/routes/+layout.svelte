<script>
	import Header from '$lib/components/Header.svelte'
	import '$lib/styles/style.sass'
	import '$lib/styles/prism-gruvbox-dark.css'
</script>

<Header />

<main>
	<slot />
</main>

<footer>And this is the footer.</footer>