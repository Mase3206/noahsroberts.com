<script>
	let { posts } = $props();
</script>

<ul>
	{#each posts as post}
		<li>
			<h2><a href="{post.path}">{post.meta.title}</a></h2>
			Published {post.meta.date}
		</li>
	{/each}
</ul>