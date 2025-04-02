import { mdsvex } from 'mdsvex';
import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

const config = {
	preprocess: [
		vitePreprocess(), 
		mdsvex({
			extensions: ['.md']
		})
	],
	kit: { adapter: adapter() },
	extensions: ['.svelte', '.md']
};

export default config;
