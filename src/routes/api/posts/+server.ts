import { fetchMarkdownPosts } from "$lib/utils";
import { json } from "@sveltejs/kit";

export async function GET() {
	const allPosts = await fetchMarkdownPosts();

	try {
		// Sort all posts in descending order
		const sortedPosts = allPosts.sort((a, b) => {
			let aDate = new Date(a.meta.date);
			let bDate = new Date(b.meta.date);
	
			// use the difference in their milliseconds since the Unix Epoch to sort in descending order
			return bDate.getTime() - aDate.getTime();
		});
		
		// export the data as json and set the proper headers
		return json(sortedPosts);
	} catch (TypeError) {
		// export the data as json and set the proper headers
		return json([]);
	}
}