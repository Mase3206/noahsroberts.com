<script>
	import { ChevronDown } from "@lucide/svelte";
	import NavItem from "./NavItem.svelte";

	let { children, title, href } = $props();
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



<div id="items">
	<!-- <button>Items</button> -->
	<div class="flex">
		<NavItem {href} isDropdownTitle={true}>{title}</NavItem>
		<ChevronDown class="w-4 md:mr-3" />
	</div>

	<ul class="hidden shadow bg-base-100 absolute pt-2 pr-4 border-[0.5px] md:ml-3 max-w-50">
		{@render children()}
	</ul>
</div>