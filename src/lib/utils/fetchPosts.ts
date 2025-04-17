import type { Post } from ".";

export async function getAllPosts(category: string) {
	const response = await fetch(`/api/posts`);
	const allPosts: Post[] = await response.json();

	const filteredPosts = allPosts.filter((post) => {
		// no categories in the post
		if (post.meta.categories == null) {
			return false;
		// no category given, get all of the posts
		} else if (category == '') {
			return true;
		// otherwise, filter it
		} else {
			return post.meta.categories.includes(category);
		}
	});


	return new Promise<Post[]>((fulfil, reject) => {
		if (filteredPosts == null || filteredPosts.length <= 0) {
			if (category != '') {
				reject(`No posts found under the "${category}" category.`)
			} else {
				reject("No posts found.")
			}
		}

		fulfil(filteredPosts);
	})
} 