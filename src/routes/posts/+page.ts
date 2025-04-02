import type { List } from 'immutable';

export async function load({ fetch }) {
	const response = await fetch('/api/posts');

	// add le type
	const posts: { meta: any, path: string, }[] = await response.json();

	return { posts };
}