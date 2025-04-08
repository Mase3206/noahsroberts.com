<script lang="ts">
  import type { Snippet } from "svelte";

	let { 
		children, 
		href, 
		isDropdownTitle = false,
	}: {
		children: Snippet;
		href: string;
		isDropdownTitle?: boolean;
	} = $props();
</script>

<li class="mb-2 md:ml-3 {isDropdownTitle ? 'md:mr-1' : 'md:mr-3'} text-base nav-item">
	<a {href} class="no-underline hover:underline">
		{@render children()}
	</a>
</li>