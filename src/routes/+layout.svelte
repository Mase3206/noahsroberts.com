<script>
	import Navbar from '$lib/components/nav/Navbar.svelte';
	import NavItem from '$lib/components/nav/NavItem.svelte';
	import NavBrand from '$lib/components/nav/NavBrand.svelte';
	import NavItemContainer from '$lib/components/nav/NavItemContainer.svelte';

	import Footer from '$lib/components/Footer.svelte'
	import '$lib/css/main.css'
	// import '$lib/styles/style.sass'
</script>

<Navbar>
	<NavBrand>Noah S. Roberts</NavBrand>

	<NavItemContainer>
		<NavItem href="/posts">Posts</NavItem>
		<NavItem href="/resume">Resume</NavItem>
	</NavItemContainer>
</Navbar>

<main class="p-4 my-8 mx-auto max-w-160 overflow-hidden md:overflow-auto">
	<slot />
</main>

<Footer />