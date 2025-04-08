<script lang="ts">
  import type { Snippet } from "svelte";

	let { 
		children, 
		href, 
		isDropdownTitle = false,
		classes = "",
	}: {
		children: Snippet;
		href: string;
		isDropdownTitle?: boolean;
		classes?: string;
	} = $props();
</script>

<li class="mb-2 md:ml-3 {isDropdownTitle ? 'md:mr-1' : 'md:mr-3'} text-base nav-item">
	<a {href} class="no-underline hover:underline {classes}">
		{@render children()}
	</a>
</li>