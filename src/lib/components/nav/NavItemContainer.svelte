<script>
	import { Menu, X } from "@lucide/svelte";

	let { children } = $props();

	let isDropdownOpen = $state(false);  // default state
	const onClickDropdown = () => {
		isDropdownOpen = !isDropdownOpen;
	}
	$inspect(isDropdownOpen);
</script>

<nav class="ml-auto">
	<!-- Small screens -->
	<button 
		class="block md:hidden hover:bg-gray-200 dark:hover:bg-neutral-700 rounded-sm p-1 ml-auto mr-0"
		onclick={onClickDropdown}
	>
		<!-- Menu icon -->
		<Menu />
	</button>

	<div class="{isDropdownOpen ? 'block' : 'hidden'} md:hidden fixed top-0 left-0 mt-0 px-8 pb-4 h-full w-screen bg-white dark:bg-neutral-900 overflow-scroll">
		<button 
		class="block md:hidden hover:bg-gray-200 dark:hover:bg-neutral-700 rounded-sm p-1 mt-8 ml-auto mr-0"
		onclick={onClickDropdown}
		>
			<X />
		</button>
		<ul>
			{@render children()}
		</ul>
	</div>


	<!-- Medium screens -->
	<ul class="hidden md:flex">
		{@render children()}
	</ul>
</nav>

