export async function load({ fetch, params }) {
	const { category } = params;
	const response = await fetch(`/api/posts`);
	const allPosts: { meta: { title: string, date: string, categories: string[] }, path: string }[] = await response.json();

	const posts = allPosts.filter((post) => {
		if (post.meta.categories == null) {
			return false;
		} else {
			return post.meta.categories.includes(category)
		}
	});

	return {
		category,
		posts,
	};
}