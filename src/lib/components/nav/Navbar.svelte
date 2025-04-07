<!-- Header.svelte -->

<script>
	import NavItem from '$lib/components/nav/NavItem.svelte';
	import NavBrand from './NavBrand.svelte';
	import NavItemContainer from './NavItemContainer.svelte';
</script>

<header class="flex mx-8 p-0">
	<NavBrand>Noah S. Roberts</NavBrand>

	<NavItemContainer>
		<NavItem href="/posts">Posts</NavItem>
		<NavItem href="/resume">Resume</NavItem>
	</NavItemContainer>
</header>