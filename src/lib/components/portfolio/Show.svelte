<script lang="ts">
	import type { Snippet } from 'svelte';
	
	let {
		title,
		author,
		details,
		children,
	}: {
		title: string;
		author: string;
		details: { name: string, content: string }[];
		children: Snippet;
	} = $props();

	let width = 75;  // em
</script>


<style>
	/* remove the bottom margin from the children of Show elements, as it makes the background look bad */
	:global(p):last-child {
		margin-bottom: 0em;
	}

	.show-card {
		position: relative;
		z-index: -1;
	}
</style>


{#snippet detail(d: { name: string, content: string })}
	<div class="block mr-4">
		<p class="font-bold mb-0">{d.name}</p>
		<p class="mt-0">{d.content}</p>
	</div>
{/snippet}


<div class="bg-neutral-100 dark:bg-neutral-800 p-8 mb-8 overflow-visible show-card w-{width * 4}" style="left: {-((width) / 4) + 1.5}em">
	<div>
		<h2 class="italic mb-0 mt-0">{title}.</h2>
		<p class="mt-0 mb-2">by {author}</p>
	</div>

	<div class="flex flex-wrap">
		<!-- Iterate over all of the given details -->
		{#each details as d}
			{@render detail(d)}
		{/each}
	</div>

	<div>
		{@render children()}
	</div>
</div>
