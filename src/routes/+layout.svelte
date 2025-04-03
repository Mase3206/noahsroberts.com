<script>
	import DesktopNavbar from '$lib/components/DesktopNavbar.svelte'
	import Footer from '$lib/components/Footer.svelte'
	import '$lib/styles/style.sass'
</script>

<DesktopNavbar />

<main>
	<slot />
</main>

<Footer />