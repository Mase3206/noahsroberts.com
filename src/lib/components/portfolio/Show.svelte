<script lang="ts">
	import type { Snippet } from 'svelte';
	
	let {
		details,
		title,
		author,
		children,
	}: {
		details: { name: string, content: string }[];
		title: string;
		author: string;
		children: Snippet;
	} = $props();
</script>

<style>
	/* remove the bottom margin from the children of Show elements, as it makes the background look bad */
	:global(p):last-child {
		margin-bottom: 0em;
	}
</style>

{#snippet detail(d: { name: string, content: string })}
	<div class="block mr-4">
		<p class="font-bold mb-0">{d.name}</p>
		<p class="mt-0">{d.content}</p>
	</div>
{/snippet}


<div class="bg-gray-100 p-8 mb-8">
	<div>
		<h2 class="italic mb-0 mt-0">{title}.</h2>
		<p class="mt-0 mb-2">by {author}</p>
	</div>

	<div class="flex flex-wrap">
		{#each details as d}  <!-- Iterate over all of the given details -->
			{@render detail(d)}
		{/each}
	</div>

	<div>
		{@render children()}
	</div>
</div>
