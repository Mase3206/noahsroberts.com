/// Fetch all Markdown posts in the /src/routes/posts directory.
export async function fetchMarkdownPosts() {
	// Vite function; imports all files matching the glob.
	// Each file is an object where each file’s relative path is the key, and the value is a “resolver” function
	// that loads the file contents as a JavaScript promise.
	const allPostFiles = import.meta.glob('/src/routes/posts/*.md');
	const iterablePostFiles = Object.entries(allPostFiles);

	// since each file is a Promise, we gotta wrap it in one
	const allPosts = await Promise.all(
		iterablePostFiles.map(async ([path, resolver]) => {
			const { metadata } = await resolver() as { metadata: any };
			// strip the parent path and the extension
			const postPath = path.slice(11, -3);

			return {
				meta: metadata,
				path: postPath,
			};
		})
	)

	return allPosts;
}
