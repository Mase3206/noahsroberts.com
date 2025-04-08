<script lang="ts">
	import DotSeparator from "$lib/components/DotSeparator.svelte";
	import PostList from "$lib/components/PostList.svelte";

	export let data;
	const { posts } = data;

	// let posts: { meta: any, path: string }[] = [];

	// // modifies `posts` directly
	// async function fetchPosts() {
	// 	const response = await fetch('/api/posts');
	// 	posts = await response.json();
	// }
	
	// fetchPosts();
</script>

<h1>Welcome.</h1>
<img src="https://noahsroberts.com/wp-content/uploads/2023/10/headshot-1-edited-3.jpg?w=2046" alt="" />

<p>
	Hey there! I am an Eagle Scout and Computer Science major with a minor in German at the University of Montana. I am a member of the Davidson Honors College and the Franke Global Leadership Initiative. I enjoy music, theater, transit design, being outside, and learning about the world.
</p>

<DotSeparator />

<h2>Recent updates</h2>

<PostList {posts} />