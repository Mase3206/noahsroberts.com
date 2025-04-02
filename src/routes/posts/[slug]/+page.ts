// TODO: should prolly have a try-catch block
export async function load({ params }) {
	const post = await import(`../${params.slug}.md`);
	const { title, date } = post.metadata;
	const Content = post.default;

	return {
		title,
		date,
		Content,
	};
}