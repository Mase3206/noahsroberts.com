export async function load({ fetch, params }) {
	const { category } = params;

	return {
		category,
	};
}