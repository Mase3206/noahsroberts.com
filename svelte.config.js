import { mdsvex } from 'mdsvex';
// import adapter from '@sveltejs/adapter-static';
import adapter from '@sveltejs/adapter-cloudflare';
// import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
import rehypeCallouts from 'rehype-callouts';
import fs from 'fs';
import path from 'path';


// Read all Markdown files in the "posts" directory
const postsDirectory = path.resolve('src/routes/posts');
const files = fs.readdirSync(postsDirectory)
	.filter((file) => file.endsWith('.md'));

// Generate routes for each post
const postRoutes = files.map((file) => `/posts/${file.replace('.md', '')}`);


const config = {
	preprocess: [
		// vitePreprocess(),  // sass preprocessor/
		mdsvex({
			extensions: ['.md'],
			rehypePlugins: [ rehypeCallouts ],
			layout: {
				// no layout for posts, as those are handled dynamically
				
				normal_page: 'src/lib/layouts/normal_page.svelte',
			},
		})
	],
	kit: {
		adapter: adapter(),
		prerender: {
			entries: [
				'/',
				'/posts',
				...postRoutes
			]
		}
	},
	extensions: ['.svelte', '.md'],
};

export default config;
