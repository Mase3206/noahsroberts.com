<script>
	import DesktopNavbar from '$lib/components/DesktopNavbar.svelte'
	import Footer from '$lib/components/Footer.svelte'
	import '$lib/css/main.css'
	// import '$lib/styles/style.sass'
</script>

<DesktopNavbar />

<main class="p-4 my-8 mx-auto max-w-160">
	<slot />
</main>

<Footer />