<script lang="ts">
	import { getAllPosts } from "$lib/utils/fetchPosts";
	let { category = '' } = $props();

	let promisePosts = getAllPosts(category);
</script>


{#await promisePosts}
	<p>Fetching posts...</p>
{:then posts}
	<ul>
		{#each posts as post}
			<li>
				<h2><a href="{post.path}">{post.meta.title}</a></h2>
				Published {post.meta.date}
			</li>
		{/each}
	</ul>
{:catch error}
	<p>{error}</p>
{/await}
