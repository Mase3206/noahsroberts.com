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

<main class="px-8 py-0 my-8 mx-auto max-w-180 overflow-x-visible whitespace-no-wrap">
	<slot />
</main>

<Footer />