<script>
	// filled in by API, not prop
	export let data;
	const { category, posts } = data;

	import PostList from '$lib/components/PostList.svelte'
</script>

{#if posts}
	<h1>Posts under {category}</h1>
	<PostList {posts} />
{:else}
	<h1>No posts found under {category}</h1>
{/if}
