<script>
	import { formatDate } from '$lib/utils/format.js';

	// mdsvex doesn't really work with v5, runes, and $props.
	export let data;
	const { title, date, categories, Content } = data;
</script>

<style>
	h1 {
		font-weight: normal;
		text-align: left;
		margin-bottom: 1em;
	}
</style>

<article>
	<h1>{title}</h1>
	<Content />
</article>


<div>
	<hr class="mt-24" />
	<p>Published: {formatDate(date)}</p>
	{#if categories}
		<p>Posted in:
			{#each categories as category}
				<a href="/posts/category/{category}">{category}</a>&nbsp;&nbsp;
			{/each}
		</p>
	{:else}
		<p>Not posted in any categories.</p>
	{/if}
	</div>