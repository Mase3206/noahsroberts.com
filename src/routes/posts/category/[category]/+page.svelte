<script>
	// filled in by API, not prop
	export let data;
	const { category } = data;

	import PostList from '$lib/components/PostList.svelte'
</script>

<h1>Posts under {category}</h1>
<PostList {category} />
