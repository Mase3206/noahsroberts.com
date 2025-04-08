<script>
	// not a prop, filled in internally
	export let data;
	const { posts } = data;

	import PostList from '$lib/components/PostList.svelte';
</script>

<h1>Posts</h1>

<PostList {posts} />

<!-- <ul>
	{#each data.posts as post}
		<li>
			<h2><a href="{post.path}">{post.meta.title}</a></h2>
			Published {post.meta.date}
		</li>
	{/each}
</ul> -->
