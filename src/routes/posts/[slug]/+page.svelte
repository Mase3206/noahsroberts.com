<script>
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
	<p>Published: {date}</p>
	<Content />
</article>


<aside>
	{#if categories}
		<h2>Posted in:</h2>
		<ul>
			{#each categories as category}
				<li><a href="/blog/category/{category}">{category}</a></li>
			{/each}
		</ul>
	{:else}
		<h2>Not posted in any categories.</h2>
	{/if}
</aside>