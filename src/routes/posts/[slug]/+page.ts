// TODO: should prolly have a try-catch block
export async function load({ params }) {
	const post = await import(`../${params.slug}.md`);
	// const { title, date, categories } = post.metadata;
	const title = post.metadata.title;
	const date = post.metadata.date;
	// const categories = (): ArrayLike<string> => {
		// }
	let categories: string[];
	try {
		categories = post.metadata.categories;
	} catch (TypeError) {
		categories = [];
	}


	const Content = post.default;

	return {
		title,
		date,
		categories,
		Content,
	};
}