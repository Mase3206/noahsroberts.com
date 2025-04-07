import { mdsvex } from 'mdsvex';
import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

const config = {
	preprocess: [
		// vitePreprocess(),  // sass preprocessor
		mdsvex({
			extensions: ['.md'],
			layout: {
				// no layout for posts, as those are handled dynamically
				
				normal_page: 'src/lib/layouts/normal_page.svelte',
			}
		})
	],
	kit: { adapter: adapter() },
	extensions: ['.svelte', '.md'],
};

export default config;
