<script>
	import { ChevronDown } from "@lucide/svelte";
	import NavItem from "./NavItem.svelte";

	let { children, title, href } = $props();

	// let isMobileDropdownOpen = $state(false);  // default state
	// const onClickDropdown = () => {
	// 	isMobileDropdownOpen = !isMobileDropdownOpen;
	// }
	// $inspect(isMobileDropdownOpen);
</script>

<style>
	#items:hover,
  #items:focus,
  #items:hover > ul,
  #items:focus > ul {
    display: block;
    opacity: 1;
  }
</style>


<div class="block md:hidden">
	<NavItem {href} isDropdownTitle={true} classes="font-semibold">{title}</NavItem>
	<div class="ml-6 mb-6">
		{@render children()}
	</div>
</div>


<!-- Medium screens -->
<div id="items" class="hidden md:block">
	<div class="flex">
		<NavItem {href} isDropdownTitle={true}>{title}</NavItem>
		<ChevronDown class="w-4 md:mr-3" />
	</div>

	<ul class="hidden shadow bg-base-100 absolute pt-2 pr-4 border-[0.5px] md:ml-3 max-w-50">
		{@render children()}
	</ul>
</div>