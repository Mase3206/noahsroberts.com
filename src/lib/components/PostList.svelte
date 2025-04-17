<script lang="ts">
	import { getAllPosts } from "$lib/utils/fetchPosts";
	import { formatDate } from "$lib/utils/format";
	let { category = '' } = $props();

	let promisePosts = getAllPosts(category);
</script>


{#await promisePosts}
	<p>Fetching posts...</p>
{:then posts}
	<ul>
		{#each posts as post}
			<li>
				<h3><a href="{post.path}">{post.meta.title}</a></h3>
				Published: {formatDate(post.meta.date)}
			</li>
		{/each}
	</ul>
{:catch error}
	<p>{error}</p>
{/await}
