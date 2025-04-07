<script>
	import Navbar from '$lib/components/nav/Navbar.svelte'
	// import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, Dropdown, DropdownItem, DropdownDivider } from 'flowbite-svelte';
  // import { ChevronDownOutline } from 'flowbite-svelte-icons';
  // import { page } from '$app/stores';  // TODO: figure out deprecation
  // $: activeUrl = $page.url.pathname;

	import Footer from '$lib/components/Footer.svelte'
	import '$lib/css/main.css'
	// import '$lib/styles/style.sass'
</script>

<Navbar />

<main class="p-4 my-8 mx-auto max-w-160 overflow-hidden md:overflow-auto">
	<slot />
</main>

<Footer />