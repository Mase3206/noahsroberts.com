import { mdsvex } from 'mdsvex';
// import adapter from '@sveltejs/adapter-static';
import adapter from '@sveltejs/adapter-cloudflare';
// import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
import rehypeCallouts from 'rehype-callouts';

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
	kit: { adapter: adapter() },
	extensions: ['.svelte', '.md'],
};

export default config;
