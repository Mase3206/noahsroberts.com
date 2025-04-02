<!-- post.svelte -->
<script>
	let { 
		// metadata
		title,
		date,
		// post content
		children
	} = $props();
	
</script>

<article>
	<h1>{title}</h1>

	<p>Published: {date}</p>

	{@render children?.() }
</article>