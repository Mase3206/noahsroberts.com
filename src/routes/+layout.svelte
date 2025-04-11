<script>
	import Navbar from '$lib/components/nav/Navbar.svelte';
	import NavItem from '$lib/components/nav/NavItem.svelte';
	import NavBrand from '$lib/components/nav/NavBrand.svelte';
	import NavItemContainer from '$lib/components/nav/NavItemContainer.svelte';
	import NavDropdown from '$lib/components/nav/NavDropdown.svelte';

	import Footer from '$lib/components/Footer.svelte'
	import '$lib/css/main.css'
	// import '$lib/styles/style.sass'
</script>

<Navbar>
	<NavBrand>Noah S. Roberts</NavBrand>

	<NavItemContainer>
		<NavDropdown href="/education" title="Education">
			<NavItem href="/education/dhc">DHC</NavItem>
			<NavItem href="/education/gli">GLI</NavItem>
		</NavDropdown>
		
		<!-- code, scouts, theatre, homelab -->
		<NavDropdown href="/hobbies" title="Hobbies">
			<NavItem href="/hobbies/code">Code</NavItem>
			<NavItem href="/hobbies/scouts">Scouts</NavItem>
			<NavItem href="/hobbies/theatre">Theatre</NavItem>
			<NavItem href="/hobbies/homelab">Homelab</NavItem>
		</NavDropdown>

		<NavItem href="/posts">Posts</NavItem>
		<NavItem href="/resume"><span class="font-semibold">Resume</span></NavItem>
	</NavItemContainer>
</Navbar>

<main class="px-8 py-0 my-8 mx-auto max-w-180 overflow-x-visible whitespace-no-wrap">
	<slot />
</main>

<Footer />